# 최빈값 구하기

def solution(array):
    array.sort()
    number_index = set(array)
    arr_dic = {idx : 0 for idx in number_index}
    if len(array) ==1:
        return array[0]
    for num in array:
        arr_dic[num] += 1
    result = sorted(arr_dic.items(), key=lambda x : x[-1], reverse=True)
    if len(result) <= 1:
        return result[0][0]
    return -1 if result[0][1] == result[1][1] else result[0][0]

print(solution([1,2,3,3,3,4]))
print(solution([1,1,2,2]))
print(solution([1]))