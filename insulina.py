# Importar la biblioteca necesaria
import re

# Ruta del archivo de insulina
file_path = r'C:\Users\Administrador\Desktop\Apuntes Python\preproinsulin-seq.txt'

# Función para limpiar la secuencia de insulina
def limpiar_secuencia(secuencia):
    # Eliminar caracteres no alfabéticos
    return re.sub(r'[^a-zA-Z]', '', secuencia)

# Leer el archivo
with open(file_path, 'r') as file:
    # Leer todas las líneas del archivo
    lineas = file.readlines()

# Procesar cada línea
for linea in lineas:
    # Limpiar la secuencia
    secuencia_limpia = limpiar_secuencia(linea)
    # Imprimir la secuencia limpia
    print(secuencia_limpia)