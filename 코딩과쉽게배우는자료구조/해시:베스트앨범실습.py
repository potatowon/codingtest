'''
가장 많이 재생된 노래 2개씩 모아 베스트 앨범 출시
노래는 고유번호로 구분 ; hash 값

1. 속한 노래가 많이 재생된 장르 수록
2. 장르 내에서 많이 재생된 노래
3. 장르 내에서 재생횟수가 같으면 고유번호가 낮은 노래
'''
def solution(genres, plays):
    answer = []
    # {장르: [(재생 횟수, 고유 번호), ...]} 형태로 딕셔너리 생성
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [(plays[i], i)]
        else:
            genre_dict[genres[i]].append((plays[i], i))
    # print(genre_dict)
    # 재생 횟수 합이 큰 장르 순으로 정렬
    sorted_genre = sorted(list(genre_dict.keys()), key=lambda x: sum(play[0] for play in genre_dict[x]), reverse=True)
    for genre in sorted_genre:
        # 재생 횟수가 큰 노래부터 2개씩 선택
        genre_dict[genre].sort(key=lambda x: (-x[0], x[1]))
        for i in range(min(2, len(genre_dict[genre]))):
            answer.append(genre_dict[genre][i][1])

    return answer
