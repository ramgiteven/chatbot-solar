from app.repositories.geocoding_repository import geocoding_repository
from app.repositories.solarapi_repository import solarapi_repository

class get_solar_potential:

    def __init__(self, repository_geocoding = geocoding_repository, repository_solar_potential= solarapi_repository):
        self.repository_geocoding = repository_geocoding()
        self.repository_solar_potential = repository_solar_potential()

    def execute(self, address, monthlyBill):
        print(
            f"Calculating solar panel potential for {address} with bill amount {monthlyBill}."
        )
        return  self.get_financial_data_for_address(address)
       
    def get_financial_data_for_address(self, address):
        print(
            f"get finalacial data for adreess l for {address}."
        )
        lat, lng = self.repository_geocoding.get_coordinates(address)

        if not lat or not lng:
            return {"error": "Could not get coordinates for the address provided."}

        solar_api_response = self.repository_solar_potential.get_solar_data_from_solar_api(lat, lng)
        
        if not solar_api_response:
            return {"error": "Could not get Solar api info for the address provided."}
        
        return self.extract_financial_analyses_list_from_solar_data(solar_api_response)
    
    def get_coordinates_from_geocoding_api(self, address):
        print(f"get coordinates data for adreess l for {address}.")
        return self.repository_geocoding.get_coordinates(address)


    def extract_financial_analyses_list_from_solar_data(self, solar_data):
        try:
            return solar_data.get('solarPotential', {}).get('financialAnalyses', [])
        except KeyError as e:
            print(f"Data extraction error: {e}")
