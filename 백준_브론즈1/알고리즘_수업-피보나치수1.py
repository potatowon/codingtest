def recursive_fib(n):
    if n == 1 or n == 2:
        return 1, 1  # 코드1 실행 횟수를 반환
    fib_n_minus_1, count1 = recursive_fib(n - 1)
    fib_n_minus_2, count2 = recursive_fib(n - 2)
    return fib_n_minus_1 + fib_n_minus_2, count1 + count2


def dynamic_fib(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2 실행

    return f[n], n - 2  # 코드2는 n-2번 실행됩니다


n = int(input())
_, code1_count = recursive_fib(n)
_, code2_count = dynamic_fib(n)
print(code1_count, code2_count)
