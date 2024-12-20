# Se importa Nominatim para geolocalización y la clase Clima para obtener datos climáticos.
from geopy.geocoders import Nominatim
from beans.clima import Clima

# Clase Localizador
class Localizador:
    # Atributos de la clase  
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

    # Constructor que recibe latitud y longitud, y obtiene la dirección y clima.
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.__obtener_direccion()  # Llama al método privado para obtener la dirección de la ubicación.
        self.clima = Clima(self.latitud, self.longitud)  # Inicializa un objeto de la clase Clima.

    # Método para convertir los datos del localizador en un diccionario.
    def to_dict(self):
        return {
            "latitud": self.latitud,
            "longitud": self.longitud,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "barrio": self.barrio,
            "provincia": self.provincia,
            "estado": self.estado,
            "estado": self.estado,  # Repetido, probablemente debería ser 'pais'
            "codigo_postal": self.codigo_postal,
            "clima": self.clima.to_dict()  # Convierte el objeto clima en un diccionario también.
        }

    # Método privado que obtiene la dirección, ciudad, barrio, provincia, estado, país y código postal.
    def __obtener_direccion(self):
        try:
            # Inicializa el geolocalizador con un user_agent.
            geolocator = Nominatim(user_agent="test")
            # Realiza la consulta a Nominatim para obtener la dirección a partir de las coordenadas.
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            
            # Rellena los datos básicos de la dirección.
            self.direccion = location.address if location else "Dirección no encontrada"
            
            # Rellena los datos adicionales si están disponibles en la respuesta de Nominatim.
            try:
                self.barrio = location.raw['address']['suburb'] if 'suburb' in location.raw['address'] else None
                self.ciudad = location.raw['address']['city'] if 'city' in location.raw['address'] else None
                self.provincia = location.raw['address']['province'] if 'province' in location.raw['address'] else None
                self.estado = location.raw['address']['state'] if 'state' in location.raw['address'] else None
                self.pais = location.raw['address']['country'] if 'country' in location.raw['address'] else None
                self.codigo_postal = location.raw['address']['postcode'] if 'postcode' in location.raw['address'] else None
            except:
                pass
        except Exception as e:
            # Captura cualquier error al intentar obtener la dirección y muestra un mensaje de error.
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"
        
    # Método que verifica si las coordenadas actuales son las mismas que las pasadas como parámetro.
    def check_lat_lng(self, latitud, longitud):
        if self.latitud == latitud:
            if self.longitud == longitud:
                return True
            else:
                return False
        else:
            return False

    # Método que muestra la información completa del localizador, incluyendo los datos de clima.
    def mostrar_informacion(self):
        # Formatea la información del localizador para su presentación.
        info_localizador = (
            f"Localizador:\n"
            f"  Latitud: {self.latitud}\n"
            f"  Longitud: {self.longitud}\n"
            f"  Dirección: {self.direccion}\n"
            f"  Ciudad: {self.ciudad}\n"
            f"  Barrio: {self.barrio}\n"
            f"  Provincia: {self.provincia}\n"
            f"  Estado: {self.estado}\n"
            f"  País: {self.pais}\n"
            f"  Código postal: {self.codigo_postal}"
        )
        
        # Muestra la información del localizador y del clima.
        print(info_localizador)
        print(self.clima)