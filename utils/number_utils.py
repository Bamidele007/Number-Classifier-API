import requests
from math import sqrt

def is_prime(n: int) -> bool:
    # Negative numbers and 1 or 0 can't be prime
    if n <= 1:
        return False
    for i in range(2, int(sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    num_str = str(abs(n))  # Use absolute value
    power = len(num_str)
    return abs(n) == sum(int(digit) ** power for digit in num_str)

def get_properties(n: int) -> list:
    properties = []
    abs_n = abs(n)
    if is_armstrong(abs_n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 else "even")
    return properties

def get_digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(n: int) -> str:
    try:
        abs_n = abs(n)
        response = requests.get(f"http://numbersapi.com/{abs_n}/math")
        if response.status_code == 200:
            if n < 0:
                return f"{n} is the negative of {abs_n}. {response.text}"
            return response.text
        return f"{n} is {'negative' if n < 0 else 'positive'} and {n % 2 and 'odd' or 'even'}"
    except:
        return f"{n} is {'negative' if n < 0 else 'positive'} and {n % 2 and 'odd' or 'even'}"