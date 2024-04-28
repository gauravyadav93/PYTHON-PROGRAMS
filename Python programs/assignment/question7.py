# write a python program to find a profit or loss for a tourist bus.
price_fuel = 70
mileage = 10
ticket_price = 80
no_passengers = int(input("enter the no. of passengers:- "))
distance_kms = int(input("enter the distance:- "))
collection = no_passengers*ticket_price
print(collection)
fuel_cost = (distance_kms//10)*price_fuel
print(fuel_cost)
if fuel_cost<collection:
    print("Profit")
else:
    print("Loss")