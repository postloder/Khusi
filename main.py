import os
import requests
import time
from datetime import datetime

# Clear screen function
def cls():
    print("\033[2J\033[H", end="")

# Logo display function
def logo():
    print("""
\033[1;36m
𝗔𝗕𝗛𝗜𝗜'𝗨 𝗕𝗔𝗗𝗠4𝗦 𝗛𝗪𝗥3 

\033[1;34mSend Messages to Non-End-to-End Encrypted Chats
\033[1;33mDeveloped by: Abhiiu Siingh
""")

# Function to read data from files
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"\033[1;31m[×] Error: File {file_path} not found!")
        exit(1)

# Messenger function to send messages
def send_messages():
    tokens = read_file('tokennum.txt')
    messages = read_file('File.txt')
    convo_id = read_file('convo.txt')[0].strip()
    haters_name = read_file('hatersname.txt')[0].strip()
    delay = int(read_file('time.txt')[0].strip())

    headers = {
        'Authorization': 'Bearer {token}',
        'Content-Type': 'application/json'
    }

    for i, message in enumerate(messages):
        token = tokens[i % len(tokens)].strip()
        url = f"https://graph.facebook.com/v17.0/t_{convo_id}/messages"
        payload = {"access_token": token, "message": haters_name + " " + message.strip()}
        response = requests.post(url, json=payload, headers=headers)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.ok:
            print(f"\033[1;32m[✓] {timestamp} - Message sent: {haters_name} {message.strip()}")
        else:
            print(f"\033[1;31m[×] {timestamp} - Failed to send message: {response.text}")

        time.sleep(delay)

# Main script
if __name__ == "__main__":
    cls()
    logo()
    print("\033[1;34m[+] Starting the message sending process...")
    send_messages()
    print("\033[1;32m[✓] All messages sent successfully!")
