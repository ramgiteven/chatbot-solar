from app import create_app

app = create_app()

@app.route('/', methods=['GET'])
def ping():
    return "<h1> Deployed  Successful</h1>"



if __name__ == "__main__":
    
    app.run(debug=True)
