# type(), str(), and escape sequences exercises
# Do all of this in a .py file in Pycharm.

# Create a variable and assign it a float

# Use print() and type() to print the data type of the variable in the output

# Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result

# print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)

float_val = 3.14
print(float_val) # 3.14
print(type(float_val)) # <class 'float'>

str_float_val = str(float_val) + " is a float"
print(str_float_val) # 3.14 is a float

print("\"Hello, I'm [Test], it's nice to meet you!\"") # "Hello, I'm [Test], it's nice to meet you!"
print('\"Hello, I\'m [Test], it\'s nice to meet you!\"') # "Hello, I'm [Test], it's nice to meet you!"

