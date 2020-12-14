# Character recognition software often makes mistakes when documents (especially old ones written with a typewriter) are digitized.

# Your task is to correct the errors in the digitized text. You only have to handle the following mistakes:

# A is misinterpreted as 4
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def keyboard_mistakes(txt):
	txt = txt.replace("4", "A")
	txt = txt.replace("5", "S")
	txt = txt.replace("0", "O")
	txt = txt.replace("1", "I")
	return txt