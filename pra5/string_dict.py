user_input = {}
text = input("Text: ")
words = text.split()

for word in words:
    user_input1 = user_input.get(word, 0)

    if user_input1 not in user_input:
        user_input[word] = 1
    else:
        user_input[word] += 1


words = list(user_input.keys())
words.sort()
max_length = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, max_length, user_input[word]))
