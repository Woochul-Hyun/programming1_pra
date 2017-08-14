def read_file():
    FILENAME = "mobile-data-usage.csv"

    file_pointer = open(FILENAME, "r")
    data = file_pointer.read().splitlines()
    data.remove(data[0])
    file_pointer.close()
    return data



def clean_file(data):

    for i in data:
        fixed_data = i.split()
        new_parts = i.split('-')
        new_parts2 = new_parts[1].split(',')
        new_data = [new_parts[0], new_parts2[0], new_parts2[1]]

        print(new_data)

    return new_data


def main():
    data = read_file()
    clean_file(data)
main()