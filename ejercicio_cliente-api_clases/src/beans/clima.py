import requests


class Clima:

    # Atributos 
    latitud = None
    longitud = None
    temperatura = None
    velocidad_viento = None

    # Constructor de la clase que inicializa la latitud y longitud, y obtiene los datos climáticos
    def __init__(self, latitud, longitud):
        # Asignamos las coordenadas proporcionadas a los atributos de la instancia
        self.latitud = latitud
        self.longitud = longitud
        # Llamamos al método para obtener los datos climáticos
        self.__obtener_datos_climaticos()

    def __str__(self):
        # Formateamos y devolvemos la información climática como un string
        return (
            f"Clima:\n"
            f"  Latitud: {self.latitud}\n"
            f"  Longitud: {self.longitud}\n"
            f"  Temperatura: {self.temperatura}°C\n"
            f"  Velocidad del viento: {self.velocidad_viento} km/h")

    # Método privado para obtener los datos climáticos desde la API de Open-Meteo
    def __obtener_datos_climaticos(self):
        try:
            # URL de la API de Open-Meteo con los parámetros de latitud y longitud
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            
            # Hacemos la solicitud HTTP a la API usando la URL
            response = requests.get(url)
            # Convertimos la respuesta en formato JSON
            data = response.json()
            
            # Comprobamos si la respuesta fue exitosa y contiene los datos del clima
            if response.status_code == 200 and "current_weather" in data:
                # Si es exitoso, extraemos la temperatura y la velocidad del viento
                current_weather = data["current_weather"]
                self.temperatura = current_weather["temperature"]
                self.velocidad_viento = current_weather["windspeed"]
            else:
                # Si ocurre un error en la respuesta, asignamos valores desconocidos
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            # Si ocurre un error en la solicitud o en el procesamiento de los datos, lo capturamos
            print(f"Error al obtener los datos climáticos: {e}")
            # Asignamos valores de error en caso de excepciones
            self.temperatura, self.velocidad_viento = "Error", "Error"
        
        # Devolvemos los valores de temperatura y velocidad del viento obtenidos
        return self.temperatura, self.velocidad_viento