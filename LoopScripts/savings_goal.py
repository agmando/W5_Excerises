bank_balance = 100  
savings_goal = 1000  
weekly_savings = 50  


while bank_balance < savings_goal:
    bank_balance += weekly_savings
    if bank_balance >= savings_goal * 0.75:
        bank_balance -= 10  # Treating yourself costs $10
        print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}.")
    elif bank_balance >= savings_goal * 0.5:
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}.")
    else:
        print(f"This week my balance increased to ${bank_balance:.2f}.")

print(f"Goal met! My current balance is ${bank_balance:.2f}.")
