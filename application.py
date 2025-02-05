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
       if number is None:
           return jsonify({"number": None, "error": True}), 400

       # Convert to float first, then int - handles both floats and negative numbers
       try:
           float_num = float(number)
           num = int(float_num)
           abs_num = abs(num)
           
           response = {
               "number": num,  # Returns integer part only
               "is_prime": is_prime(abs_num) if num > 0 else False,
               "is_perfect": is_perfect(abs_num) if num > 0 else False, 
               "properties": get_properties(num),
               "digit_sum": get_digit_sum(abs_num),
               "fun_fact": get_fun_fact(num)
           }
           return jsonify(response), 200
           
       except ValueError:
           return jsonify({"number": number, "error": True}), 400

   except Exception as e:
       return jsonify({"number": number if 'number' in locals() else None, "error": True}), 400