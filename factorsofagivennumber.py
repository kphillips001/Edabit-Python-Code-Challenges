# Create a function that finds each factor of a given number n. Your solution should return a list of the number(s) that meet this criteria.

# Notes
# Return an empty list if the given number is less than 1.
def find_factors(n):
	return [i for i in range(1, n + 1) if n % i==0]