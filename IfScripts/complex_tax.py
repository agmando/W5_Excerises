# complex_taxes.py
weekly_hours = float(input("Enter weekly hours worked: "))
pay_rate = float(input("Enter hourly pay rate: "))
filing_status = input("Enter filing status (single/joint): ")

annual_gross_pay = weekly_hours * pay_rate * 52

if filing_status == 'single':
    if annual_gross_pay < 9875:
        tax_rate = 0.10
    elif annual_gross_pay < 40125:
        tax_rate = 0.12
    elif annual_gross_pay < 85525:
        tax_rate = 0.22
    else:
        tax_rate = 0.24
elif filing_status == 'joint':
    if annual_gross_pay < 19750:
        tax_rate = 0.10
    elif annual_gross_pay < 80250:
        tax_rate = 0.12
    elif annual_gross_pay < 171050:
        tax_rate = 0.22
    else:
        tax_rate = 0.24
else:
    tax_rate = None

if tax_rate is not None:
    tax_withheld = annual_gross_pay * tax_rate
    print(f"Annual Gross Pay: ${annual_gross_pay:.2f}")
    print(f"Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Tax Withheld: ${tax_withheld:.2f}")
else:
    print("Invalid filing status.")
