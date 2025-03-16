import pytest
from bmi_calculator import (
    convert_weight_to_kg,
    convert_height_to_meters,
    compute_bmi,
    classify_bmi,
    calculate_bmi
)

# 1️⃣ Test convert_weight_to_kg()
@pytest.mark.parametrize("weight, expected", [
    (100, 45.0),  # Normal weight conversion
    (200, 90.0),  # Double weight
    (0, 0.0),  # Edge case: Zero weight
    (1, 0.45),  # Smallest weight
])
def test_convert_weight_to_kg(weight, expected):
    assert convert_weight_to_kg(weight) == expected

# 2️⃣ Test convert_height_to_meters()
@pytest.mark.parametrize("feet, inches, expected", [
    (5, 7, 1.675),  # Standard height
    (6, 0, 1.8),  # Even feet, no inches
    (0, 1, 0.025),  # Only inches
])
def test_convert_height_to_meters(feet, inches, expected):
    assert convert_height_to_meters(feet, inches) == expected

# Check for division by zero
def test_convert_height_to_meters_zero():
    with pytest.raises(ValueError, match="Height cannot be zero."):
        convert_height_to_meters(0, 0)

# 3️⃣ Test compute_bmi()
@pytest.mark.parametrize("weight_kg, height_m, expected", [
    (45, 1.675, 16.0),  # Underweight
    (70, 1.75, 22.9),  # Normal weight
    (90, 1.75, 29.4),  # Overweight
    (100, 1.6, 39.1),  # Obese
])
def test_compute_bmi(weight_kg, height_m, expected):
    assert compute_bmi(weight_kg, height_m) == expected

# 4️⃣ Test classify_bmi() with Boundary Shift and Missing Boundary Testing
@pytest.mark.parametrize("bmi, expected", [
    (18.4, "Underweight"),  # Just below 18.5
    (18.5, "Normal weight"),  # Exact 18.5 boundary
    (18.6, "Normal weight"),  # Just above 18.5
    (24.8, "Normal weight"),  # Just below 25
    (24.9, "Normal weight"),  # Exact 24.9 boundary
    (25.0, "Overweight"),  # Exact 25.0 boundary
    (25.1, "Overweight"),  # Just above 25
    (29.9, "Overweight"),  # Just below 30
    (30.0, "Obese"),  # Exact 30.0 boundary
    (30.1, "Obese"),  # Just above 30
])
def test_classify_bmi(bmi, expected):
    assert classify_bmi(bmi) == expected

# 5️⃣ Test calculate_bmi() (End-to-End Test)
@pytest.mark.parametrize("weight, feet, inches, expected", [
    (96, 5, 7, "Underweight"),  # Just below normal
    (97, 5, 7, "Normal weight"),  # Exact 18.5
    (130, 5, 7, "Normal weight"),  # Just below overweight
    (131, 5, 7, "Overweight"),  # Exact 25.0
    (156, 5, 7, "Overweight"),  # Just below obese
    (157, 5, 7, "Obese"),  # Exact 30.0
])
def test_calculate_bmi(weight, feet, inches, expected):
    assert calculate_bmi(weight, feet, inches) == expected
