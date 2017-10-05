"""
Given:
subjects= {"CP1401": (60, 70, 80),
           "CP1404": (70, 80, 90)}
print the above data with string formatting like the following:
    CP1401       60%        70%        80.00%

"""

def print_marks(subjects={"dummy", (0, 0, 0)}):
    for key, value in subjects.items():
        print("{:^15}{:>10d}%{:>10d}%{:10.2f}%".format(key, value[0], value[1], value[2]))

subjects= {"CP1401": (60, 70, 80),
           "CP1404": (70, 80, 90)}
print_marks(subjects)