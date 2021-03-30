def get_spam_file(file_name="spamfile.txt"):
    spam_messages = []
    with open(file_name, "r") as f:
        raw_spam_messages = f.read().split("+")

    for message in raw_spam_messages:
        message_chunk = []
        if len(message) > 2000:
            messages_needed = int(len(message)/2000)+1
            for message_part in range(messages_needed-1):
                message_chunk.append(message[message_part*2000:(message_part+1)*2000])
            message_chunk.append(message[messages_needed-1*2000:])

        else:
            message_chunk.append(message)
        spam_messages.append(message_chunk)

    return spam_messages
    

if __name__ == "__main__":
    get_spam_file()
