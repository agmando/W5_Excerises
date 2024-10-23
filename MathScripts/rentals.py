import math

seats_per_van = 15
cost_per_van = 250.00

tourists = int(input("How many people will be attending? "))

vans_needed = math.ceil(tourists/seats_per_van)

total_cost = vans_needed * cost_per_van

cost_per_person = total_cost/tourists

print(f"Vans needed: {vans_needed}")
print(f"Total cost to rent: {total_cost:.2f}")
print(f"Cost per person: {cost_per_person:.2f}")
