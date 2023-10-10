from itertools import combinations

def get_ability_diff(ability, team_start):
    n = len(ability)
    team_link = [i for i in range(n) if i not in team_start]
    
    ability_start = sum(ability[i][j] + ability[j][i] for i, j in combinations(team_start, 2))
    ability_link = sum(ability[i][j] + ability[j][i] for i, j in combinations(team_link, 2))
    
    return abs(ability_start - ability_link)

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
players = [i for i in range(n)]

min_diff = float('inf')

for team_start in combinations(players, n // 2):
    diff = get_ability_diff(ability, team_start)
    min_diff = min(min_diff, diff)

print(min_diff)
