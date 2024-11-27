from math import ceil

def getMessageAndKey(Message, Key):
    Message = input("Enter the message you want to encrypt: ")
    Key = input("Enter the key you would like to encrypt it with: ")
    return Message, Key

def createLongKey(Message, Key):
    tempKey = Key
    for i in range(ceil(len(Message) / len(Key))):
        Key += tempKey
    return Key

def encrypt(Message, Key):
    tempMessage = ""
    for i in range(len(Message)):
        currentMLetter = ord(Message[i])
        currentKLetter = ord(Key[i])

        currentMLetter += currentKLetter + 45
        currentMLetter = hex(currentMLetter)
        tempMessage += currentMLetter[currentMLetter.index("x")+1:len(currentMLetter)] + "="
    return tempMessage[0:len(tempMessage)-1]

def main():
    Message, Key = "", ""
    Message, Key = getMessageAndKey(Message, Key)
    Key = createLongKey(Message, Key)
    Message = encrypt(Message, Key)
    print(Message)

main()
