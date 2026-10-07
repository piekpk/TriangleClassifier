from triangle import classify_triangle

def test_stained_glass_acceptance():
    # Criterion 1: Invalid triangles return a safe message, no crash
    assert classify_triangle(0, 10, 10) == "Invalid"
    assert classify_triangle(3, 3, 10) == "Invalid"
    
    # Criterion 2: Right-angle pieces are flagged with "Right" for reinforced corners
    shape_result = classify_triangle(3, 4, 5)
    assert "Right" in shape_result
    
    # Criterion 3: Valid pieces correctly identify the base shape for the builder
    assert classify_triangle(6, 6, 6) == "Equilateral"
    assert classify_triangle(5, 5, 8) == "Isosceles"