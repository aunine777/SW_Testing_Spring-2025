#Aunine Livingston 
#asl358
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
    """Returns the BMI category based on the correct boundaries."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:  #  Ensure BMI 18.5 is "Normal weight"
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:  #  Ensure BMI 25.0 is "Overweight"
        return "Overweight"
    else:
        return "Obese"



#After catching the boundary shift problems I needed to debug.
def calculate_bmi(weight, height_ft, height_in):
    weight_kg = convert_weight_to_kg(weight)
    height_meters = convert_height_to_meters(height_ft, height_in)
    bmi = round(weight_kg / (height_meters ** 2), 1)

    # Debug print statement
    print(f"DEBUG: Weight={weight}, Height={height_ft}'{height_in}\" -> BMI={bmi} -> Category={classify_bmi(bmi)}")

    return classify_bmi(bmi)
    return round(weight_kg / (height_meters ** 2), 1)
    #return weight_kg / (height_meters ** 2)  # Avoid early rounding



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
