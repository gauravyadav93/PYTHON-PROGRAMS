#custmr_id, name, unit = int(input("enter customer id:-")), input("enter customer name:-"), int(input("enter customer unit:-"))
def electricity_bill(custmr_id, name, unit):
    if unit<=199:
        print("the total amount to pay by the customer:-", unit*1.20)
    elif 200<=unit<400:
        print("the total amount to pay by the customer:-", unit*1.50)
    elif 400<=unit<600:
        print("the total amount to pay by the customer:-", unit*1.80)
    else:
        print("the total amount to pay by the customer:-", unit*2.00)
electricity_bill(custmr_id = int(input("enter customer id:-")), name =  input("enter customer name:-"), unit = int(input("enter customer unit:-")))     
print(electricity_bill)
#electricity_bill(2345, "Gaurav", 45)

