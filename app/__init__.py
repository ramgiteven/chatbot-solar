from flask import Flask
from app.controllers.chatbot_controller import chatbot_bp
from app.controllers.solar_controller import solar_bp
from app.controllers.lead_controller import lead_bp

def create_app():
    app = Flask(__name__)

    # Registrar los Blueprints
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
    app.register_blueprint(solar_bp, url_prefix='/solar')
    app.register_blueprint(lead_bp, url_prefix='/lead')

    return app
