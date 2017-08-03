filename = str(input("Enter a filename:"))

try:
    my_file = open(filename, "r")
    print(my_file.readline())
    my_file.close()
except FileNotFoundError:
    print("File not found")
except:
    print("Generic except")