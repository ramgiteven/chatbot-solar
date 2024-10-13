from app.interfaces.openai_gateway_interface import OpenAIGatewayInterface

class ChatbotUseCase:
    def __init__(self, openai_gateway: OpenAIGatewayInterface):
        """
        Inicializa el caso de uso con el gateway para OpenAI.
        """
        self.openai_gateway = openai_gateway

    def create_assistant(self):
        """
        Crea un nuevo asistente en OpenAI.

        :return: ID del asistente creado
        """
        return self.openai_gateway.create_assistant()

    def process_chat_message(self, thread_id: str, message: str):
        """
        Procesa un mensaje enviado al chatbot.

        :param thread_id: ID del hilo de conversación
        :param message: Mensaje enviado por el usuario
        :return: Respuesta del asistente de OpenAI
        """
        # Añadir el mensaje al hilo usando el gateway de OpenAI
        self.openai_gateway.add_message_to_thread(thread_id, message)

        # Obtener la respuesta del asistente
        return self.openai_gateway.get_latest_assistant_response(thread_id)
