# def gcd_(a, b):
#   if b == 0:
#     return a
#   else:
#     return gcd_(b, a%b)
#
# print(gcd_(1071, 1029))
#
# a, b = 1071, 1029
#
# while b != 0 :
#   a, b = b, a%b
#
# print(a)

def solution(n, m):
  a = max(n, m)
  b = min(n, m)
  while b != 0:
    a, b = b, a % b
  gcd_ = a
  lcm = gcd_ * (n / gcd_) * (m / gcd_)
  return [gcd_, lcm]