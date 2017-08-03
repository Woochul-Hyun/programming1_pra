def grade(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(score)
    print("Your grade is: {}" .format(grade(score)))

main()