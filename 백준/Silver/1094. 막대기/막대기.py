from collections import deque
X = int(input())

pipe = [64]

while sum(pipe) > X:
    # print(pipe)
    pipe.sort(reverse=True)
    shorts = pipe.pop()
    new_pipe = shorts//2
    if new_pipe + sum(pipe) >= X:
        pipe.append(new_pipe)
    else:
        pipe.append(new_pipe)
        pipe.append(new_pipe)

print(len(pipe))