
def get_oldest():
    names = ["John", "Amy", "Ann"]
    ages = [20, 40, 30]
    oldest_person = names[ages.index(max(ages))]
    print(oldest_person)
    return oldest_person



def main():
    oldest_person = get_oldest()

main()