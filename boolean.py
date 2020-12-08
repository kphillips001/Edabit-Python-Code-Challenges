# Check the principles of minimalist code in the intro to the first challenge.

# In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section down below.

# Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.

# Tips
# Converting a boolean, or something that will ultimately be interpreted as a boolean, into a boolean is redundant.

# start of code
def parity(n):
	remander = bool(n % 2)
	if remainder == False:
		return "even"
	if remainder == True:
		return "odd"

# end of code
def parity(n):
		return 'even' if n % 2 == 0 else 'odd'