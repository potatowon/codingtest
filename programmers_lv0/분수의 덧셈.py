def solution(numer1, denom1, numer2, denom2):
    a =  max(denom1, denom2)
    b =  min(denom1, denom2)
    while b != 0:
        a, b = b, a%b
    gcd_ = a

    lcm = gcd_ * (denom1//gcd_) * (denom2//gcd_)

    numer = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))
    
    c = max(numer, lcm)
    d = min(numer, lcm)
    while d != 0:
        c, d = d, c%d
    
    return [numer//c, lcm//c]