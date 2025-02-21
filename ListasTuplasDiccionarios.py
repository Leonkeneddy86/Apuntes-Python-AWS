# En Python, los tipos de datos numéricos y de cadena se suelen utilizar en grupos denominados colecciones. La lista, la tupla y el diccionario son tres de estas colecciones compatibles con Python.

'''
utilizar el tipo de dato de lista
utilizar el tipo de datos de “tupla” (tuple)
utilizar el tipo de dato de diccionario___
'''

# En esta actividad, editará un script en Python para almacenar una colección de nombres de frutas o una lista.

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
# Para acceder a la cadena apple, escriba el siguiente código

print(myFruitList[0])

# Para acceder a la cadena banana, escriba el siguiente código

print(myFruitList[1])

# Para acceder a la cadena cherry, escriba el siguiente código

print(myFruitList[2])

# Los valores de una lista se pueden cambiar. En esta actividad, cambiará cherry por orange.

myFruitList[2] = "orange"
print(myFruitList)

# Una tupla es similar a una lista, pero no se puede cambiar. Un tipo de dato que no se puede cambiar después de su creación se conoce como inmutable. Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([])

myFruitTuple = ("apple", "banana", "pineapple")
print(myFruitTuple)
print(type(myFruitTuple))

# Para acceder a la cadena apple, escriba el siguiente código

print(myFruitTuple[0])

# Para acceder a la cadena banana, escriba el siguiente código

print(myFruitTuple[1])

# Para acceder a la cadena pineapple, escriba el siguiente código

print(myFruitTuple[2])

# Presentar el tipo de dato de diccionario

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Acceso al diccionario por nombre
'''
En esta actividad,
en lugar de utilizar números,
recurrirá al nombre de las personas para acceder a su fruta favorita.
'''
# Para acceder a la fruta favorita de Akua, escriba el siguiente código
print(myFavoriteFruitDictionary["Akua"])
# Para acceder a la fruta favorita de Saanvi, escriba el siguiente código
print(myFavoriteFruitDictionary["Saanvi"])
# Para acceder a la fruta favorita de Paulo, escriba el siguiente código
print(myFavoriteFruitDictionary["Paulo"])

