orders_value = [452, 12, 876, 345, 999, 23, 104, 678, 432, 89, 211, 754, 533, 901, 3, 444, 287, 615, 119, 842]
big_orders = 0

for order_value in orders_value:
    print(order_value)
    if order_value >= 200:
        big_orders = big_orders + 1

print(f'Dużych zamówień jest: {big_orders}')