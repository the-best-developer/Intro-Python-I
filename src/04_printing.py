"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

def print_mod_string():
    print('x is %(x)s, y is %(y)s, z is "%(z)s"' % {"x": x, "y": round(y, 2), "z": z})

print_mod_string()

# Use the 'format' string method to print the same thing

def print_dot_format_string():
    print('x is {0}, y is {1}, z is "{2}"'.format(x, round(y, 2), z))

print_dot_format_string()

# Finally, print the same thing using an f-string

def print_f_string():
    print(f'x is {x}, y is {round(y, 2)}, z is "{z}"')

print_f_string()
