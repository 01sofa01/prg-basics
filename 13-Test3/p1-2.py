def f(word):
    length = len(word)
    list_of_words = []
    if length == 0:
        return ""
    else:
        for index in range(length):
            list_of_words.append(word[:index] + word[index].upper() + word[index + 1:])
        return '-'.join(list_of_words)
        

print(f("book"))