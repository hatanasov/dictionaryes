string = input()

char_count = {}

for char in string:
    if not char in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

for key, value in char_count.items():
    print(key, '->', value)