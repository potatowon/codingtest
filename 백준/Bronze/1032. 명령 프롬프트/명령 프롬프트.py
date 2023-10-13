def find_pattern(file_names):
    pattern = list(file_names[0])

    for file_name in file_names[1:]:
        for i, char in enumerate(file_name):
            if pattern[i] != char:
                pattern[i] = '?'

    return ''.join(pattern)

n = int(input())
file_names = [input() for _ in range(n)]
pattern = find_pattern(file_names)

print(pattern)
