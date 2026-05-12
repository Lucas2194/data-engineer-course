order = {
    
    'status': 'sent',
    'order_value': -1
}

errors = []

if order.get('order_value') is None:
    if order.get("order_id") is not None:
        errors.append(f'Zamówienie o numerze {order["order_id"]}, nie ma klucza wartości zamówienia')
else:
    if order['order_value'] <= 0:
        if order.get("order_id") is not None:
            errors.append(f'Zamówienie o numerze {order["order_id"]}, ma wartośc mniejszą bądź równą 0')
        else:
            errors.append('Jest błąd z wartością zamówienia, która jest na minusie bądź 0, lecz niestety w rekordzie brakuje również klucza, także nie można wskazać w którym to rekordzie.')
print(errors)

