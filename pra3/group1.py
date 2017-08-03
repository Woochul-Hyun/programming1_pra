def get_password():
    password = input("Enter your password: ")
    return password


def endcode(password):
    encoded_password =""
    for each in range(len(password)):
        if each != len(password)-1:
            encoded_password += ((ord(password[each]) -65)*2) +","
        else:
            encoded_password += str((ord(password[each]) -65)*2)
        return encoded_password

def print_to_file(encoded_password):
    out_file = open("secret.txt", "w")
    print(encoded_password, file=out_file)
    out_file.close()

def main():
    pw = get_password()
    endcode = endcode(pw)
    print_to_file(encoded)

main()