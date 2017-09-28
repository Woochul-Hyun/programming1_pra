"""
Download the csv file from week 9 learnjcu and save it as sales.csv in your working directory.
Write a program with the following requirements:
1. A class called House with 3 attributes (br, sqft, price)
2. Use with and csv reader to read the sales.csv
3. Process the data, must make use of object created from House, and print out:
    The average price per square feet for 3 bedroom
"""

import csv


class House:
    def __init__(self, br, sqft, price):
        self.br = br
        self.sqft = sqft
        self.price = price

    def __str__(self):
        return "This house is {} bedder {} sqft @ ${}".format(self.br, self.sqft, self.price)


def process_file_reading(filename):
    data = []
    with open(filename, "r") as file_obj:
        csv_pointer = csv.reader(file_obj)
        count = 0
        for row in csv_pointer:
            count += 1
            if count == 1:
                continue
            house_obj = House(row[4], row[6], row[9]) #object instantiation
            data.append(row)
            print(house_obj)
    return data

def get_average(houses, num_of_bed):
    total_price = 0
    total_sqft = 0
    #print("num_of_bed = ", num_of_bed)
    for each in houses:
        #print(each.br, int(each.br) == num_of_bed)
        if each.br == num_of_bed:
            total_price += int(each.price)
            total_sqft += int(each.sqft)
            print("adding", each)
    print("THe average price for {} bedder is ${:.f}".format(num_of_bed, total_price/total_sqft))


def main():
    FILENAME = "sales.csv"
    data = process_file_reading(FILENAME)
    get_average(data, 3)


main()