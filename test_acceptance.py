from triangle import classify_triangle

def test_customer_requirements():
    # Check that valid triangles are classified correctly
    assert classify_triangle(4, 4, 4) == "Equilateral"
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"

    # Check that invalid triangles return Invalid
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"

    # Check that right triangles are flagged
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    