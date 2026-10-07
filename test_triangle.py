import math
import pytest
from triangle import is_valid_triangle, classify_triangle

def test_invalid_negative_sides():
    # Covers the <= 0 requirement
    assert classify_triangle(-1, 5, 5) == "Invalid"
    assert classify_triangle(0, 4, 3) == "Invalid"

def test_degenerate_boundary():
    # Covers the degenerate case where a + b == c
    assert classify_triangle(2, 2, 4) == "Invalid"
    assert classify_triangle(3, 4, 7) == "Invalid"

def test_equilateral():
    # Covers all sides equal
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    # Covers exactly two sides equal
    assert classify_triangle(3, 3, 2) == "Isosceles"

def test_scalene():
    # Covers all sides different
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_integer():
    # Covers standard right triangle
    assert classify_triangle(3, 4, 5) == "Right Scalene"

def test_right_non_integer():
    # Covers the specific floating point requirement
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"