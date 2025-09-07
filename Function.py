# sample function

def TestPython():
    print("This is a test function")


TestPython() # function call

# function arg

def addition(param1, param2):
    print(param1 + param2)


addition(3,5)

# default parameters on function

def default_param_addition(param1 = 0, param2 = 0):
    print(param1 + param2)


default_param_addition(3)

# function return

def product_of_two(param1, param2):
    return param1 * param2


print(product_of_two(8,2)) # 16

# default return from function is None