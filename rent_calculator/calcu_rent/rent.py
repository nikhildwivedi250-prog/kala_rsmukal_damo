rent = int(input("enter your flat rent = "))
food = int(input("enter the amount of food order = "))
electricity_spend = int(input("enter the total of electricity spend = "))
charge_par_unit = int (input("enter the charge per unit = "))
person = int(input("enter the number of persion living in flat = "))


total_bill = electricity_spend * charge_par_unit

output = (food + rent + total_bill) // person

print("each person will pay = ", output)