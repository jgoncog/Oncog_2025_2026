#output by Josue Ruch III G. Oncog

# Get the unit of measurement from the user and convert it to capitalized format
unit = input("Enter a unit of measurement for temperature ( Fahrenheit, Celsius, Kelvin ) : ").capitalize()

# Check if the entered unit is valid (Celsius, Fahrenheit, or Kelvin)
if unit not in ["Celsius","Fahrenheit","Kelvin"]:
    print ("INVALID unit")  # Print an error message if the unit is invalid
    exit()  # Exit the program

# Get the temperature from the user
temperature = input("Enter temperature in chosen measurement: ")

# Try to convert the temperature to a floating-point number
try:
    temperature = float(temperature)
except ValueError:
    print("Invalid temperature input. Please enter a number.")  # Print an error message if the input is not a number
    exit()  # Exit the program

# Convert the temperature to Celsius based on the unit
if unit == "Fahrenheit":
    celsius = (temperature - 32) * 5 / 9  # Fahrenheit to Celsius conversion formula
elif unit == "Kelvin":
    celsius = temperature - 273.15  # Kelvin to Celsius conversion formula
else:
    celsius = temperature  # If the unit is Celsius, no conversion is needed

# Define a function to check the temperature range and return a message
def check_temperature(celsius):
    if celsius < 0:
        return "Too cold!"  # Return "Too cold!" if the temperature is below 0 Celsius
    elif 0 <= celsius <= 35:
        return "Safe temperature."  # Return "Safe temperature." if the temperature is between 0 and 35 Celsius
    else:
        return "Too hot!"  # Return "Too hot!" if the temperature is above 35 Celsius

# Call the check_temperature function with the calculated Celsius value and print the returned message
print(check_temperature(celsius))
