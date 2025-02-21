# Creación de una función definida por el usuario
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Nota: Las partes obligatorias de la instrucción de una función son la palabra clave def, un nombre y los dos puntos (:). Además, en Python, no es necesario declarar las variables, y sus tipos de datos se deducen a partir de la instrucción de asignación.
'''
Para comprender lo que hace la función, tome una entrada de muestra, como alphabet="ABC". La cadena devuelta para esta entrada sería "ABC" + "ABC" = "ABCABC". El signo más (+) concatena los textos en uno solo.
'''
# Cifrado de un mensaje
# La siguiente función que definirá solicitará al usuario un mensaje para cifrar. Utilizará la función integrada denominada input().

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Obtención de una clave de cifrado

'''
La clave de cifrado es la distancia con la que desplazará las letras. Mediante el uso de dos alfabetos, puede tener una clave de cifrado que sea cualquier número entero entre 1 y 25. No considere la clave en el índice 26 porque esa clave lo dirigirá de nuevo al mensaje original.
'''

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Hasta ahora, las funciones han sido cortas y sencillas. Este suele ser el caso cuando mantiene una tarea específica dentro de una función. La función encryptMessage será un poco más larga.

# debe diseñar el algoritmo de cifrado de la siguiente manera:

'''
Tome tres argumentos: el mensaje, la clave de cifrado y el alfabeto.

Inicie las variables.

Utilice un bucle for para recorrer cada letra del mensaje.

Para una letra específica, busque su posición.

Para una letra específica, determine la nueva posición de acuerdo con la clave de cifrado.

Si la letra actual está en el alfabeto, agregue la nueva letra al mensaje cifrado.

Si la letra actual no está en el alfabeto, añada la letra actual.

Devuelva el mensaje cifrado tras agotar todas las letras del mensaje.
'''

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Las funciones son útiles, ya que pueden reutilizarse. Escribirá una función decryptMessage() al reutilizar la función encryptMessage(). Para este cifrado sencillo, puede deshacer el cifrado si mueve cada letra hacia atrás. De este modo, en lugar de agregar la clave de cifrado, la eliminará. Para evitar reescribir la mayor parte de la lógica, pasará una clave de cifrado negativa.

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Creación de una función principal

'''
Ha creado una colección de funciones definidas por el usuario que lo ayudarán a escribir un programa de cifrado César. Desde luego, la lógica principal del programa también estará incluida en una función.
'''


# diseñe la lógica:

'''
Defina una variable de cadena para que contenga el alfabeto inglés.

Para poder desplazar las letras, duplique la cadena del alfabeto.

Obtenga del usuario un mensaje para cifrar.

Obtenga del usuario una clave de cifrado.

Cifre el mensaje.

Descifre el mensaje.
'''

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
    # Para ayudarlo con la depuración y la comprensión del programa, se agregaron las instrucciones print(), pero no son estrictamente necesarias para que el programa opere de forma correcta.
    
    # No ocurre nada. ¿Por qué? Recuerde que una función es una sección de un programa que realiza una tarea específica. Todavía no llamado la función.
    
    runCaesarCipherProgram()
    
    
