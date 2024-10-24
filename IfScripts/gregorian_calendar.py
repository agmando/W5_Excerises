year = int(input("input a year "))

if year % 100 == 0:
    year % 400 == 0
    year % 4 == 0
    print(f"The year {year} is a leap year") 
else: 
    print(f"The year {year} is not a leap year")
     
     
