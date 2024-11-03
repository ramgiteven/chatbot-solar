from flask import Blueprint, jsonify, request
from app.services.chatbot_service import chatbot_service
from app.repositories.openai_repository import openai_repository
from app.use_cases.get_solar_potential import get_solar_potential
from app.use_cases.parse_finanacial_analisis import parse_financial_analisis
from app.use_cases.save_data_customer import save_data_customer

chatbot_bp = Blueprint('chatbot', __name__)
chatbot_service_instance = chatbot_service(openai_repository(), get_solar_potential(), parse_financial_analisis(), save_data_customer())

@chatbot_bp.route('/start', methods=['GET'])
def start_conversation():
    """
        Crear un hilo de conversación
    """
    try:
        thread_id = chatbot_service_instance.start_conversation()
        return jsonify({"thread_id": thread_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """
        Envio mensaje basado en el hilo de conversación
    """
    data = request.json
    thread_id = data.get('thread_id')
    user_input = data.get('message', '')

    if not thread_id:
        return jsonify({"error": "Falta el Hilo de la converación"}), 400

    if not user_input:
        return jsonify({"error": "Falta el mensaje"}), 400

    try:
        response = chatbot_service_instance.process_message(thread_id, user_input)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@chatbot_bp.route('/cancel', methods=['POST'])
def cancel_run():
    """
        Detener la ejecución de un hilo de conversación
    """
    data = request.json
    thread_id = data.get('thread_id')
    run_id = data.get('run_id')
    
    if not thread_id:
        return jsonify({"error": "Missing thread_id"}), 400

    if not run_id:
        return jsonify({"error": "Missing run_id"}), 400

    try:
        response = chatbot_service_instance.cancel_run(thread_id, run_id)
        return jsonify({"status": f"El hilo {thread_id} de la ejecución {run_id} se detuvo correctamente ", "response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
