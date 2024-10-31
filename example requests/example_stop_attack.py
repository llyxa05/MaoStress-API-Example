import requests

def stop_attack(user, api_key, address):
    url = "https://mao-stress.tech/api/stop.php"
    params = {
        'user': user,
        'api_key': api_key,
        'address': address
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Attack stopped successfully.")
            print("Response:", response.json())
        else:
            print("Failed to stop attack.")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
user_id = 2
api_key = "yourapikey"
address = "1.1.1.1"

stop_attack(user_id, api_key, address)
