# def solution(A, B):
#     answer = 0
#     for a in A:
#         res = []
#         for b in B:
#             if b > a:
#                 res.append(b)
#         if len(res) >= 1:
#             answer += 1
#             B.remove(min(res))
        
#     return answer

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    j = 0
    for i in range(len(A)):
        while j < len(B):
            if B[j] > A[i]:
                answer += 1
                j += 1
                break
            j += 1
                
    return answer
