def is_isogram(word):
    word = word.lower()

    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
             return False

    return True
   

text = input("Введіть слово: ")

if is_isogram(text):
    print("Слово є ізограмою")
else:
    print("Слово не є ізограмою")