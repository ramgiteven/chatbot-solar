from app.interfaces.airtable_gateway_interface import AirtableGatewayInterface
from app.entities.lead import Lead

class CreateLeadUseCase:
    def __init__(self, airtable_gateway: AirtableGatewayInterface):
        """
        Inicializa el caso de uso con el gateway para Airtable.
        """
        self.airtable_gateway = airtable_gateway

    def execute(self, name: str, phone: str, address: str):
        """
        Crea un lead en Airtable utilizando los datos proporcionados.

        :param name: Nombre del lead
        :param phone: Teléfono del lead
        :param address: Dirección del lead
        :return: Respuesta del gateway de Airtable
        """
        # Crear la entidad Lead
        lead = Lead(name=name, phone=phone, address=address)

        # Obtener la información del lead
        lead_info = lead.get_lead_info()

        # Enviar la información al gateway para crear el lead
        return self.airtable_gateway.create_lead(
            name=lead_info["name"], 
            phone=lead_info["phone"], 
            address=lead_info["address"]
        )
