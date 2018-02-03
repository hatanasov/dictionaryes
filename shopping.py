def stock():
    stocks = {}
    while True:
        input_stock = input()
        if input_stock == 'shopping time':
            break
        input_stock = input_stock.split()
        if input_stock[1] in stocks:
            stocks[input_stock[1]] += int(input_stock[2])
        else:
            stocks[input_stock[1]] = int(input_stock[2])
    return stocks


def bye(stock_dict):
    stocks = stock_dict
    while True:
        bye_stock = input()
        if bye_stock == 'exam time':
            break
        bye_stock = bye_stock.split()
        if bye_stock[1] not in stocks:
            print(bye_stock[1], "doesn't exist")
        elif stocks[bye_stock[1]] < 1:
            print(bye_stock[1], 'out of stock')
        elif stocks[bye_stock[1]] < int(bye_stock[2]):
            stocks[bye_stock[1]] = 0
        else:
            stocks[bye_stock[1]] -= int(bye_stock[2])
    for key, value in stocks.items():
        if value > 0:
            print(key, '->', value)


bye(stock())
