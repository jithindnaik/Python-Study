# Do all of this in a .py file in Pycharm

# Create a variable and assign it the string "Just do it!"

# Access the "!" from the variable by index and print() it

# Print the slice "do" from the variable

# Get and print the slice "it!" from the variable

# Print the slice "Just" from the variable

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

var_str = "Just do it!"
print(var_str) # Just do it!

print(var_str[10]) # !
print(var_str[10:11]) # !

print(var_str[5:7]) # do

print(var_str[8:10]) # it

print(var_str[8:]) # it!

print(var_str[:4]) # Just

print("Don't " + var_str[5:]) # do it!
