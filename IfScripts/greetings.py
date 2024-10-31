# greeting.py
hour = int(input("Enter the current hour (0-23): "))

if 0 <= hour < 4 or 23 <= hour < 24:
    greeting = "What are you doing up so late??"
elif 4 <= hour < 10:
    greeting = "Good morning!"
elif 10 <= hour < 17:
    greeting = "Good day!"
elif 17 <= hour < 23:
    greeting = "Good evening!"
else:
    greeting = "Invalid hour."

print(greeting)
