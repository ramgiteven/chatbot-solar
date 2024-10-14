import os
import json
import requests


class geocoding_repository:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_CLOUD_API_KEY')
        if not self.api_key:
            raise ValueError("La variable de entorno 'GOOGLE_CLOUD_API_KEY' no está configurada.")

    def get_coordinates(self, address):
        """
            Get coordinates GeoCodingApi
        """
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Error al obtener coordenadas")
