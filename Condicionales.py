# Siguientes instrucciones que  se pueden utilizar en Python
'''
utilizar la instrucción if
utilizar la instrucción else
utilizar la instrucción elif
'''

# Trabajo con la instrucción if

# deberá editar un script de Python para hacer envíos de paquetes.

userReply = input("Do you need to ship a package? (Enter yes or no) ")
'''
Utilice la instrucción if para mostrar una respuesta.
Las instrucciones de una declaración if deben mantener una sangría de un tabulador, debajo de la instrucción if. En otros lenguajes de programación, a menudo se utilizan corchetes ({}) para indicar el inicio y el final de un bloque lógico, pero Python utiliza espaciado:
'''

if userReply == "yes":
    print("We can help you ship that package!")
    
    #Nota: El símbolo == es un operador de comparación. Significa es igual a.
    
    #  Trabajo con la instrucción else
    
    '''
    Para mejorar el servicio de atención al cliente, sería una buena idea proporcionar una respuesta, incluso cuando el usuario no desee enviar un paquete. En este ejercicio, mejorará el script de Python mediante la instrucción else:
    '''
    
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    # Trabajar con la declaración elif
    
    '''
    En este ejercicio, mejorará el script de Python ofreciendo al usuario servicios adicionales. Cuando tenga varias condiciones, puede utilizar la elifinstrucción , que es la abreviatura de else-if .
    '''
    
    # Nota: La elif declaración siempre viene después de una ifdeclaración y antes de la elsedeclaración.
    
    userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
