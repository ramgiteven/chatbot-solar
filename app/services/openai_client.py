import openai
import os
import json
from app.interfaces.openai_gateway_interface import OpenAIGatewayInterface

class OpenAIClient(OpenAIGatewayInterface):
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def get_solar_data(self, lat: float, lng: float):
        """
        Implementa el método para obtener datos de energía solar basados en coordenadas.

        :param lat: Latitud
        :param lng: Longitud
        :return: Datos de energía solar en formato JSON
        """
        solar_api_url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={lng}&requiredQuality=HIGH&key={os.getenv('GOOGLE_CLOUD_API_KEY')}"

        response = requests.get(solar_api_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener datos solares: {response.text}")

    def simplify_financial_data(self, data: dict):
        """
        Implementa el método para simplificar los datos financieros usando OpenAI.

        :param data: Datos financieros en formato dict
        :return: Datos simplificados en formato dict
        """
        system_prompt = "Format the financial data provided in a simple and understandable way."
        
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is some data: {json.dumps(data)}"}
            ],
            temperature=0.5
        )

        simplified_data = completion.choices[0].message['content']
        return json.loads(simplified_data)

    def create_assistant(self):
        """
        Implementa el método para crear un asistente en OpenAI.

        :return: ID del asistente creado
        """
        assistant = openai.Assistant.create(
            model="gpt-4",
            instructions="Assistant for solar panel analysis and lead generation."
        )

        return assistant.id
