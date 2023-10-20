def solution(dirs):
    answer = 0
    visited = set()
    x, y = 5, 5
    for move in dirs:
        nx, ny = x, y
        if move == "U":
            ny += 1
        elif move == "D":
            ny -= 1
        elif move == "L":
            nx -= 1
        else:
            nx += 1

        if 0 <= nx < 11 and 0 <= ny < 11:
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))
                answer += 1
            x, y = nx, ny

    return answer
