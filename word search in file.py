def count_word_occurrences(file, word):
    try:
        f = open(file, 'r')
        text = (f.read()).split()
        f.close()

        count = 0
        for t in text:
            if t == word:
                count += 1
        return count

    except FileNotFoundError:
        return "file does not exsist"

file = input("enter the name of the file: ")
word = input("enter the word to search for: ")
print(count_word_occurrences(file, word))