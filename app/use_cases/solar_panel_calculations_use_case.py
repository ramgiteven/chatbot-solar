from app.interfaces.geocoding_gateway_interface import GeocodingGatewayInterface
from app.interfaces.openai_gateway_interface import OpenAIGatewayInterface
from app.entities.solar_analysis import SolarAnalysis

class SolarPanelCalculationsUseCase:
    def __init__(self, geocoding_gateway: GeocodingGatewayInterface, openai_gateway: OpenAIGatewayInterface):
        """
        Inicializa el caso de uso con los gateways para la API de Geocoding y OpenAI.
        """
        self.geocoding_gateway = geocoding_gateway
        self.openai_gateway = openai_gateway

    def execute(self, address: str, monthly_bill: int):
        """
        Realiza cálculos solares basados en la dirección y la factura mensual.

        :param address: Dirección del usuario
        :param monthly_bill: Factura mensual del usuario
        :return: Resumen del análisis solar
        """
        # Obtener las coordenadas (lat, lng) usando el servicio de geocodificación
        lat, lng = self.geocoding_gateway.get_coordinates(address)

        # Obtener los datos solares usando el gateway de OpenAI
        solar_data = self.openai_gateway.get_solar_data(lat, lng)

        # Crear una entidad SolarAnalysis con los datos obtenidos
        solar_analysis = SolarAnalysis(
            address=address, 
            monthly_bill=monthly_bill, 
            financial_analysis=solar_data
        )

        # Devolver un resumen del análisis
        return solar_analysis.get_analysis_summary()
