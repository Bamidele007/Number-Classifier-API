from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.number_utils import *

application = Flask(__name__)
app = application
CORS(app)

def is_valid_number(s):
   try:
       float(s)
       return True
   except ValueError:
       return False

@app.route('/health', methods=['GET'])
def health_check():
   return jsonify({"status": "healthy"}), 200

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number', '')
        float_num = float(number)  # Convert string to float
        num = int(float_num)       # Convert float to int
        abs_num = abs(num)         # Get absolute value

        response = {
            "number": num,
            "is_prime": is_prime(abs_num),
            "is_perfect": is_perfect(abs_num),
            "properties": ["even"] if num % 2 == 0 else ["odd"],
            "digit_sum": get_digit_sum(abs_num),
            "fun_fact": get_fun_fact(num)
        }
        return jsonify(response), 200

    except ValueError:
        return jsonify({"number": number, "error": True}), 400