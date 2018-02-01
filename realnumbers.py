from collections import OrderedDict

real_nums = [float(num) for num in input().split()]

counts = {}

for num in real_nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

ordered_counts = OrderedDict(sorted(counts.items()))

for key, value in ordered_counts.items():
    print(key, '->', value, 'times')