from abc import ABC, abstractmethod

class GeocodingGatewayInterface(ABC):
    @abstractmethod
    def get_coordinates(self, address: str):
        """
        Obtiene las coordenadas (latitud y longitud) de una dirección a través de una API de geocodificación.

        :param address: Dirección para la cual obtener las coordenadas
        :return: Una tupla con la latitud y la longitud
        """
        pass
