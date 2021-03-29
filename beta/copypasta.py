import praw

r = praw.Reddit('bot1')
 
subreddit = r.subreddit("copypasta")
 	
def get_pasta(amount=10):
    copypastas = {}
    for submission in subreddit.hot(limit=amount):
        title = submission.title
        text = submission.selftext
        messages = []

        if len(text) > 2000:
            print("POG")
            messages_needed = int(len(text)/2000)
            for message in range(messages_needed-1):
                messages.append(text[message*2000:(message+1)*2000])
            messages.append(text[messages_needed:])

        else:
            messages.append(text)

        copypastas[title] = messages

    return copypastas


if __name__ == "__main__":
    print(get_pasta(100))
