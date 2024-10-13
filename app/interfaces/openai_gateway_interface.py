from abc import ABC, abstractmethod

class OpenAIGatewayInterface(ABC):
    @abstractmethod
    def get_solar_data(self, lat: float, lng: float):
        """
        Obtiene datos de energía solar basados en las coordenadas geográficas.

        :param lat: Latitud de la ubicación
        :param lng: Longitud de la ubicación
        :return: Diccionario con los datos de energía solar
        """
        pass

    @abstractmethod
    def simplify_financial_data(self, data: dict):
        """
        Simplifica los datos financieros utilizando el modelo de OpenAI.

        :param data: Diccionario con los datos financieros
        :return: Diccionario con los datos simplificados
        """
        pass

    @abstractmethod
    def create_assistant(self):
        """
        Crea un nuevo asistente en OpenAI para manejar conversaciones del chatbot.

        :return: ID del asistente creado
        """
        pass
