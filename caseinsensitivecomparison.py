# Write a function that validates whether two strings are identical. Make it case insensitive.

def match(s1, s2):
	return s1.casefold() == s2.casefold()