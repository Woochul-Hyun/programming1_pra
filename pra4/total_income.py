def main():
    incomes = []
    month_with_earnings = int(input("How many months? "))

    for month in range(1, month_with_earnings + 1):
        income = float(input("Enter income for month {} : ".format(month_with_earnings)))
        incomes.append(income)

    result_of_imcome(incomes)

def result_of_imcome(incomes):

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
main()
