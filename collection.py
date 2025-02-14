# List Operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Updated list: ", numbers)

# Looping through a list
for num in numbers:
    print(num * 2)

# Dictionary Operations
student = {
    "name" : "John",
    "age" : 18,
    "course" : "Data Engineering"
}

# Accessing and Modifying Dictionary
print(student["name"])
student["age"] = 26
student['grade'] = 'A'

# Looping through a Dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# list of your favorite programming languages.
programming_lang = ["Python", "Swift", "SQL"]
print(f"My favourite language:  {programming_lang}")

# Make a dictionary for a book with keys like title, author, and year.
book = {
    "title": "Python Programming",
    "author": "Guido van Rossum",
    "year": 1960,
}

for key, value in book.items():
    print(f"{key}: {value}")