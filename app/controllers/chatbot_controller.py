from flask import Blueprint, jsonify, request
from app.services.chatbot_service import chatbot_service
from app.repositories.openai_repository import openai_repository
from app.useCases.get_solar_potential import get_solar_potential
from app.useCases.parse_finanacial_analisis import parse_financial_analisis
from app.useCases.save_data_customer import save_data_customer

chatbot_bp = Blueprint('chatbot', __name__)
chatbot_service_instance = chatbot_service(openai_repository(), get_solar_potential(), parse_financial_analisis(), save_data_customer())

@chatbot_bp.route('/start', methods=['GET'])
def start_conversation():
    """
        Create thread of conversation
    """
    try:
        thread_id = chatbot_service_instance.start_conversation()
        return jsonify({"thread_id": thread_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """
        Send message based to thread
    """
    data = request.json
    thread_id = data.get('thread_id')
    user_input = data.get('message', '')

    if not thread_id:
        return jsonify({"error": "Missing thread_id"}), 400

    if not user_input:
        return jsonify({"error": "Missing message"}), 400

    try:
        response = chatbot_service_instance.process_message(thread_id, user_input)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@chatbot_bp.route('/cancel', methods=['POST'])
def cancel_run():
    """
        Kill thread and conversation with errors
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
        return jsonify({"status": "Run cancelled successfully", "response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
