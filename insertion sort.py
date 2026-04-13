def insertion_sort(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > item:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item

    return lst

print(insertion_sort([7, 1, 5, 9, 11, 2, 15, 3]))