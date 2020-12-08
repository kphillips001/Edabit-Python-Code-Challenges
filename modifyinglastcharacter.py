# Create a function which makes the last character of a string repeat n number of times.

def modify_last(txt, n):
    return txt[:-1] + txt[-1] * n