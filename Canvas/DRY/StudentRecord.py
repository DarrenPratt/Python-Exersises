# Step 1: Create a dictionary for a student record
student = {
    "name": "John Doe",
    "age": 21,
    "university": "University of Example",
    "major": "Computer Science"
}

# Step 2: Access and print the dictionary values with appropriate titles
print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("University:", student["university"])
print("Programme:", student["major"])
print()

# Step 3: Update the student's major
student["major"] = "Data Science"
print("Updated Programme:", student["major"])
print()

# Step 4: Add a new field for modules
student["modules"] = ["Maths", "Engineering"]
print("Modules:", student["modules"])
print()

# Step 5: Remove a key-value pair (e.g., removing the age field)
del student["age"]
print("Student record after removing 'age':", student)
print()

# Step 6: For loop to print each key
print("Keys in student record:")
for key in student:
    print(key)
print()

# Step 7: For loop to print each value
print("Values in student record:")
for value in student.values():
    print(value)
print()

# Step 8: For loop to print each key-value pair
print("Key-Value pairs in student record:")
for key, value in student.items():
    print(f"{key}: {value}")



'''
Using Functions
'''
# Step 1: Create the initial student dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "university": "University of Example",
    "major": "Computer Science"
}

# Function to print student information
def getStudentInfo():
    print("Student Details:")
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("University:", student["university"])
    print("Programme:", student["major"])
    print()

# Function to modify a student's data
def modifyStudentData(key, value):
    student[key] = value
    print(f"Updated {key.capitalize()}: {student[key]}")
    print()

# Function to remove a student's data
def removeStudentData(key):
    if key in student:
        del student[key]
        print(f"Removed '{key}' from student record.")
    else:
        print(f"'{key}' not found in student record.")
    print()

# Function to retrieve and print all key-value pairs in the dictionary
def getStudentData():
    print("Complete Student Record:")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")
    print()

# Step 2: Call getStudentInfo to display the initial student info
getStudentInfo()

# Step 3: Call modifyStudentData to update the student's major
modifyStudentData("major", "Data Science")

# Step 4: Add a new field for modules
modifyStudentData("modules", ["Maths", "Engineering"])

# Step 5: Call removeStudentData to remove 'age' from the student record
removeStudentData("age")

# Step 6: Call getStudentData to display the final student record
getStudentData()
