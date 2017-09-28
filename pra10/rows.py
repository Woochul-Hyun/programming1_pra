def get_rows(n):
    if n == 1:
        return 1
    else:
        return n + get_rows(n-1)

print("Youn need {} blocks".format(get_rows(6)))