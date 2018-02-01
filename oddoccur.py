words = input().split()

word_occur = {}

for word in words:
    word = word.lower()
    if word not in word_occur:
        word_occur[word] = 1
    else:
        word_occur[word] += 1

result = [word for word in word_occur if word_occur[word] % 2 == 1]

print(*result, sep=', ')