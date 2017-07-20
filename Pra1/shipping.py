num = float(input("Enter how many items: "))
price = float(input("Enter price: "))

total = num * price

if total > 100:
    result = total * 0.9
    print(result)
else:
    print(total)