# A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to people 18 and older and when he's not on break.

# Given the person's age, and whether break time is in session, create a function which returns whether he should serve drinks.

def should_serve_drinks(age, on_break):
	return age >= 18 and not on_break