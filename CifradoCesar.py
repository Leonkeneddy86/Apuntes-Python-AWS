# Creación de una función definida por el usuario
def getDoubleAlphabet(alphabet):
    return alphabet * 2

def getMessage():
    return input("Please enter a message to encrypt: ")

def getCipherKey():
    return input("Please enter a key (whole number from 1-25): ")

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    for currentCharacter in message.upper():
        position = alphabet.find(currentCharacter)
        if position != -1:
            newPosition = (position + int(cipherKey)) % len(alphabet)
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    return encryptMessage(message, -int(cipherKey), alphabet)

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()