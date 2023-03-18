
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
a = 5
c= 1

# b = lambda x: x + a * c

b = lambda x, y, z: x * y + z

# print(b(2,5,4))

def my_func(n):
    return lambda x: x + n

first_number = my_func(2)
second_number = my_func(4)

total_one = first_number(5)
total_two = second_number(2)

print(total_one, total_two)