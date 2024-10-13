from flask import Blueprint, request, jsonify
from app.use_cases.chatbot_use_case import ChatbotUseCase
from app.services.openai_client import OpenAIClient

# Crear un Blueprint para las rutas del chatbot
chatbot_bp = Blueprint('chatbot', __name__)

# Instanciar el caso de uso del chatbot
openai_gateway = OpenAIClient()
chatbot_use_case = ChatbotUseCase(openai_gateway=openai_gateway)

# Ruta para iniciar una nueva conversación
@chatbot_bp.route('/start', methods=['GET'])
def start_conversation():
    try:
        thread_id = chatbot_use_case.create_assistant()
        return jsonify({"thread_id": thread_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para procesar un mensaje en el chatbot
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    thread_id = data.get('thread_id')
    message = data.get('message', '')

    if not thread_id or not message:
        return jsonify({"error": "Missing thread_id or message"}), 400

    try:
        response = chatbot_use_case.process_chat_message(thread_id, message)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
