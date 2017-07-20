num = int(input("Enter how many items: "))
sum = 0
for i in range(num):
    price = float(input("Enter price for item: "))
    sum += price

if sum > 100:
    total = sum * 0.9
    print(total)
else:
    print(sum)

