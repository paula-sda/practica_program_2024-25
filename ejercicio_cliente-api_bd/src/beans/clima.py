import requests

# Clase para obtener el clima
class Clima:
    
    def __init__(self, latitud, longitud):
        
        #Inicializa una instancia de la clase Clima.

        self.latitud = latitud
        self.longitud = longitud
        self.temperatura = None
        self.velocidad_viento = None
        self.__obtener_datos_climaticos()

    def to_dict(self):
        
        #Convierte los datos del clima a un diccionario.
        return {
            "latitud": self.latitud,
            "longitud": self.longitud,
            "temperatura": self.temperatura,
        }
    
    def __str__(self):
        
        # Devuelve una representación en cadena del objeto Clima.

        return (
            f"Clima:\n"
            f"  Latitud: {self.latitud}\n"
            f"  Longitud: {self.longitud}\n"
            f"  Temperatura: {self.temperatura}°C\n"
            f"  Velocidad del viento: {self.velocidad_viento} km/h"
        )

    def __obtener_datos_climaticos(self):
        
        #Obtiene los datos climáticos actuales desde la API de Open-Meteo.
        try:
            # URL de la API de Open-Meteo
            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={self.latitud}&longitude={self.longitud}"
                f"&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            )
            # Hacer la solicitud a la API
            response = requests.get(url)
            data = response.json()

            # Verificar respuesta y extraer datos
            if response.status_code == 200 and "current_weather" in data:
                current_weather = data["current_weather"]
                self.temperatura = current_weather["temperature"]
                self.velocidad_viento = current_weather["windspeed"]
            else:
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            print(f"Error al obtener los datos climáticos: {e}")
            self.temperatura, self.velocidad_viento = "Error", "Error"
        return self.temperatura, self.velocidad_viento