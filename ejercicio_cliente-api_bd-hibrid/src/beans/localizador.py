from geopy.geocoders import Nominatim

from beans.clima import Clima

# Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
class Localizador:

    # Atributos de clase 
    latitud = None
    longitud = None
    direccion = None
    ciudad = None
    barrio = None
    provincia = None
    estado = None
    pais = None
    codigo_postal = None
    clima = None

    # Constructor que inicializa latitud y longitud, obtiene la dirección y crea un objeto de la clase Clima
    def __init__(self, latitud, longitud):
        self.latitud = latitud  # Asigna el valor de latitud
        self.longitud = longitud  # Asigna el valor de longitud
        self.__obtener_direccion()  # Llama al método privado para obtener la dirección
        self.clima = Clima(self.latitud, self.longitud)  # Crea una instancia de la clase Clima

    # Método para convertir los datos en un diccionario
    def to_dict(self):
        return {
            "latitud": self.latitud,  # Incluye la latitud
            "longitud": self.longitud,  # Incluye la longitud
            "direccion": self.direccion,  # Incluye la dirección
            "ciudad": self.ciudad,  # Incluye la ciudad
            "barrio": self.barrio,  # Incluye el barrio
            "provincia": self.provincia,  # Incluye la provincia
            "estado": self.estado,  # Incluye el estado
            "codigo_postal": self.codigo_postal,  # Incluye el código postal
            "clima": self.clima.to_dict()  # Incluye los datos del clima (convertidos a diccionario)
        }

    # Método privado para obtener la dirección a partir de la latitud y longitud usando Nominatim
    def __obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")  # Inicializa el geolocalizador
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")  # Realiza la búsqueda de la dirección
            # Asigna la dirección si se encuentra, de lo contrario asigna un mensaje de error
            self.direccion = location.address if location else "Dirección no encontrada"
            # Rellenamos los datos adicionales (barrio, ciudad, provincia, estado, país y código postal)
            try:
                self.barrio = location.raw['address']['suburb'] if 'suburb' in location.raw['address'] else None
                self.ciudad = location.raw['address']['city'] if 'city' in location.raw['address'] else None
                self.provincia = location.raw['address']['province'] if 'province' in location.raw['address'] else None
                self.estado = location.raw['address']['state'] if 'state' in location.raw['address'] else None
                self.pais = location.raw['address']['country'] if 'country' in location.raw['address'] else None
                self.codigo_postal = location.raw['address']['postcode'] if 'postcode' in location.raw['address'] else None
            except:
                pass  # Si hay un error al acceder a los datos adicionales, se ignora
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"  # En caso de error, se asigna un mensaje de error

    # Método para verificar si las coordenadas coinciden con las del localizador
    def check_lat_lng(self, latitud, longitud):
        if self.latitud == latitud:  # Verifica si la latitud coincide
            if self.longitud == longitud:  # Verifica si la longitud coincide
                return True
            else:
                return False
        else:
            return False  # Si la latitud no coincide, devuelve False

    # Método para mostrar la información completa del localizador y el clima
    def mostrar_informacion(self):
        info_localizador = (
            f"Localizador:\n"
            f"  Latitud: {self.latitud}\n"  # Muestra la latitud
            f"  Longitud: {self.longitud}\n"  # Muestra la longitud
            f"  Dirección: {self.direccion}\n"  # Muestra la dirección
            f"  Ciudad: {self.ciudad}\n"  # Muestra la ciudad
            f"  Barrio: {self.barrio}\n"  # Muestra el barrio
            f"  Provincia: {self.provincia}\n"  # Muestra la provincia
            f"  Estado: {self.estado}\n"  # Muestra el estado
            f"  País: {self.pais}\n"  # Muestra el país
            f"  Código postal: {self.codigo_postal}"  # Muestra el código postal
        )
        
        # Muestra la información del localizador y luego el clima
        print(info_localizador)
        print(self.clima)  # Muestra la información climática