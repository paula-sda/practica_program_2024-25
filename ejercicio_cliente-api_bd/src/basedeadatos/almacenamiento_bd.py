from pymongo import MongoClient
from beans.localizador import Localizador

# Establece la conexión con MongoDB en la dirección predeterminada
client = MongoClient('mongodb://localhost:27017/')

# Define el nombre de la base de datos y la colección a utilizar
db_name = 'eda'
collection_name = 'localizaciones'

# Función para buscar ubicaciones por provincia
def buscar_por_provincia(provincia):
    
    #Busca ubicaciones en la base de datos por provincia o estado.

    print("Buscando los datos de la base de datos")
    
    # Intentar buscar por provincia
    db_pruebas = client[db_name][collection_name].find({"provincia": provincia})
    lista_ubicaciones = []

    for x in db_pruebas:
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)
    
    # Si no se encuentran ubicaciones por provincia, buscar por estado
    if not lista_ubicaciones:
        db_pruebas = client[db_name][collection_name].find({"estado": provincia})
        for x in db_pruebas:
            latitud = x['latitud']
            longitud = x['longitud']
            localizacion = Localizador(latitud, longitud)
            lista_ubicaciones.append(localizacion)

    # Si no hay resultados, mostrar un mensaje
    if not lista_ubicaciones:
        print(f"No se encontraron ubicaciones para la provincia o estado: {provincia}")
    
    return lista_ubicaciones

# Función para buscar ubicaciones por código postal
def buscar_por_codigo_postal(codigo_postal):

    print("Mostramos los datos filtrados por código postal")
    db_pruebas = client[db_name][collection_name].find({"codigo_postal": codigo_postal})
    lista_ubicaciones = []

    for x in db_pruebas:
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)
    return lista_ubicaciones

# Función para buscar una ubicación específica por latitud y longitud
def buscar_por_latitud_longitud(latitud, longitud):
    
    #Busca una ubicación en la base de datos utilizando latitud y longitud.

    resultado = client[db_name][collection_name].find_one({"latitud": str(latitud), "longitud": str(longitud)})
    if resultado:
        return Localizador(resultado['latitud'], resultado['longitud'])
    return None

# Función para insertar una nueva localización en la base de datos
def insertar_localizacion(localizador):
    
    #Inserta un nuevo registro de localización en la base de datos.
    client[db_name][collection_name].insert_one(localizador)

# Función para cargar todos los datos almacenados en la base de datos
def cargar_datos_bd():
    
    #Carga y muestra todos los datos almacenados en la base de datos.    
    print("Mostramos los datos de la base de datos paula-eda")
    db_pruebas = client[db_name][collection_name].find({})
    
    lista_ubicaciones = []
    for x in db_pruebas:
        latitud = x['latitud']
        longitud = x['longitud']
        localizacion = Localizador(latitud, longitud)
        lista_ubicaciones.append(localizacion)

    return lista_ubicaciones

# Función para obtener todas las ubicaciones en forma de lista de documentos
def obtener_todas_las_ubicaciones():
    """
    Recupera todos los documentos almacenados en la colección.

    Retorna:
        list: Una lista de documentos JSON representando todas las ubicaciones.
    """
    return list(client[db_name][collection_name].find({}))

# Función para contar la cantidad de documentos en la colección
def contar_elementos():
    """
    Cuenta la cantidad de documentos almacenados en la colección.

    Retorna:
        int: El número total de documentos en la colección.
    """
    coleccion = client[db_name][collection_name]
    total = coleccion.count_documents({})
    return total