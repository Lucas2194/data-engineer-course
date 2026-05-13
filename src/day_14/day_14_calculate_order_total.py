def calculate_order_total(quantity, unit_price):
    return quantity * unit_price

order_one = calculate_order_total(2, 399)
order_two = calculate_order_total(1, 199)
order_three = calculate_order_total(5, 299.99)

print(f"Wartość zamówienia pierwszego to: {order_one}, wartość zamówienia drugiego to {order_two}, wartość zamówienia trzeciego to {order_three}")
