"""
Get into your preferred group, and work on the following:
1. Construct a read_file() mrthod that reads in a string input as filename then
return the list of data from file.
   def read_file(filename):
       .........
       return data
   calling:
       data = read_file("data.txt")
       data[0] = "2005-Q1, 0.00062"
2. Second function that cleans up the data.
   def clean_up(data):
       return data

    calling:
       data = clean_up(data)
       data[0] = ["2005", "Q1", 0.00062]
3. finally display all data from main()

"""

def read_file():
    data = open("mobile-data-usage.csv", "r")
    data.remove(data[0])
    print(data)
    return data


def clean_up(data):
    for each in data:
        split_data = data.strip("-")
        split_data2 = split_data[0].split(",")
    return data


def main():


    FILENAME = "mobile-data-usage.csv"
    data = read_file()
    data = clean_up(data)
    print(split_data) # [[2005, "Q1", 0.00062], [2005, "Q1", 0.00062]]

main()