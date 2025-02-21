# Un tipo de datos compuesto es cualquier tipo de datos que comprende tipos de datos primitivos. Si le gusta la comida, puede imaginar un tipo de datos compuesto como si fuera turducken, un plato que consiste en pavo relleno con pato que, a su vez, está relleno con pollo. En este laboratorio, creará un tipo de datos que consiste en una cadena que está en un diccionario y que, a su vez, se encuentra en una lista.

'''
utilizar tipos de datos numéricos
utilizar tipos de datos de texto (cadena o string)
utilizar el tipo de dato de diccionario
utilizar el tipo de dato de lista
utilizar un bucle for
utilizar la función print()
utilizar la instrucción if
utilizar la instrucción else
utilizar la instrucción import
'''

# Creación de datos de un inventario de vehículos

# para hacer este ejercicio se tiene que crear un archivo con este bloque de codigo en formato CSV.
'''
vin,make,model,year,range,topSpeed,zeroSixty,mileage
TMX20122,AnyCompany Motors, Coupe, 2012, 335, 155, 4.1, 50000
TM320163,AnyCompany Motors, Sedan, 2016, 240, 140, 5.2, 20000
TMX20121,AnyCompany Motors, SUV, 2012, 295, 155, 4.7, 100000
TMX20204,AnyCompany Motors, Truck, 2020, 300, 155, 3.5, 0
'''

# Crearemos un script en Python para almacenar un inventario de vehículos.

import csv # Bliblioteca que se requiere
import copy # Bliblioteca que se requiere

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
# usaremos el bucle for para recorrer las claves y los valores del diccionario
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
    myInventoryList = []
    
    # Leerá los datos del disco (disco duro) y realizará una copia en memoria (memoria de acceso aleatorio o RAM). En una computadora, se utiliza un disco duro para almacenar los datos a largo plazo, incluso cuando se apaga la alimentación. La sigla RAM hace referencia a la memoria temporal, que es más rápida, pero se borra cuando se apaga la alimentación de la computadora.Se le presentará la instrucción de sintaxis with open, que mantiene un archivo abierto mientras lee datos. Cerrará automáticamente el archivo CSV cuando termine de ejecutarse el código dentro del bloque with.También utilizará una nueva manera de formatear una cadena. En lugar de utilizar comillas dobles y .format para pasar las variables, puede utilizar comillas simples y escribir las variables entre los símbolos “{}”.Por último, csv.reader() es una función existente en la biblioteca csv, que ya ha importado con la instrucción import csv.Debería estar familiarizado con la mayor parte del resto del código.
    
    # Ahora, regrese al archivo en Python:
    
    ith open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    # Contiene un bucle for con una instrucción if-else, seguido de una instrucción print() al final.
    
    currentVehicle = copy.deepcopy(myVehicle)