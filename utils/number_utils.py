def get_properties(n: int) -> list:
    properties = []
    abs_n = abs(n)
    
    # Check Armstrong property using absolute value
    if is_armstrong(abs_n):
        properties.append("armstrong")
    
    # Check odd/even using original number
    properties.append("odd" if n % 2 else "even")
    
    return properties