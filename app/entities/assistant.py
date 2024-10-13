class Assistant:
    def __init__(self, assistant_id: str, name: str):
        """
        Inicializa un nuevo asistente con un ID único y un nombre.
        
        :param assistant_id: ID del asistente
        :param name: Nombre del asistente
        """
        self.assistant_id = assistant_id
        self.name = name

    def get_info(self):
        """
        Devuelve la información básica del asistente.
        """
        return {
            "assistant_id": self.assistant_id,
            "name": self.name
        }
    
    def update_name(self, new_name: str):
        """
        Actualiza el nombre del asistente.
        
        :param new_name: Nuevo nombre del asistente
        """
        self.name = new_name
