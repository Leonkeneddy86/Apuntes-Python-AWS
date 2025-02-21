# Trabajar con bucles
import random
'''
Utilice un while bucle
Utilice un for bucle
'''

# Trabajar con un bucle while
'''
Un whilebucle hace que una sección de código se repita hasta que se cumpla una determinada condición. En este ejercicio, creará un script de Python que le pide al usuario que adivine correctamente un número.
'''

# Impresión de las reglas del juego

# Utilice la print()función para informar al usuario sobre su juego:

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
# Realice un seguimiento si el usuario adivinó su número creando una variable llamada isGuessRight :
isGuessRight = False
# Para manejar la lógica del juego, crea un whilebucle:

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        print("Count to 10!")
        # Nota: El whilebucle repetirá el código dentro del bucle hasta que se adivine el número correctamente, lo que se representa mediante la condición isGuessRight != Trueen el código. Además, Python utiliza la sangría para determinar los bloques lógicos o qué declaraciones se consideran parte del whilebucle. Puede sangrar una línea colocando el cursor junto a una declaración y presionando TAB.

# Nota: Python utiliza sangría para determinar que la printdeclaración está dentro de la fordeclaración del bucle.):

for x in range (0, 11):
    print(x)
    
# Aquí hay una explicación de lo que sucedió en esas dos líneas. La fordeclaración usa las for … inpalabras clave para indicarle a la computadora que recorra la lista. La range()función genera una lista. La range()función toma un número inicial y un número final, pero el número final no es inclusivo. Por lo tanto, pasas 11para que la función deje de contar en 10. La letra x actúa como una variable. Cada vez que se pasa por el bucle, la variable x se asigna a la siguiente variable en el bucle y se imprime en la pantalla.    


