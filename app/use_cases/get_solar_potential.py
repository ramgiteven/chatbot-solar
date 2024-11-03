from app.repositories.geocoding_repository import geocoding_repository
from app.repositories.solarapi_repository import solarapi_repository

class get_solar_potential:
    repository_geocoding = geocoding_repository()
    repository_solar_potential = solarapi_repository()

    def __init__(self):
        pass

    def execute(self, address, monthlyBill):
        print(
            f"Calculando el potencial de paneles solares para {address} con una factura de {monthlyBill}."
        )
        return self.get_financial_data_for_address(address)
       
    def get_financial_data_for_address(self, address):
        print(
            f"Obteniendo datos financieros para la dirección {address}."
        )
        lat, lng = self.repository_geocoding.get_coordinates(address)

        if not lat or not lng:
            return {"error": "No se pudieron obtener las coordenadas para la dirección proporcionada."}

        solar_api_response = self.repository_solar_potential.get_solar_data_from_solar_api(lat, lng)
        
        if not solar_api_response:
            return {"error": "No se pudo obtener información de la API solar para la dirección proporcionada."}
        
        return self.extract_financial_analyses_list_from_solar_data(solar_api_response)
    
    def get_coordinates_from_geocoding_api(self, address):
        print(f"Obteniendo coordenadas para la dirección {address}.")
        return self.repository_geocoding.get_coordinates(address)

    def extract_financial_analyses_list_from_solar_data(self, solar_data):
        try:
            return solar_data.get('solarPotential', {}).get('financialAnalyses', [])
        except KeyError as e:
            print(f"Error al extraer datos: {e}")
