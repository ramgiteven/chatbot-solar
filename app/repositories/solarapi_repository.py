import os
import requests

class solarapi_repository:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_CLOUD_API_KEY')

    def get_solar_data_from_solar_api(self, lat, lng):
        """
        Obtener datos de solar_api
        """
        solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}"
        "&location.longitude={lng}&requiredQuality=HIGH&key={self.api_key}"
        response = requests.get(solar_api_url)
        if response.status_code == 200:
            print(f"Datos solares obtenidos exitosamente.")
            return response.json()
        else:
            print(f"Error al obtener datos solares: {response.text}")
            return None
