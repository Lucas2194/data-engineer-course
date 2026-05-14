def is_valid_status(status):
    allowed_statuses = ['paid', 'cancel', 'shipping']
    return status in allowed_statuses

def validate_order(order):
    errors = []

    if order.get('order_id') is None:
        errors.append(f"Zamówienie ID: {order.get("order_id", "BRAK")} - Brakuje klucza identyfikatora zamówienia")
    
    if order.get('order_value') is None:
        errors.append(f'Zamówienie o ID: {order.get("order_id", "BRAK")} - Brakuje klucza wartości zamówienia')
    elif order['order_value'] <= 0:
        errors.append(f'Zamówienie o ID: {order.get("order_id", "BRAK")} - Wartość zamówienia jest równa, bądź mniejsza od 0')
    
    if order.get('status') is None:
        errors.append(f'Zamówienie ID: {order.get("order_id", "Brak")} - Brakuje klucza statusu zamówienia')
    elif not is_valid_status(order['status']):
        errors.append(f'Zamówienie ID: {order.get("order_id", "Brak")} - Niedozwolony status zamówienia')

    return errors

def validate_orders(orders):

    errors = []

    for order in orders:
        errors.extend(validate_order(order))
    
    return errors