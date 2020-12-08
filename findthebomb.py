# Create a function that finds the word "bomb" in the given string. If found, return "Duck!!!", otherwise, return "There is no bomb, relax.".

# "bomb" may appear in different cases (i.e. uppercase, lowercase, mixed).
def bomb(txt):
	if "bomb" in txt.lower():
		return "Duck!!!"
	else:
		return "There is no bomb, relax."