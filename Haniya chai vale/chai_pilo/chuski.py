menu = {
    'simpal chai':20,
    'masala chai':40,
    'kada chai':60,
    'zingali chai':70,
    'kullhad chai':80,
    'goinga chai':100
}

print("welcome to haniya chai vala")
print("simpal chai: rs20\nmasala chai: rs40\nkada chai: rs60\nzingali chai: rs70\nkullhad chai: rs80\ngoinga chai: rs100")

order_total = 0

chai = input("enter the name of your order = ")
if chai in menu:
    order_total += menu[chai]
    print(f"your chai {chai} has been ordered")

else:
    print(f"your chai {chai} is not availabal")

print(f"total amount of your {order_total}")

feedback = input("do you like our chai (yes/No)")
if feedback == "yes":
   print("thanks for visiting haniya chai vala")

else:
   print("Exit gate par aapko ek paper milega aur aapko kya achha nhi laga vo likh kar apni pichh vade me dal le THANK YOU")