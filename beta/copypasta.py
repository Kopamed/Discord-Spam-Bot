import praw
import json

r = praw.Reddit('bot1')
 
subreddit = r.subreddit("copypasta")
 	
def get_pasta(amount=10, save=True, remote=True):
    copypastas = {}
    if remote:
        submission_count = 0
        for submission in subreddit.hot(limit=amount):
            title = submission.title
            text = submission.selftext
            messages = []

            if len(text) > 2000:
                messages_needed = int(len(text)/2000)+1
                for message in range(0,messages_needed-1):
                    messages.append(text[message*2000:(message+1)*2000])
                messages.append(text[messages_needed-1*2000:])

            else:
                messages.append(text)
            
            submission_count += 1
            print(f"Indexed submission number {submission_count}")
            copypastas[title] = messages
        
        if save:
            try:
                with open("copypasta.json", "r") as f:
                        prev_json = json.loads(f.read())

                new_pasta = copypastas | prev_json

                with open("copypasta.json", "w") as f:
                    json.dump(new_pasta, f, indent=4)
            
            except json.decoder.JSONDecodeError:
                print("First run, huh? Enjoy the spammer!")
                with open("copypasta.json", "w") as f:
                    json.dump(copypastas, f, indent=4)
        

    else:
        with open("copypasta.json", "r") as f:
            try:
                copypastas = json.loads(f.read())

            except json.decoder.JSONDecodeError:
                copypastas = {"i am big idiot":["i need to fetch pasta first from remote"], "before":["fucking spamming it"], "ich bin": ["un poco loco"]}




    return copypastas


if __name__ == "__main__":
    print(get_pasta(100))
