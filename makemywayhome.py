# You will be given a list, showing how far James travels away from his home for each day. He may choose to travel towards or away from his house, so negative values are to be expected.

# Create a function which calculates how far James must walk to get back home.

def distance_home(lst):
	return abs(sum(lst))