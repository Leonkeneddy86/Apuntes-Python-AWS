import json

def readJsonFile(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Recuperar los datos JSON
data = readJsonFile('C:\\Users\\Administrador\\Desktop\\Apuntes Python\\insulin.json')

# Verificar si los datos no están vacíos
if data:
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculando el peso molecular de la insulina
    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}
    
    # Multiplicar el conteo por los pesos
    molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaCountInsulin)
    
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
else:
    print("Error. Exiting program")