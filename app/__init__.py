from flask import Flask
from app.controllers.chatbot_controller import chatbot_bp

def create_app():
    """
    Inicializa la aplicación Flask y registra los blueprints.
    """
    app = Flask(__name__)
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

    return app
