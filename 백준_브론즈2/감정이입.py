b1 = input().strip()
b2 = input().strip()

answer = bin(int(b1, 2)*int(b2, 2))[2:]

print(answer)

