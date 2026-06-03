def count_words(file, word):
    try:
        f = open(file, 'r')
        total_words = 0
        for line in f.read().splitlines():
            words = line.strip().split()
            total_words += len(words)
        f.close()
        return total_words

    except FileNotFoundError:
        return "file does not exsist"

print(count_words(input("enter the name of the file: ")))
