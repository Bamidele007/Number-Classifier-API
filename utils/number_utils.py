# app/utils/number_utils.py
import requests
from math import sqrt

def is_prime(n: int) -> bool:
    # Negative numbers can't be prime
    if n <= 1:  # Changed from n < 2 to catch both negative and 1
        return False
    for i in range(2, int(sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def get_properties(n: int) -> list:
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 else "even")
    return properties

def get_digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        return f"{n} is an {'Armstrong' if is_armstrong(n) else 'interesting'} number"
    except:
        return f"{n} is an {'Armstrong' if is_armstrong(n) else 'interesting'} number"