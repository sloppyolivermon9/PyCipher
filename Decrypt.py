from math import ceil

def getMessageAndKey(Message, Key):
    Message = input("Enter the message you want to decrypt: ")
    Message = Message.split("=")
    Key = input("Enter the key you would like to decrypt it with: ")
    return Message, Key

def createLongKey(Message, Key):
    tempKey = Key
    for i in range(ceil(len(Message) / len(Key))):
        Key += tempKey
    return Key

def encrypt(Message, Key):
    tempMessage = ""
    for i in range(len(Message)):
        currentMLetter = int(Message[i], 16)
        currentKLetter = ord(Key[i])

        currentMLetter -= currentKLetter + 45
        tempMessage += chr(currentMLetter)
    return tempMessage

def main():
    Message, Key = [], ""
    Message, Key = getMessageAndKey(Message, Key)
    Key = createLongKey(Message, Key)
    Message = encrypt(Message, Key)
    print(Message)

main()
