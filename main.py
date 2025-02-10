from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.number_utils import *

application = Flask(__name__)
app = application
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        input_number = request.args.get('number', '')
        
        if not input_number:
            return jsonify({
                "number": input_number,
                "error": True
            }), 400
            
        num = int(float(input_number))
        abs_num = abs(num)
        
        return jsonify({
            "number": num,
            "is_prime": False if num <= 1 else is_prime(abs_num),
            "is_perfect": False if num <= 1 else is_perfect(abs_num),
            "properties": get_properties(num),
            "digit_sum": get_digit_sum(abs_num),
            "fun_fact": get_fun_fact(num)
        }), 200
        
    except (ValueError, TypeError):
        return jsonify({
            "number": input_number,
            "error": True
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')