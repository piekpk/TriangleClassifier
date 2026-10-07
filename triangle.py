import math

def is_valid_triangle(a, b, c) -> bool:
    # Any side <= 0 is invalid
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Triangle inequality fails (includes the degenerate boundary case)
    if a + b <= c or a + c <= b or b + c <= a:
        return False
        
    return True

def classify_triangle(a, b, c) -> str:
    # 1. Check validity
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # 2. Determine base shape
    if a == b == c:
        shape = "Equilateral"
    elif a == b or b == c or a == c:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    # 3. Check for right triangle using a tolerance
    # Sort the sides to easily identify the hypotenuse (the longest side)
    sides = sorted([a, b, c])
    leg1, leg2, hypotenuse = sides[0], sides[1], sides[2]
    
    # Use math.isclose instead of == to handle floating-point precision
    if math.isclose(leg1**2 + leg2**2, hypotenuse**2, rel_tol=1e-9, abs_tol=1e-9):
        return f"Right {shape}"

    return shape