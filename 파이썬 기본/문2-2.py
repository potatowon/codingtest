def max_index(lst):
    max_val = lst[0]
    for idx, num in enumerate(lst):
        if num >= max_val:
            max_val = num
            index = idx
    return index

print(max_index([1,2,3,4,10]))