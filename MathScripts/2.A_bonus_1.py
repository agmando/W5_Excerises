assets = float(input("What are your total assests? "))
debts = float(input("What is your total debt? "))

net_worth = assets - debts

print("Your net worth is " + format(net_worth, ".2f"))