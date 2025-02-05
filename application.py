from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.number_utils import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number')
        if not number or not number.isdigit():
            return jsonify({
                "number": number,
                "error": True
            }), 400
        
        num = int(number)
        return jsonify({
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": get_properties(num),
            "digit_sum": get_digit_sum(num),
            "fun_fact": get_fun_fact(num)
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")  # Add logging
        return jsonify({
            "number": number if 'number' in locals() else None,
            "error": True
        }), 400

application = app  # Add this line

if __name__ == '__main__':
    app.run()