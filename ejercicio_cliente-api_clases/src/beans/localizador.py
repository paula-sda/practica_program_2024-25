from geopy.geocoders import Nominatim

from beans.clima import Clima



## Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
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

    # Constructor que recibe latitud y longitud y obtiene la dirección y el clima
    def __init__(self, latitud, longitud):
        # Almacenamos las coordenadas
        self.latitud = latitud
        self.longitud = longitud
        # Llamamos al método privado para obtener la dirección
        self.__obtener_direccion()
        # Creamos un objeto de la clase Clima para obtener datos climáticos
        self.clima = Clima(self.latitud, self.longitud)

    # Método privado para obtener la dirección a partir de la latitud y longitud
    def __obtener_direccion(self):
        try:
            # Usamos Nominatim para obtener la ubicación inversa
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            
            # Si encontramos la ubicación, almacenamos la dirección
            self.direccion = location.address if location else "Dirección no encontrada"
            
            # Obtener información adicional como barrio, ciudad, provincia, etc.
            try:
                self.barrio = location.raw['address']['suburb'] if 'suburb' in location.raw['address'] else None
                self.ciudad = location.raw['address']['city'] if 'city' in location.raw['address'] else None
                self.provincia = location.raw['address']['province'] if 'province' in location.raw['address'] else None
                self.estado = location.raw['address']['state'] if 'state' in location.raw['address'] else None
                self.pais = location.raw['address']['country'] if 'country' in location.raw['address'] else None
                self.codigo_postal = location.raw['address']['postcode'] if 'postcode' in location.raw['address'] else None
            except:
                # Si ocurre un error al obtener los datos adicionales, no hacemos nada
                pass
        except Exception as e:
            # Si ocurre un error en la obtención de la dirección, lo capturamos
            print(f"Error al obtener la dirección: {e}")
            # Asignamos un valor predeterminado en caso de error
            self.direccion = "Error al obtener la dirección"
        
    # Método para comprobar si las coordenadas coinciden con las dadas
    def check_lat_lng(self, latitud, longitud):
        # Comprobar si las latitudes y longitudes son iguales
        if self.latitud == latitud:
            if self.longitud == longitud:
                return True
            else:
                return False
        else:
            return False

    # Método para mostrar toda la información obtenida
    def mostrar_informacion(self):
        # Cadena con la información del localizador
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
        
        # Mostramos la información del Localizador y el clima asociado
        print(info_localizador)
        print(self.clima)


