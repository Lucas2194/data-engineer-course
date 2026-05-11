orders = [
    {
        'order_id': 101,
        'order_value': 250,
        'status': 'paid'
    },
    {
        'order_id': 102,
        'order_value': 0,
        'status': 'cancel'
    },
    {
        'order_id': 103,
        'order_value': 120,
        'status': 'pending'
    }
]

for order in orders:
    print(f"Zamówienie numer: {order['order_id']}, a jego status to: {order['status']}")