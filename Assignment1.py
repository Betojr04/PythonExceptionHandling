"""
Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
"""

# temp = input("Please enter the temperature in Fahrenheit: ")

"""
Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
"""


def celsius_conversion(temp):
    conversion = (temp - 32) * 5 / 9
    return conversion


"""
Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
"""

while True:
    try:
        user_input = float(input("Enter Fahrenheit temperature: "))

    except ValueError as e:
        print("Invalid input, please enter a valid number.")

    else:
        print(
            f"{user_input} degrees Fahrenheit is {celsius_conversion(user_input):.2f} degrees Celsius"
        )
        break


"""
Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
"""


def celsius_conversion(temp):
    conversion = (temp - 32) * 5 / 9
    return conversion


while True:
    try:
        user_input = float(input("Enter Fahrenheit temperature: "))

    except ValueError as e:
        print("Invalid input, please enter a valid number.")

    else:
        print(
            f"{user_input} degrees Fahrenheit is {celsius_conversion(user_input):.2f} degrees Celsius"
        )

    finally:
        continue_input = input(
            "Would you like to perform another conversion? (yes/no): "
        ).lower()
        if continue_input == "no":
            print("Thank you for using the converter!")
            break
