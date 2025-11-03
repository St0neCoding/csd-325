import json


# Load JSON data from student file
with open("student.json", "r") as f:
    students = json.load(f)

# Function to print the student list
def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

# Print the unchanged student list
print("Original Student List:")
print_students(students)

# Add myself to the list (with fake student ID and email)
students.append({
    "F_Name": "Stone",
    "L_Name": "Nettles",
    "Student_ID": 55555,  
    "Email": "snettles@gmail.com"
})

# Print the edited list
print("Updated Student List:")
print_students(students)

# Save the list additions to the JSON file
with open("student.json", "w") as f:
    json.dump(students, f, indent=4)

print("The student.json file has been updated.")
