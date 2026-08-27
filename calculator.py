""" Build a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division. 
The calculator should take two numbers and an operator as input from the user and display the result of the operation."""
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %, **): ")
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b
elif operator == '%':
    result = a % b
elif operator == '**':
    result = a ** b
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /, %, **")
print("The result of {} {} {} = {}".format(a, operator, b, result))    