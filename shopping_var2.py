def gen_product_dict(stop_keyword):

    product_dict = {}

    while True:
        user_input = input()
        if user_input == stop_keyword:
            break
        user_input = user_input.split()
        if user_input[1] not in product_dict:
            product_dict[user_input[1]] = int(user_input[2])
        else:
            product_dict[user_input[1]] += int(user_input[2])

    return product_dict

stock = gen_product_dict('shopping time')
bye = gen_product_dict('exam time')

for key, value in bye.items():
    if key not in stock:
        print(key, "doesn't exist")
    elif stock[key] < 1:
        print(key, 'out of stock')
    elif stock[key] < bye[key]:
        stock[key] = 0
    else:
        stock[key] -= bye[key]

for key, value in stock.items():
    if value > 0:
        print(key, '->', value)