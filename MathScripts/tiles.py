length = float(input("Enter room length in feet: "))
width = float(input("Enter room width in feet: "))

area = length * width

boxes_needed = area / 12

total_boxes = boxes_needed * 1.10

import math
total_boxes = math.ceil(total_boxes)

print(f"You will need {total_boxes} boxes of tiles.")
