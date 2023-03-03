arr = [1, 1, 5, 124, 400, 599, 1004, 2876, 8712]

def binary_search(array, find_value):
    left = 0 # start
    right = len(array) - 1
    mid = (left + right) // 2

    while left < right:
        if array[mid] == find_value:
            return mid
        
        if array[mid] < find_value:
            left = mid + 1

        else:
            right = mid - 1

        mid = (right + left) // 2

    return -1
    
# result

print(binary_search(arr, 2876))
