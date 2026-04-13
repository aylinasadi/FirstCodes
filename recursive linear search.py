def linear_search(list, key, i=0):
    if len(list) <= i:
        return False
    
    elif list[i] == key:
        return True
    
    return linear_search(list, key, i+1)
    

print(linear_search(['A', 'B', 'C', 'D', 'E'], 'B'))