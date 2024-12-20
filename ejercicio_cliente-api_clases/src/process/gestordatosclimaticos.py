
# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from beans.localizador import Localizador  # Se importa la clase Localizador para manejar ubicaciones

class GestorDeDatosClimaticos:
    # Atributo de clase que almacena todas las ubicaciones (lista de ubicaciones)
    ubicaciones = []

    def __init__(self): #Inicializa el gestor de datos y muestra el número de ubicaciones actuales.

        print("Iniciando gestor de datos climaticos")
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")

    def get_numero_ubicaciones(self): #Devuelve el número de ubicaciones almacenadas en el gestor.

        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        
        #Muestra los códigos postales y las provincias almacenadas.
        #Si una provincia está vacía, usa el valor de la comunidad autónoma (estado) como respaldo.

        provincias_codigos_postales = {}
        # Recorre todas las ubicaciones y organiza los códigos postales por provincia
        for ubicacion in self.ubicaciones:
            # Si la provincia está vacía, se usa el estado como provincia
            provincia = ubicacion.provincia or ubicacion.estado

            # Si la provincia ya está en el diccionario, agrega el código postal
            if provincia in provincias_codigos_postales:
                if ubicacion.codigo_postal not in provincias_codigos_postales[provincia]:
                    provincias_codigos_postales[provincia].append(ubicacion.codigo_postal)
            else:
                # Si la provincia no está en el diccionario, se la agrega con el código postal
                provincias_codigos_postales[provincia] = [ubicacion.codigo_postal]

        # Muestra los resultados en formato JSON (si hay datos) o un mensaje de que no hay ubicaciones
        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    def insertar_nueva_ubicacion(self, latitud, longitud):
    
        # Intenta insertar una nueva ubicación con la latitud y longitud proporcionadas.
        # Si la ubicación ya existe (mismo latitud y longitud), no se agrega nuevamente.
    
        ubicacion_encontrada = False
        # Recorre las ubicaciones existentes para verificar si ya hay una ubicación con las mismas coordenadas
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicacion.mostrar_informacion())  # Muestra información de la ubicación existente
                print("================================================")
                break
        
        # Si no se encuentra la ubicación, se agrega una nueva
        if not ubicacion_encontrada:
            self.ubicaciones.append(Localizador(latitud, longitud))  # Se crea un nuevo objeto Localizador
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")
        
        return ubicacion_encontrada  # Retorna si se encontró o no la ubicación

    def buscar_por_codigo_postal(self, codigo_postal):

        #Busca una ubicación por su código postal y la devuelve si la encuentra.
        #Si no la encuentra, devuelve None.
        
        ubicacion_encontrada = None
        # Recorre todas las ubicaciones para encontrar la que tenga el código postal dado
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                ubicacion_encontrada = ubicacion
                break
        return ubicacion_encontrada  # Retorna la ubicación encontrada o None

    def buscar_por_provincia(self, provincia):
        
        #Busca todas las ubicaciones que pertenezcan a la provincia dada.
        #Si no se encuentra ninguna, busca por estado (comunidad autónoma).
        #Si tampoco se encuentra por estado, muestra un mensaje indicando que no se encontró ninguna ubicación.
        #Devuelve una lista con las ubicaciones encontradas.

        lista_ubicaciones = []

        # Primero, busca por provincia
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
    
        # Si no se encuentra ninguna, busca por estado (comunidad autónoma)
        if not lista_ubicaciones:
            for ubicacion in self.ubicaciones:
                if ubicacion.estado == provincia:  # Aquí asumimos que si no se encuentra por provincia, se busca por estado
                    lista_ubicaciones.append(ubicacion)

        # Si después de buscar por ambos no se encuentran ubicaciones, muestra un mensaje de no encontrado
        if not lista_ubicaciones:
            print(f"No se encontraron ubicaciones en '{provincia}'.")
    
        return lista_ubicaciones  # Retorna la lista de ubicaciones encontradas (vacía si no se encontró ninguna)

    def buscar_por_latitud_longitud(self, latitud, longitud):
        
        #Busca una ubicación usando la latitud y longitud proporcionadas.
        #Si la ubicación es encontrada, la retorna; si no, retorna None.

        for ubicacion in self.ubicaciones:
            # Verifica si la latitud y longitud coinciden con alguna ubicación almacenada
            if ubicacion.check_lat_lng(latitud, longitud):
                return ubicacion
