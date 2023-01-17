babbling = 	["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
word = ["aya", "ye", "woo", "ma"]
cnt = 0
for b in babbling:
    for i in word:
        b = b.replace(i, ',')
    if (b == ',') or(b == ',,') or (b ==',,,') or(b == ',,,,'):
        cnt += 1
a = babbling[0].replace(word[3], '')


