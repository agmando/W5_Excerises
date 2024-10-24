pay_rate = float(input("What is your hourly rate? "))
hours_worked = float(input("How many hours did you work? "))


if hours_worked <= 40:
    reg_pay = pay_rate * hours_worked
    print(f"Your total pay is {reg_pay}")
else:
    reg_pay = pay_rate * 40
    ot = hours_worked - 40
    ot_payrate = 1.5 * pay_rate
    ot_pay = ot * ot_payrate
    total_pay = reg_pay + ot_pay
    print (f"Your total pay is {total_pay}")
 



