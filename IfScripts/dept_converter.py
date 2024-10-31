# dept_converter.py
code = int(input("Enter department code: "))

if code == 1:
    department = "Marketing"
elif code == 5:
    department = "Human Resources"
elif code == 10:
    department = "Accounting"
elif code == 12:
    department = "Legal"
elif code == 18:
    department = "IT"
elif code == 20:
    department = "Customer Relations"
else:
    department = "Unknown Department"

print(f"Department: {department}")
