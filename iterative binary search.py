def binary_iterative(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high)//2

        if lst[mid] == key:
            return True
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(binary_iterative([1, 5, 11, 14, 22, 25, 26, 31, 38, 50, 77], 45))