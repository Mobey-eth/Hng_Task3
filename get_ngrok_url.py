import requests
import time

def get_ngrok_url():
    while True:
        try:
            response = requests.get('http://localhost:4040/api/tunnels')
            data = response.json()
            tunnels = data['tunnels']
            for tunnel in tunnels:
                if tunnel['proto'] == 'https':
                    print("Ngrok URL:", tunnel['public_url'])
                    return
        except Exception as e:
            print("Error:", e)
        time.sleep(2)

if __name__ == "__main__":
    get_ngrok_url()
