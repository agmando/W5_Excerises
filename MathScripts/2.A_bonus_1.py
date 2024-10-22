assets = float(input("What are your total assests? "))
debts = float(input("What is your total debt? "))

net_worth = assets - debts

print(f"Your net worth is ${net_worth:.2f}")