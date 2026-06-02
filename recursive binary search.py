def recursive_binary(lst, key):
    if len(lst) == 0:
        return False
    
    mid = len(lst)//2
    if key == lst[mid]:
        return True
    elif key > lst[mid]:
        return recursive_binary(lst[mid+1:], key)
    else:
        return recursive_binary(lst[:mid], key)
    
print(recursive_binary([1, 5, 11, 14, 22, 25, 26, 31, 38, 50, 77], 38))