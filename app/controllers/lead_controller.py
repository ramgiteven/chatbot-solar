from flask import Blueprint, request, jsonify
from app.use_cases.create_lead_use_case import CreateLeadUseCase
from app.services.airtable_client import AirtableClient

# Crear un Blueprint para las rutas de leads
lead_bp = Blueprint('lead', __name__)

# Instanciar el servicio y el caso de uso para crear leads
airtable_gateway = AirtableClient()
create_lead_use_case = CreateLeadUseCase(airtable_gateway=airtable_gateway)

# Ruta para crear un lead
@lead_bp.route('/create', methods=['POST'])
def create_lead():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    address = data.get('address')

    if not name or not phone or not address:
        return jsonify({"error": "Missing name, phone, or address"}), 400

    try:
        lead = create_lead_use_case.execute(name, phone, address)
        return jsonify({"lead": lead}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
