# Defining a function
def greet(name):
    print(f"Hello, {name}! Welcome to Data Engineering")


# Calling the function
greet("John")


# Function with return value
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 7)
print("Sum: ", result)


# Function with default parameters
def introduce(name, role="Data Engineer"):
    print(f"My name is {name} and I am {role}.")


introduce("John")
introduce("Alex", role="Data Analyst")


# Function to check if it's even or odd
def check_number(a):
    if a % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


check_number(598)


# Function that takes a list of numbers and return the sum
def sum_of_list(a):
    result = 0
    for i in a:
        result = result + i
    return result

list = [2, 6, 2, 8]
result = sum_of_list(list)
print(f"Sum of list {list} is {result}")
