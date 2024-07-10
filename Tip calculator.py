print("Welcome to Tip Calculator")
bill=float(input("What was the Total bill $"))
tip=int(input("How much tip would you like to give 10,12 or 15?"))
people=int(input("How many people to split the bill"))
tip_percent= tip/100
total_tip=bill*tip_percent
total_bill=total_tip +bill
split_bill= total_bill/people
Finalamount=round(split_bill,2)
print(f"Each person should pay ${Finalamount}")