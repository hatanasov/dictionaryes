saved_values = {}

while True:
    entry = input().split(' = ')
    if entry == ['end']:
        break
    try:
        saved_values[entry[0]] = int(entry[1])
    except ValueError:
        if entry[1] in saved_values.keys():
            saved_values[entry[0]] = saved_values[entry[1]]


for key, value in saved_values.items():
    print(key, '===', int(value))