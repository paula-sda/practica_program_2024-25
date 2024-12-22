# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from beans.localizador import Localizador
from basedeadatos import almacenamiento_bd


class GestorDeDatosClimaticos:

    # Lista para almacenar las ubicaciones cargadas en memoria
    ubicaciones = []

    def __init__(self):
        #Constructor de la clase que inicializa el gestor de datos climáticos.
        #Carga las ubicaciones desde la base de datos al iniciar.
        
        print("Iniciando gestor de datos climáticos")
        self.ubicaciones = almacenamiento_bd.cargar_datos_bd()  # Carga las ubicaciones desde la base de datos
        print(f"Número de ubicaciones actuales: {self.get_numero_ubicaciones()}")

    def get_numero_ubicaciones(self):
        
        #Devuelve el número de ubicaciones almacenadas en memoria.
        
        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        
        #Muestra un diccionario de provincias con los códigos postales correspondientes.
    
        provincias_codigos_postales = {}

        # Itera sobre las ubicaciones almacenadas
        for ubicacion in self.ubicaciones:
            # Usa provincia o estado como respaldo si provincia está vacía
            provincia = ubicacion.provincia or ubicacion.estado

            # Si la provincia ya está en el diccionario, añade el código postal si no está duplicado
            if provincia in provincias_codigos_postales:
                if ubicacion.codigo_postal not in provincias_codigos_postales[provincia]:
                    provincias_codigos_postales[provincia].append(ubicacion.codigo_postal)
            else:
                # Si la provincia no está en el diccionario, la añade con el código postal
                provincias_codigos_postales[provincia] = [ubicacion.codigo_postal]

        # Imprime el diccionario formateado como JSON o un mensaje si no hay datos
        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    def insertar_nueva_ubicacion(self, latitud, longitud):
        
        #Inserta una nueva ubicación si no existe ya en la lista de ubicaciones.
        #Primero verifica si la ubicación ya está en la lista. Si no, la añade.
        ubicacion_encontrada = False

        # Busca si la ubicación ya existe
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicacion.mostrar_informacion())
                print("================================================")
                break

        # Si no se encontró, crea una nueva ubicación y la guarda
        if not ubicacion_encontrada:
            nueva_ubicacion = Localizador(latitud, longitud)  # Crea una nueva ubicación
            almacenamiento_bd.insertar_localizacion(nueva_ubicacion.to_dict())  # La guarda en la base de datos
            self.ubicaciones.append(nueva_ubicacion)  # La añade a la lista en memoria
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")

        return ubicacion_encontrada

    def buscar_por_codigo_postal(self, codigo_postal):

        #Busca una ubicación por su código postal.
        
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                return ubicacion
        return None

    def buscar_por_provincia(self, provincia):
        
        #Busca todas las ubicaciones que pertenecen a una provincia.
        
        lista_ubicaciones = []

        # Busca por provincia
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)

        # Si no se encuentran por provincia, busca por estado
        if not lista_ubicaciones:
            for ubicacion in self.ubicaciones:
                if ubicacion.estado == provincia:
                    lista_ubicaciones.append(ubicacion)

        # Si no se encuentra nada, muestra un mensaje
        if not lista_ubicaciones:
            print(f"No se encontraron ubicaciones en '{provincia}'.")

        return lista_ubicaciones

    def buscar_por_latitud_longitud(self, latitud, longitud):
        #Busca una ubicación por su latitud y longitud. (Recorriendo la lista de ubicaciones)
    
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                return ubicacion
        return None
