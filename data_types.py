# Different Data types
from tokenize import String

integer_num = 100
float_num = 99.99
string_text = 'Hello, Data Engineer'
boolean_val = True

# Type Conversion
num_str = '123'
converted_num = int(num_str) # Converting string to integer
print('Converted Number:', converted_num)

# Automatic Type Conversion
result = integer_num + float_num
print('Result of adding int and float:', result)

# Check Data Types
print(type(integer_num))
print(type(float_num))
print(type(string_text))
print(type(boolean_val))

# Converting float to string
str_float = 56.6
converted_string = str(str_float)
print('Result of converting string to float:', converted_string)

result_string = str(str_float) + string_text
print('Result of adding string to int and float:', result_string)