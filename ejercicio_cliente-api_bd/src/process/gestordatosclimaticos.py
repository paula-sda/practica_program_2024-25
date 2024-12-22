# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
import json
from beans.localizador import Localizador
from basedeadatos import almacenamiento_bd


class GestorDeDatosClimaticos:

    def __init__(self):
        # Constructor de la clase que inicializa el gestor de datos climáticos
        print("Iniciando gestor de datos climaticos")
        # Imprime el número actual de ubicaciones almacenadas
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")

    def get_numero_ubicaciones(self):
        # Obtiene el número total de documentos en la base de datos usando el método `contar_elementos`
        return almacenamiento_bd.contar_elementos()

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        
        #Consulta todas las ubicaciones almacenadas en la base de datos y organiza los códigos postales por provincia o estado, mostrando el resultado en formato JSON.
        
        # Consulta todos los documentos de la base de datos
        ubicaciones = almacenamiento_bd.obtener_todas_las_ubicaciones()

        # Diccionario para agrupar códigos postales por provincia
        agrupacion_codigos_postales = {}

        for ubicacion in ubicaciones:
            # Intenta obtener la provincia o asigna "Sin provincia" si no está disponible
            provincia = ubicacion.get("provincia") or ubicacion.get("estado") or "Sin provincia"
            codigo_postal = ubicacion.get("codigo_postal")

            # Solo se agregan ubicaciones con códigos postales válidos
            if codigo_postal:
                if provincia in agrupacion_codigos_postales:
                    agrupacion_codigos_postales[provincia].append(codigo_postal)
                else:
                    agrupacion_codigos_postales[provincia] = [codigo_postal]

        # Muestra los resultados de forma legible en formato JSON
        if agrupacion_codigos_postales:
            print(json.dumps(agrupacion_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    def insertar_nueva_ubicacion(self, latitud, longitud):
        
        try:
            # Asegura que las coordenadas sean números válidos
            latitud = latitud  # Latitud en formato numérico
            longitud = longitud  # Longitud en formato numérico
        except ValueError:
            # Muestra un mensaje de error si los valores no son números válidos
            print("Error: La latitud y longitud deben ser números válidos.")
            return None

        # Comprueba si la ubicación ya está en la base de datos
        ubicacion_encontrada = almacenamiento_bd.buscar_por_latitud_longitud(latitud, longitud)

        if ubicacion_encontrada:
            # Si ya existe, muestra la ubicación encontrada
            print("================================================")
            print("Ubicación ya existe")
            print(f"Latitud: {ubicacion_encontrada.latitud}, Longitud: {ubicacion_encontrada.longitud}")
            print("================================================")
        else:
            # Si no existe, crea una nueva ubicación y la inserta en la base de datos
            nueva_ubicacion = Localizador(latitud, longitud)
            almacenamiento_bd.insertar_localizacion(nueva_ubicacion.to_dict())
            print("Ubicación agregada correctamente")

        # Devuelve la ubicación encontrada (si existía) o None
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self, codigo_postal):
        
        ubicaciones = almacenamiento_bd.buscar_por_codigo_postal(codigo_postal)
        if ubicaciones:  
            ubicacion_encontrada = ubicaciones[0]  # Obtiene la primera ubicación
        else:
            ubicacion_encontrada = None  # Si no hay resultados, retorna None

        return ubicacion_encontrada

    def buscar_por_provincia(self, provincia):
       
        ubicaciones = almacenamiento_bd.buscar_por_provincia(provincia)
        return ubicaciones

    def buscar_por_latitud_longitud(self, latitud, longitud):
        
        # Intentamos buscar la ubicación en la base de datos primero con números flotantes
        ubicacion = almacenamiento_bd.buscar_por_latitud_longitud(latitud, longitud)
    
        # Si no se encuentra, tratamos de buscar usando las coordenadas como cadenas
        if not ubicacion:
            # Intentamos con las coordenadas como cadenas
            latitud_str = str(latitud)
            longitud_str = str(longitud)
            ubicacion = almacenamiento_bd.buscar_por_latitud_longitud(latitud_str, longitud_str)
    
        if ubicacion:
            print(f"Ubicación encontrada: Latitud = {ubicacion.latitud}, Longitud = {ubicacion.longitud}")
        else:
            print("No se encontró ninguna ubicación con las coordenadas proporcionadas.")
    
        return ubicacion