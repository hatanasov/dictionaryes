real_nums = [num for num in input().split()]

counts = {}

for num in real_nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

for key, value in counts.items():
    print(key, '->', value, 'times')
