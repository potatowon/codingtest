def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return str(r)
    else:
        return convert(q, base) + str(r)

# 소수 판별
def primenumber(x):
    if x == 0 or x == 1:
        return False
    for i in range (2, int(x**0.5) + 1):	
    	if x % i == 0:		
        	return False
    return True				
def solution(n, k):
    k_num = convert(n, k)
    k_num.split('0')
    answer = 0
    for i in k_num.split('0'):
        if i != '' and primenumber(int(i)):
            answer += 1
    return answer
            
            
            
            

    
    
     