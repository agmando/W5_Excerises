student_name = input("Enter student name: ")
student_major = input("Enter student major code (e.g., ENG): ")

if student_major == "ENG":
    major_name = "English"
    location = "Kerr Hall, Room 201"
elif student_major == "BIOL":
    major_name = "Biology"
    location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    location = "Sheppard Hall, Room 314"
elif student_major == "HIST":
    major_name = "History"
    location = "Kerr Hall, Room 114"
else:
    major_name = "<unknown>"
    location = ""

print(f"Student: {student_name}")
print(f"Major: {major_name}")
print(f"Department Location: {location}")
