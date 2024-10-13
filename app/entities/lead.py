class Lead:
    def __init__(self, name: str, phone: str, address: str):
        """
        Inicializa un nuevo lead con nombre, teléfono y dirección.
        
        :param name: Nombre del lead
        :param phone: Teléfono del lead
        :param address: Dirección del lead
        """
        self.name = name
        self.phone = phone
        self.address = address

    def get_lead_info(self):
        """
        Devuelve la información completa del lead.
        """
        return {
            "name": self.name,
            "phone": self.phone,
            "address": self.address
        }
    
    def update_phone(self, new_phone: str):
        """
        Actualiza el número de teléfono del lead.
        
        :param new_phone: Nuevo número de teléfono
        """
        self.phone = new_phone

    def update_address(self, new_address: str):
        """
        Actualiza la dirección del lead.
        
        :param new_address: Nueva dirección
        """
        self.address = new_address
