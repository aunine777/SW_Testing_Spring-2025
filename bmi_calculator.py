def convert_weight_to_kg(weight):
    """Converts weight from pounds to kilograms."""
    return weight * 0.45

def convert_height_to_meters(height_ft, height_in):
    """Converts height from feet and inches to meters."""
    total_height_inches = (height_ft * 12) + height_in
    if total_height_inches == 0:
        raise ValueError("Height cannot be zero.")
    return total_height_inches * 0.025

def compute_bmi(weight_kg, height_meters):
    """Calculates BMI given weight in kg and height in meters."""
    return round(weight_kg / (height_meters ** 2), 1)

def classify_bmi(bmi):
    """Returns the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(weight, height_ft, height_in):
    """Main function that calculates and classifies BMI."""
    weight_kg = convert_weight_to_kg(weight)
    height_meters = convert_height_to_meters(height_ft, height_in)
    bmi = compute_bmi(weight_kg, height_meters)
    return classify_bmi(bmi)

def main():
    """Prompts user for input and displays BMI category."""
    try:
        weight = float(input("Enter your weight in pounds: "))
        height_ft = int(input("Enter your height in feet: "))
        height_in = int(input("Enter additional inches: "))

        bmi_category = calculate_bmi(weight, height_ft, height_in)
        print(f"Your BMI category is: {bmi_category}")

    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
