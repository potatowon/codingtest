def is_acceptable(password):
    모음 = "aeiou"
    모음여부 = False
    연속_모음 = 0
    연속_자음 = 0
    prev_char = None

    for char in password:
        # 모음 여부 판단
        if char in 모음: # 모음인경우 모음 추가
            모음여부 = True
            연속_모음 += 1
            연속_자음 = 0
        else: # 자음인 경우 자음추가
            연속_자음 += 1
            연속_모음 = 0
        
        # 연속 판단
        if 연속_모음 == 3 or 연속_자음 == 3:
            return False
        
        # 같은 문자인경우 판단
        if char == prev_char:
            if char != 'e' and char != 'o':
                return False
        
        prev_char = char
    
    # 모음 여부 판단 반환
    return 모음여부

while True:
    password = input()
    if password == 'end':
        break
    
    if is_acceptable(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
