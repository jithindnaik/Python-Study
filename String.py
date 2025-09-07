string_of_text = "This is an example"

# String Printing
print(string_of_text[0]) #  T
print(string_of_text[1]) #  h
print(string_of_text[2]) #  i
print(string_of_text[3]) #  s
print(string_of_text[4]) #
print(string_of_text[5]) #  i
print(f"String length is {len(string_of_text)}")  #  String length is 18
print(f"The last character is '{string_of_text[len(string_of_text) - 1]}'") # The last character is 'e'

# String Slicing
print(string_of_text[:3]) # Thi
print(string_of_text[0:6]) # This i
print(string_of_text[4:6]) #  i

#String Concatenation
new_string = "This is additional text"
concatenated_string = string_of_text + "," + new_string
print(concatenated_string)

