from collections import defaultdict
def rod(num, x):
    if num % x == 0:
        return num//x
    else:
        return (num//x) + 1

def solution(fees, records):
    answer = []
    park_sum = defaultdict(int)
    park = dict()
    for r in records:
        t, n, h = r.split()

        if h == "IN":
            park[n] = t
        elif h == "OUT":
            time = (int(t[:2]) - int(park[n][:2])) * 60 + (int(t[-2:]) - int(park[n][-2:]))
            park_sum[n] += time
            del park[n]
    if park:
        for k, v in park.items():
            time = (23 - int(v[:2])) * 60 + (59 - int(v[-2:]))
            park_sum[k] += time
    numbers = sorted(list(park_sum.keys()))
    park_ssum = {k: park_sum[k] for k in numbers}
    for n, t in park_ssum.items():
        if t <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + rod((t- fees[0]), fees[2])*fees[3]
            answer.append((fee))
    return answer