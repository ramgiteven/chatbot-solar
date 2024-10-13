from flask import Blueprint, request, jsonify
from app.use_cases.chatbot_use_case import ChatbotUseCase
from app.services.airtable_client import AirtableClient

# Crear un Blueprint para las rutas de creación de leads
lead_bp = Blueprint('lead', __name__)

# Instanciar el caso de uso con el gateway de Airtable
airtable_gateway = AirtableClient()
chatbot_use_case = ChatbotUseCase(airtable_gateway=airtable_gateway)

# Ruta para crear un lead
@lead_bp.route('/create-lead', methods=['POST'])
def create_lead():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    address = data.get('address')

    if not name or not phone or not address:
        return jsonify({"error": "Missing name, phone, or address"}), 400

    try:
        lead = chatbot_use_case.create_lead(name, phone, address)
        return jsonify({"lead": lead}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
