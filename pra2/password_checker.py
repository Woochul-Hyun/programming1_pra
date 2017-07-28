
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)



def is_valid_password(password):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        else:
            count_special += 1

    if len(password) < 5 or len(password) > 16:
        print ("Please check your password's length")
        return False
    elif count_upper > 0 and count_lower > 0 and count_digit > 0 and count_special > 0:
        print("Good")
        return True
    else:
        print("Please check your password includes 1 or more uppercase characters, "
              "lowercase characters, numbers, or special characters")
        return False



main()