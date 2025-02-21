import json 
import jsonFileHadler

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

# Recupere los datos JSON y almacénelos en una variable de datos.
data = jsonFileHadler.readJsonFile('files/insulin.json')

# Compruebe si los datos devueltos no están vacíos y obtenga los datos de insulina.
if data:
    bInsulin = data['molecules'].get('bInsulin', '')
    aInsulin = data['molecules'].get('aInsulin', '')
    
    if bInsulin and aInsulin:
        insulin = bInsulin + aInsulin
        molecularWeightInsulinActual = data.get('molecularWeightInsulinActual', 0)
        print('bInsulin: ' + bInsulin)
        print('aInsulin: ' + aInsulin)
        print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

        # Calculating the molecular weight of insulin  
        # Getting a list of the amino acid (AA) weights  
        aaWeights = data.get('weights', {})
        # Count the number of each amino acids  
        aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}  
        # Multiply the count by the weights  
        molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights.get(x, 0) for x in aaCountInsulin)  
        print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
        print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
    else:
        print("Error: Insulin data not found in JSON.")
else:
    print("Error. Exiting program")