order = {
    "order_id": 1001,
    "customer_name": "Anna Kowalska",
    "order_value": 249.99,
    "status": "paid"
}

print(order["status"])

for ord in order:
    print(order[ord])

print(order['status'])

order['currency'] = 'PLN'
order['status'] = 'refund'

for ord in order:
    print(order[ord])