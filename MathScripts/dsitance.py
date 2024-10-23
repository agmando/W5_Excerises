import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

z = (x1,y1)
y = (x2,y2)

print(math.dist(z,y))