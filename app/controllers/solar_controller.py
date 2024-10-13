from flask import Blueprint, request, jsonify
from app.use_cases.solar_panel_calculations_use_case import SolarPanelCalculationsUseCase
from app.services.geocoding_client import GeocodingClient
from app.services.openai_client import OpenAIClient

# Crear un Blueprint para las rutas solares
solar_bp = Blueprint('solar', __name__)

# Instanciar los servicios y el caso de uso para cálculos solares
geocoding_gateway = GeocodingClient()
openai_gateway = OpenAIClient()
solar_calculations_use_case = SolarPanelCalculationsUseCase(
    geocoding_gateway=geocoding_gateway,
    openai_gateway=openai_gateway
)

# Ruta para cálculos solares
@solar_bp.route('/calculate', methods=['POST'])
def solar_panel_calculations():
    data = request.json
    address = data.get('address')
    monthly_bill = data.get('monthly_bill')

    if not address or not monthly_bill:
        return jsonify({"error": "Missing address or monthly_bill"}), 400

    try:
        result = solar_calculations_use_case.execute(address, int(monthly_bill))
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
