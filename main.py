from app import create_app

# Inicializar la aplicación
app = create_app()

if __name__ == "__main__":
    # Ejecutar la aplicación Flask en modo debug
    app.run(debug=True)
