import requests
import os
from app.interfaces.geocoding_gateway_interface import GeocodingGatewayInterface

class GeocodingClient(GeocodingGatewayInterface):
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_CLOUD_API_KEY')

    def get_coordinates(self, address: str):
        """
        Obtiene las coordenadas (latitud y longitud) de una dirección.

        :param address: Dirección para la cual obtener las coordenadas
        :return: Una tupla con la latitud y la longitud
        """
        geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.api_key}"
        
        response = requests.get(geocoding_url)

        if response.status_code == 200:
            location = response.json().get('results')[0].get('geometry').get('location')
            return location['lat'], location['lng']
        else:
            raise Exception(f"Error al obtener coordenadas: {response.text}")
