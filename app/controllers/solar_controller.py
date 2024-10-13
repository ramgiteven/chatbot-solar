from flask import Blueprint, request, jsonify
from app.use_cases.chatbot_use_case import ChatbotUseCase
from app.services.openai_client import OpenAIClient
from app.services.geocoding_client import GeocodingClient

# Crear un Blueprint para las rutas solares
solar_bp = Blueprint('solar', __name__)

# Instanciar el caso de uso con los gateways necesarios
openai_gateway = OpenAIClient()
geocoding_gateway = GeocodingClient()
chatbot_use_case = ChatbotUseCase(openai_gateway=openai_gateway, geocoding_gateway=geocoding_gateway)

# Ruta para cálculos solares
@solar_bp.route('/solar', methods=['POST'])
def solar_panel_calculations():
    data = request.json
    address = data.get('address')
    monthly_bill = data.get('monthly_bill')

    if not address or not monthly_bill:
        return jsonify({"error": "Missing address or monthly_bill"}), 400

    try:
        result = chatbot_use_case.solar_panel_calculations(address, int(monthly_bill))
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
