n = int(input())
answer = 0
for i in range(n+1,n**2+1,n+1):
    answer += i

print(answer)