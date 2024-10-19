from app import create_app
import jsonify

app = create_app()

@app.route('/', methods=['GET'])
def ping():
    try: 
        return jsonify({"message": successfull}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    
    app.run(debug=True)
