# Given a sandwich (as a list), return a list of fillings inside the sandwich. This involves ignoring the first and last elements.
# The first and last elements will always be "bread".
def get_fillings(sandwich):
  return sandwich[1:-1]