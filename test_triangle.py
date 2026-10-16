import math
from triangle import classify_triangle


# Test that a 3-4-5 triangle is classified as Right Scalene
def test_3_4_5_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


    # Test that three equal sides are classified as Equilateral
def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"

# Test that exactly two equal sides are classified as Isosceles
def test_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"

    # Test that three different side lengths form a non-right Scalene triangle
def test_scalene_triangle():
    assert classify_triangle(3, 4, 6) == "Scalene"

    # Test that a triangle with a zero-length side is classified as Invalid
def test_invalid_triangle():
    assert classify_triangle(0, 1, 1) == "Invalid"


# Test that side lengths where two sides equal the third side are classified as Invalid
def test_invalid_triangle_two_sides_equal_third():
    assert classify_triangle(1, 1, 2) == "Invalid"


    # Test that a right isosceles triangle with a non-integer hypotenuse is recognized
def test_right_isosceles_triangle_non_integer_hypotenuse():
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"


    # Test that a triangle with a negative side length is classified as Invalid
def test_invalid_triangle_negative_side():
    assert classify_triangle(-1, 1, 1) == "Invalid"