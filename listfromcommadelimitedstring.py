# Write a function that turns a comma-delimited list into an array of strings.
def to_array(txt):
	return txt.split(', ') if txt else []