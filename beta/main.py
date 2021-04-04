import requests
from spamfile import get_spam_file
from copypasta import *
import time
import sys
import random
import string
import os
from pyfiglet import Figlet
from dotenv import load_dotenv
import threading
import pyinputplus as pyip
from cfg import *
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
            remote = pyip.inputMenu(['remote', 'local'], prompt="From which source would you like to get the copy pasta from? (remote is reccomended for first runs)\n", numbered=True)         
            if remote != "local": 
                response = pyip.inputInt('How many posts would you like to be spammed? ', min=1)
                copypasta_spam(remote=remote, amount = response)
                break
            copypasta_spam(remote="local")
            break
                        
        elif type_s == "2":
            remote = pyip.inputMenu(['chronological', 'random'], prompt="In what order would you like the messages to be spammed in?\n", numbered=True)         
            if remote == "random":
                file_spam(rand=True, repeat=True)
            else:
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



def copypasta_spam(remote, amount = 10):
    clear_screen()
    runs = 0
    delay = 0.4
    effective_msgs = 0
    wasted_msgs = 0

    #Copy pasta code
    try:
        
        if remote == "local":
            copypasta = get_pasta(amount, remote=False)
        else:
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



def file_spam(repeat=True, rand=False):
    runs = 0
    delay = 0.4
    effective_msgs = 0
    wasted_msgs = 0


    #spam from file code

    while True:
        try:
            spamfile = get_spam_file()
            
            if not rand:
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

            else:
                chunk = random.choice(spamfile)
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




            if not repeat:
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
    remote = pyip.inputMenu(['Create and configure new config file', 'Edit an existing config file', 'Overwrite an existsing config file', 'Delete an existing config file'], prompt="What would you like to do?\n", numbered=True)
    if remote == "Create and configure new config file":
        new_cfg()


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

with open("channel.txt", "r") as fi:
    channel = fi.readlines()[0].strip("\n")
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


