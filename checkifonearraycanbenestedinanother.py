# Create a function that returns True if the first list can be nested inside the second.

# list1 can be nested inside list2 if:

# list1's min is greater than list2's min.
# list1's max is less than list2's max.


# Notes
# Note the strict inequality (see example #3).
def can_nest(list1, list2):
	return min(list1) > min(list2) and max(list1) < max(list2)