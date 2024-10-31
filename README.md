# MAO Example API

Этот репозиторий содержит примеры использования API для запуска и остановки атак, а также простого Telegram-бота для управления атаками.

This repository contains examples of using the API to start and stop attacks, as well as a simple Telegram bot for managing attacks.

## Структура проекта / Project Structure

- **example requests / Примеры запросов**
  - `example_send_attack.py`: скрипт для отправки запроса на запуск атаки через API.  
    Script for sending a request to start an attack via the API.
  - `example_stop_attack.py`: скрипт для отправки запроса на остановку атаки через API.  
    Script for sending a request to stop an attack via the API.

- **example telegram bot / Пример Telegram бота**
  - `bot.py`: простой Telegram-бот для взаимодействия с API, который позволяет запускать и останавливать атаки через Telegram.  
    A simple Telegram bot for interacting with the API, allowing you to start and stop attacks via Telegram.

## Описание скриптов / Script Descriptions

### example_send_attack.py
Этот скрипт отправляет GET-запрос к API для запуска атаки. Он использует следующие параметры:  
This script sends a GET request to the API to start an attack. It uses the following parameters:

- `user`: ID пользователя / User ID.
- `api_key`: ключ API / API key.
- `target`: IP-адрес или домен для атаки / Target IP address or domain.
- `port`: порт для атаки / Port for the attack.
- `duration`: длительность атаки в секундах / Duration of the attack in seconds.
- `method`: метод атаки (например, DNS) / Attack method (e.g., DNS).

#### Пример использования / Example Usage
```python
user_id = 2
api_key = "yourapikey"
target = "1.1.1.1"
port = 80
duration = 30
method = "DNS"

send_attack(user_id, api_key, target, port, duration, method)

### example_stop_attack.py
Этот скрипт отправляет GET-запрос к API для остановки атаки. Он использует следующие параметры:  
This script sends a GET request to the API to stop an attack. It uses the following parameters:

- `user`: ID пользователя / User ID.
- `api_key`: ключ API / API key.
- `address`: IP-адрес атаки для остановки / IP address of the attack to stop.

#### Пример использования / Example Usage
```python
user_id = 2
api_key = "yourapikey"
address = "1.1.1.1"

stop_attack(user_id, api_key, address)
```

### bot.py
Этот скрипт представляет собой Telegram-бота для взаимодействия с API, позволяя пользователям запускать и останавливать атаки через команды в Telegram.  
This script is a Telegram bot for interacting with the API, allowing users to start and stop attacks via commands in Telegram.

- Убедитесь, что у вас установлен `python-telegram-bot`, и замените токен в скрипте на свой.  
  Make sure you have `python-telegram-bot` installed, and replace the token in the script with your own.

## Требования / Requirements

- Python 3.x
- `requests` библиотека для HTTP-запросов / `requests` library for HTTP requests
- `python-telegram-bot` библиотека для работы с Telegram API / `python-telegram-bot` library for working with the Telegram API

Установите зависимости с помощью следующей команды:  
Install the dependencies using the following command:

```bash
pip install requests python-telegram-bot
```

## Замечание / Note

Этот проект предоставлен только в ознакомительных целях. Использование API и данного бота предполагает соблюдение всех соответствующих законов и правил.
This project is provided for educational purposes only. Using the API and this bot implies compliance with all applicable laws and regulations.
```

Этот README предоставляет подробное описание файлов и инструкций на русском и английском языках.
