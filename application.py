from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.number_utils import *

application = Flask(__name__)
app = application
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number', '')
        
        # Handle empty string case
        if not number:
            return jsonify({"number": None, "error": True}), 400
            
        # Convert to number, handling both integers and floats
        num = int(float(number))
        abs_num = abs(num)
        
        # Always return 200 if we got here
        return jsonify({
            "number": num,
            "is_prime": is_prime(abs_num),
            "is_perfect": is_perfect(abs_num),
            "properties": ["even"] if num % 2 == 0 else ["odd"],
            "digit_sum": get_digit_sum(abs_num),
            "fun_fact": get_fun_fact(num)
        }), 200
        
    except (ValueError, TypeError):
        # Only return 400 for non-numeric strings
        return jsonify({"number": number, "error": True}), 400

if __name__ == '__main__':
    app.run()