def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2


if __name__ == "__main__":
    # Get two numbers from user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the numbers
    result = add_numbers(num1, num2)

    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")

    # Subtract the numbers
    difference = num1 - num2
    print(f"The difference of {num1} and {num2} is: {difference}")
