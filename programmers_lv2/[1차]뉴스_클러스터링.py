def solution(str1, str2):
    A, B =[], []
    for idx in range(len(str1)-1):
        a = str1[idx:idx+2]
        if a.isalpha():
            A.append(a.lower())
    for jdx in range(len(str2) - 1):
        b = str2[jdx:jdx+2]
        if b.isalpha():
            B.append(b.lower())
    if A == [] and B == []:
        return 65536*1

    real_union = list(set(A) | set(B))
    real_intersection = list(set(A) & set(B))

    deno = 0
    nume = 0
    for u in real_union:
        deno += max(A.count(u), B.count(u))
    for i in real_intersection:
        nume += min(A.count(i), B.count(i))


    answer = int((nume/deno)*65536)
    return answer

print(solution('FRANCE', 'french'))
print(solution('E=M*C^2', 'e=m*c^2' ))