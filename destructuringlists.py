# We can destructure lists like this:

# arr = ["1", "2", "3"]
# a, b, c = arr
# but what if the list has nested lists, like the following?

# arr = ["cars", "planes", ["trains", ["motorcycles"]]]

# trans1 = arr[0]
# trans2 = arr[1]
# trans3 = arr[2][0]
# trans4 = arr[2][1][0]

# println(trans1) # outputs "cars"
# println(trans2) # outputs "planes"
# println(trans3) # outputs "trains"
# println(trans4) # outputs "motorcycles"
# Can you use list destructuring to assign all four variables at once?





# arr = ["cars", "planes", ["trains", ["motorcycles"]]]

# # Fix the following using destructuring
# # Only edit what's inside of [ trans1, trans2, trans3, trans4 ]
# # this statement, as written, will cause a ValueError
# [ trans1, trans2, trans3, trans4 ] = arr

trans1 = arr[0]
trans2 = arr[1]
trans3 = arr[2][0]
trans4 = arr[2][1][0]

# '''
# print(trans1) # should output "cars"
# print(trans2) # should output "planes"
# print(trans3) # should output "trains"
# print(trans4) # should output "motorcycles"
# '''

