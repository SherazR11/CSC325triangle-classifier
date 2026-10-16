import math

def is_valid_triangle(a, b, c) -> bool:
    # Check all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Checking triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True

def classify_triangle(a, b, c) -> str:
    # Check iftriangle is valid
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Classify by side lengths
    if a == b == c:
        result = "Equilateral"
    elif a == b or a == c or b == c:
        result = "Isosceles"
    else:
        result = "Scalene"

    # Checking for right triangle using longest side
    sides = sorted([a, b, c])

    if math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2,
        rel_tol=1e-9,
        abs_tol=1e-9
    ):
        result = "Right " + result

    return result