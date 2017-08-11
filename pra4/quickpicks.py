import random

num_list = []
user_input = int(input("Enter number of picks:"))

for num in range(user_input):
    nums = []
    while len(nums) < 6:
        rand = random.randint(0, 45)
        while random in nums:
            rand =random.randint(0, 45)
        nums.append(rand)

    nums.sort()
    print(nums)


