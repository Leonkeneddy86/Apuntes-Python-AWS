# Aprendemos a usar los siguientes valores creando una lista con diferentes tipos:
'''
utilizar tipos de datos numéricos
utilizar tipos de datos de texto (cadena o string)
utilizar el tipo de dato de lista
utilizar un bucle for
utilizar una función print()
'''

# Crear una lista de varios tipos

'''
Defina una lista con diferentes tipos, como el siguiente ejemplo
'''

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Utilice una instrucción de bucle for para recorrer la lista e imprimir el tipo de dato de cada elemento en ella:

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
    