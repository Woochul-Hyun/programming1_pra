"""
Get user name
initialise counter to be 0
Loop through each character in the name
if the character is any of the "aeiou"
Increment a counter
Print out after looping the final string.
"""
username =str(input("Name:"))
counter =0
for each in username: # "B"
    if each in "aeiouAEIOU": #False
        counter +=1


print("Out of {} letters, {} has {} vowels".format(len(username), username, counter))





username ="Bobby McAardvark"
#username[0] = "z" #string is immutable

my_list =[11, 22, 33, 44, 55, 1, 5, 90, 45] # a list of integer number
print(my_list[-1])
print(my_list[1:])
print(my_list[1:4])
#my_list[0] = 100 # mutable feature of list, list can be changed
print(my_list)

# max(), min(), len(), sum(), sort()
print("max is : {}".format(max(my_list)))
print("min is : {}".format(min(my_list)))
print("len is : {}".format(len(my_list)))
print("sum is : {}".format(sum(my_list)))
print("average: {}".format(sum(my_list) /len(my_list)))
my_list.sort() # mutable structure of list
print(my_list)


num_list =[] # use meaningful variable name, avoid using list

print(username)
print(list(username)) #separate data into list structure.

person1 =["John", 23, 1000.00]
person2 =["Amy", 18, 1500.00]
people =[person1, person2] # list of list
print(people)
print(people[1][1]) #people 안에서 1인 person2로 먼저 가서 그 안에서 1번인 18이 프린트됨

print(my_list +my_list)
print(my_list *3)

if 44 in my_list:
    print("yes")

for each in my_list:
    print(each)

for index, key in enumerate(my_list):
    print("{} -> {}".format(index, key))


my_list.append(999)
print(my_list)
my_list.pop() #()안에 아무것도 쓰지않으면 마지막값이 삭제
print(my_list)

num_list = [45, 1, 8, 90, 44]
new_list = sorted(num_list)
print(num_list)
print(new_list)