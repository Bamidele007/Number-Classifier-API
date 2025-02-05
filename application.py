from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.number_utils import *

application = Flask(__name__)
app = application
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number')
        if not number:
            return jsonify({
                "number": number,
                "error": True
            }), 400
        
        # Convert to float first to handle decimals, then to int
        num = int(float(number))
        return jsonify({
            "number": num,
            "is_prime": is_prime(abs(num)),  # Use abs for negative numbers
            "is_perfect": is_perfect(abs(num)),
            "properties": get_properties(num),
            "digit_sum": get_digit_sum(abs(num)),
            "fun_fact": get_fun_fact(num)
        }), 200

    except ValueError:
        return jsonify({
            "number": number,
            "error": True
        }), 400