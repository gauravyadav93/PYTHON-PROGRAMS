num_of_shoes = int(input())
shoe_list = [int(i) for i in input().split(" ")]
num_of_purchase = int(input())
total_value = 0 

for i in range(num_of_purchase):
    size, price = map(int, input().split(" "))
    if size in shoe_list:
        total_value += price
        shoe_list.remove(size)
        
print(total_value)