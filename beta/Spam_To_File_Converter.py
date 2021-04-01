import pyinputplus as pyip

def confirm():
    e = input("Press [ENTER] to continue")


def clear_screen():
    print("\x1b[2J\x1b[H",end="")


def ask_for_spam(sep="+"):
    to_spam = []
    count = 0
    while True:
        count+= 1
        spam = input(f"Enter message number {count} that you would like to be added to your file. To save and quit, simply press enter without writing anything\n> ") 
        if spam == "":
            break
        
        to_spam.append(spam)
        clear_screen()

    if len(to_spam) == 0:
        return ""

    spam_to_text = sep.join(msg for msg in to_spam)
    return spam_to_text


sep = input("Input a character or a set of characters that are not used in your text. This will be used to separate your messages in the code (default=+): ")
if sep == "":
    sep = "+"

todo = pyip.inputInt("What would you like to do?\n[1] Append more spam to the spamfile\n[2] Overwrite the spam in the file with new spam\n> ", min=1, max=2)

if todo == 1:
    to_append = sep + ask_for_spam(sep)
    with open("spamfile.txt", "a") as f:
        f.write(to_append)
    clear_screen()
    print(f"Succesfully appended {len(to_append.split(sep))} more items to the spamfile")

else:
    to_append = ask_for_spam(sep)
    with open("spamfile.txt", "w") as f:
        f.write(to_append)
    clear_screen()
    print(f"Succesfully wrote {len(to_append.split(sep))}º items to the spamfile")

