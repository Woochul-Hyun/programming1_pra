import random

try:
    user_input = input("Enter 3 values separated by comma: ")
    datum = user_input.split(",")
    count = 0
    while count <3:
        print(datum[count])
        count += 1
except IndexError:
    print("Data insufficient")



input_flag = True
while input_flag:
    try:
        user_input = input("Enter 3 values separated by comma: ")
        datum = user_input.split(",")
        count = 0
        while count < 3:
            print(datum[count])
            count += 1
        input_flag =False
    except IndexError:
        print("Data insufficient")



def get_food(num):
    foods = ["Sandwich", "Burger", "Fried Chicken", "Udon noodle", "Fried Rice"]
    ret_food = []
    for i in range(num):
        ret_food.append(foods[random.randint(0, len(foods)-1)])
    return ret_food


def get_day(num): #0
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    num = 4
    return days[num] #0

#Sharing mutable vs immutable
org_num = 2
print(get_day(org_num))
print(org_num)

def get_day_v2(num, days): #0
    return days[num]

#Sharing mutable vs immutable
org_num = 2
print(get_day(org_num))
print(org_num)

num_v2 = 3
days_v2 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print(get_day_v2(num_v2, days_v2))
print(days_v2)


