import requests
import os
from app.interfaces.airtable_gateway_interface import AirtableGatewayInterface

class AirtableClient(AirtableGatewayInterface):
    def __init__(self):
        self.api_key = os.getenv('AIRTABLE_API_KEY')
        self.base_url = "https://api.airtable.com/v0/appM1yx0NobvowCAg/Leads"

    def create_lead(self, name: str, phone: str, address: str):
        """
        Implementa el método para crear un lead en Airtable.

        :param name: Nombre del lead
        :param phone: Teléfono del lead
        :param address: Dirección del lead
        :return: Respuesta de Airtable en formato JSON
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "records": [{
                "fields": {
                    "Name": name,
                    "Phone": phone,
                    "Address": address
                }
            }]
        }

        response = requests.post(self.base_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al crear lead en Airtable: {response.text}")
