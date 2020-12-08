# Create a function that takes two numbers and a mathematical operator and returns the result.

# Notes
# Numbers can be negative.
# The only operations used are those in the examples above.
def calculate(num1, num2, op):
	return eval(str(num1) + op + str(num2))