'''
6과 9가 호환이 된다는 점을 인지할것.
'''

room_number = input().strip()
counter = [0]*10

for digit in room_number:
    if digit == '6' or digit == '9':
        # 6과 9는 동일한 숫자로 간주
        counter[6] += 0.5  # 각각 0.5로 취급하여 한 세트에서 두 번 사용 가능하다는 것을 표현
    else:
        counter[int(digit)] += 1

print(int(max(counter)+0.9))  # 최대 필요 세트 수를 출력 (소수점 이하 올림)
