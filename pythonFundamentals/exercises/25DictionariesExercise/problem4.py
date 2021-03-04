products = {} # key is name, value is list of price and quantity

command = input()

while command != 'buy':
    name, price, quantity = command.split(' ')
    price, quantity = float(price), float(quantity)
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][1] += quantity
        products[name][0] = price

    command = input()

for name, priceQuantity in products.items():
    print(f'{name} -> {priceQuantity[0]*priceQuantity[1]:.2f}')