import requests
from spamfile import get_spam_file
from copypasta import get_pasta
import time
import sys
import random
import string
import os
from pyfiglet import Figlet
from dotenv import load_dotenv
import threading
import pyinputplus as pyip
f = Figlet(font='slant')


load_dotenv()
discord_token =  os.getenv('discord_token')


def confirm():
    e = input("Press [ENTER] to continue")

def clear_screen():
    print("\x1b[2J\x1b[H",end="")


def spam_type():
    while True:
        clear_screen()
        type_s = input("What type of spam would you like to spam?\n[1] Random bs from r/copypasta\n[2] All that from a text file\n[3] A single message\n> ")
        if type_s == "1":
            response = pyip.inputInt('How many posts would you like to be spammed? ', min=1)
            copypasta_spam(response)
            break
                        
        elif type_s == "2":
            file_spam()
            break

        elif type_s == "3":
            msg = input("Enter what you want to spam: ")
            single_spam(msg)
            break

        else:
            print("Please enter a number from the stated options")
            confirm()

    mainmenu()
            





def single_spam(msg):
    runs = 0
    delay = 0.4
    effective_msgs = 0
    wasted_msgs = 0


    #spam from file code

    while True:
        try:

            payload = {"content":str(msg)}
            r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
            #print(r.status_code, type(r.status_code))
            if r.status_code == 200:
                effective_msgs += 1
            else:
                wasted_msgs += 1
            #send_thread_1 = threading.Thread(target=send_message, daemon=True)
            if runs == 0:
                print("Timer started")
                start_time = time.time()

            runs += 1
            time.sleep(delay)

        except KeyboardInterrupt:
            run_time = time.time() - start_time
            print("#==========")
            print("#STATISTICS")
            print(f"#Total messages sent: {wasted_msgs + effective_msgs}")
            print(f"#Server recieved {effective_msgs} messages")
            print(f"#Server ignored {wasted_msgs} messages")
            print(f"#Average msg/second: {round(effective_msgs/run_time, 2)}")
            print(f"#Recived messages to wasted messages ratio: 1:{round(wasted_msgs/effective_msgs,2)}")
            print(f"#Stopped after running for {round(run_time,2)} seconds")
            break

        

    confirm()



def copypasta_spam(amount):
    runs = 0
    delay = 0.4
    effective_msgs = 0
    wasted_msgs = 0


    #Copy pasta code
    try:
        copypasta = get_pasta(amount)

        for submission in copypasta:
            payload = {"content": submission}
            r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
            #print(r.status_code, type(r.status_code))
            if r.status_code == 200:
                effective_msgs += 1
            else:
                wasted_msgs += 1
            #send_thread_1 = threading.Thread(target=send_message, daemon=True)ferfe
            if runs == 0:
                print("Timer started")
                start_time = time.time()

            runs += 1
            time.sleep(delay)

            for chunk in copypasta[submission]:
                payload = {"content": chunk}
                r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
                #print(r.status_code, type(r.status_code))
                if r.status_code == 200:
                    effective_msgs += 1
                else:
                    wasted_msgs += 1
                #send_thread_1 = threading.Thread(target=send_message, daemon=True)
                if runs == 0:
                    print("Timer started")
                    start_time = time.time()

                runs += 1
                time.sleep(delay)

    except KeyboardInterrupt:
        pass

    run_time = time.time() - start_time
    print("#==========")
    print("#STATISTICS")
    print(f"#Total messages sent: {wasted_msgs + effective_msgs}")
    print(f"#Server recieved {effective_msgs} messages")
    print(f"#Server ignored {wasted_msgs} messages")
    print(f"#Average msg/second: {round(effective_msgs/run_time, 2)}")
    print(f"#Recived messages to wasted messages ratio: 1:{round(wasted_msgs/effective_msgs,2)}")
    print(f"#Stopped after running for {round(run_time,2)} seconds")
    confirm()



def file_spam(repeat=False):
    runs = 0
    delay = 0.4
    effective_msgs = 0
    wasted_msgs = 0


    #spam from file code

    while True:
        try:
            spamfile = get_spam_file()

            for chunk in spamfile:
                for subchunk in chunk:
                    payload = {"content":str(subchunk)}
                    r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
                    #print(r.status_code, type(r.status_code))
                    if r.status_code == 200:
                        effective_msgs += 1
                    else:
                        wasted_msgs += 1
                    #send_thread_1 = threading.Thread(target=send_message, daemon=True)
                    if runs == 0:
                        print("Timer started")
                        start_time = time.time()

                    runs += 1
                    time.sleep(delay)
            if True != repeat:
                break

        except KeyboardInterrupt:
            break


    run_time = time.time() - start_time
    print("#==========")
    print("#STATISTICS")
    print(f"#Total messages sent: {wasted_msgs + effective_msgs}")
    print(f"#Server recieved {effective_msgs} messages")
    print(f"#Server ignored {wasted_msgs} messages")
    print(f"#Average msg/second: {round(effective_msgs/run_time, 2)}")
    print(f"#Recived messages to wasted messages ratio: 1:{round(wasted_msgs/effective_msgs,2)}")
    print(f"#Stopped after running for {round(run_time,2)} seconds")
    confirm()




def config():
    print("Configs")
    confirm()


def mainmenu():
    while True:
        clear_screen()
        print(f.renderText("DiscordSpam")+"v1.0")
        print("#","="*10,"Main Menu", "="*10, "#")
        print("Yes")
        print("1. Spam someone or some channel")
        print("2. Configure the spammer")
        print("3. Quit")
        print("(Enter the number of the action you want to perform)")

        user_r = input(">> ")
        if user_r == "1":
            clear_screen()
            spam_type()
            

        elif user_r == "2":
            clear_screen()
            config()
            

        elif user_r == "3":
            clear_screen()
            print("Suspended")
            sys.exit()

        else:
            print("You must enter a number from the listed options")

        break



def rand_msg():
    return ''.join(random.choice(string.printable) for i in range(16))

#https://discord.com/api/v8/channels/814958806341255188/messages


headers = {"authorization": discord_token}

channel = "739533170260836384"
mainmenu()

#idk what this is
'''
def send_message():
    while True:
        
        payload = {"content": rand_msg()}
        r = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", data = payload, headers = headers)
        #print(r.status_code, type(r.status_code))
        if r.status_code == 200:
            effective_msgs += 1
        else:
            wasted_msgs += 1
'''


