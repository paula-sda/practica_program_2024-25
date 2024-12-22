from pymongo import MongoClient
from beans.localizador import Localizador

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Establece la conexión al servidor de MongoDB en localhost, puerto 27017

# Nombre de la base de datos y la colección
db_name = 'eda'  # Nombre de la base de datos que se usará
collection_name = 'localizaciones'  # Nombre de la colección donde se almacenan las localizaciones

def insertar_localizacion(localizador):
    
    #Inserta un objeto localizador en la base de datos.

    client[db_name][collection_name].insert_one(localizador)  # Inserta el documento en la colección especificada

def cargar_datos_bd():
    
    #Carga las localizaciones almacenadas en la base de datos en una lista y las convierte a objetos Localizador.
    # Obtiene todos los documentos de la colección
    db_pruebas = client[db_name][collection_name].find({})
    
    # Lista para almacenar las localizaciones cargadas de la base de datos
    lista_ubicaciones = []
    
    # Itera sobre cada documento recuperado de la base de datos
    for x in db_pruebas:
        # Extrae y convierte los valores de latitud y longitud
        latitud = x['latitud']
        longitud = x['longitud']
        lat = float(latitud)  # Convierte la latitud a tipo float
        long = float(longitud)  # Convierte la longitud a tipo float

        # Crea un objeto Localizador usando los valores obtenidos
        localizacion = Localizador(lat, long)
        
        # Añade el objeto Localizador a la lista
        lista_ubicaciones.append(localizacion)

    # Retorna la lista de objetos Localizador
    return lista_ubicaciones
