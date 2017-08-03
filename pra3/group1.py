def get_password():
    password = input("Enter your password: ")
    return password

def print_to_file(encoded_password):
    out_file = open("secret.txt", "w")
    print(encoded_password, file=out_file)
    out_file.close()


def encode(password):
    encoded_password =""
    for each in range(len(password)):
        if each != len(password)-1:
            encoded_password += str((ord(password[each]) -65)*2) +","
        else:
            encoded_password += str((ord(password[each]) -65)*2)
    return encoded_password


def main():
    password = get_password()
    encoded = encode(password)
    print_to_file(encoded)
    
main()