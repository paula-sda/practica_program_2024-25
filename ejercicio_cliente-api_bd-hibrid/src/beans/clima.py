import requests

# Clase para obtener el clima (temperatura y velocidad del viento) de Open-Meteo
class Clima:

    # Atributos de clase 
    latitud = None
    longitud = None
    temperatura = None
    velocidad_viento = None

    # Constructor que inicializa la latitud y longitud, y obtiene los datos climáticos
    def __init__(self, latitud, longitud):
        self.latitud = latitud  # Asigna el valor de latitud
        self.longitud = longitud  # Asigna el valor de longitud
        self.__obtener_datos_climaticos()  # Llama al método privado para obtener los datos climáticos

    # Método para convertir los datos a un diccionario
    def to_dict(self):
        return {
            "latitud": self.latitud,  # Incluye la latitud
            "longitud": self.longitud,  # Incluye la longitud
            "temperatura": self.temperatura,  # Incluye la temperatura
        }
    
    # Método para representar la instancia de la clase como una cadena de texto
    def __str__(self):
        return (
            f"Clima:\n"
            f"  Latitud: {self.latitud}\n"  # Muestra la latitud
            f"  Longitud: {self.longitud}\n"  # Muestra la longitud
            f"  Temperatura: {self.temperatura}°C\n"  # Muestra la temperatura
            f"  Velocidad del viento: {self.velocidad_viento} km/h"  # Muestra la velocidad del viento
        )

    # Método privado para obtener los datos climáticos desde la API de Open-Meteo
    def __obtener_datos_climaticos(self):
        try:
            # URL de la API con los parámetros de latitud y longitud
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            # Realiza la solicitud HTTP a la API
            response = requests.get(url)
            data = response.json()  # Convierte la respuesta en formato JSON
            if response.status_code == 200 and "current_weather" in data:  # Verifica que la solicitud fue exitosa
                current_weather = data["current_weather"]  # Extrae los datos de clima actuales
                self.temperatura = current_weather["temperature"]  # Asigna la temperatura
                self.velocidad_viento = current_weather["windspeed"]  # Asigna la velocidad del viento
            else:
                # En caso de error, asigna valores desconocidos
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            # Maneja cualquier excepción en la solicitud a la API
            print(f"Error al obtener los datos climáticos: {e}")
            self.temperatura, self.velocidad_viento = "Error", "Error"
        return self.temperatura, self.velocidad_viento  # Devuelve la temperatura y la velocidad del viento