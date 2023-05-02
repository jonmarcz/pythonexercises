# ask the user for a number
user_input = input("Enter a number: ")

# try to convert the input to a float
try:
    number = float(user_input)
except ValueError:
    # if the input cannot be converted to a float, try to convert to an integer
    try:
        number = int(user_input)
    except ValueError:
        # if the input cannot be converted to an integer, print an error message
        print("Error: Invalid input. Please enter a number.")
    else:
        print("You entered an even number:", number)
else:
    print("You entered an odd number:", number)
