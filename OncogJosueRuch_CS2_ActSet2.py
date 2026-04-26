# OncogJosueRuch_CS2_ActSet2.py
# Activity Set 2: Class Directory Builder (Using List of Dictionaries)

# Step 1: Create an empty list
students = []

# Step 2: Use a loop to collect data for 3 students
for i in range(3):
   
    student = {}  # Create a new dictionary for each student
    student["name"] = input("Enter name: ")
    student["age"] = input("Enter age: ")
    student["grade"] = input("Enter grade: ")
    print()
    students.append(student)  # Add the dictionary to the list

# Step 3: Print the class directory
print("\nClass Directory:")
for student in students:
    print(f"    {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

# <3 Additional stuff I learned in the module <3

# Show all student records as dictionaries
print("Student records: ")
print(students)


#Happy New Year Sir (Hope Danielle’s okay =[   )