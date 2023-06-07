# Nested Loops

# Printing out numbers 0-9 in every combination and
# multiplying them
# Hint: You will have to do something like this for the
# multiplication tables assigment
for i in range(10):
    for j in range(10):
        print(i, j)
        print(i * j)

# Iterating through a 2D List
my_list = [[10, 23, 2, 5, 453], [45, 85, 11, 25], [56, 79, 80]]

for i in my_list:
    for j in i:
        print(j)

# Comparing the values between two lists
a = [13, 856, 12, 45, 84]
b = [854, 201, 43, 84, 20]

common_values = []

for i in a:
    for j in b:
        if i == j:
            common_values.append(i)

print(common_values)
