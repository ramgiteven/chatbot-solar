from abc import ABC, abstractmethod

class AirtableGatewayInterface(ABC):
    @abstractmethod
    def create_lead(self, name: str, phone: str, address: str):
        """
        Crea un nuevo lead en Airtable.

        :param name: Nombre del lead
        :param phone: Teléfono del lead
        :param address: Dirección del lead
        :return: Diccionario con la respuesta de Airtable
        """
        pass
