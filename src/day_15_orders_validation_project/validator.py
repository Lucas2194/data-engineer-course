def is_valid_status(status):
    allowed_statuses = ['paid', 'cancel', 'shipped']
    return status in allowed_statuses

def validate_order(order):
    errors = []

    raw_order_value = order.get("order_value")

    if order.get('order_id') is None:
        errors.append(f"Zamówienie ID: {order.get('order_id', 'BRAK')} - Brakuje klucza identyfikatora zamówienia")
    
    if raw_order_value is None:
        errors.append(f'Zamówienie o ID: {order.get("order_id", "BRAK")} - Brakuje klucza wartości zamówienia')
    else:
        order_value = safe_float(raw_order_value)

        if order_value is None:
            errors.append(f'Zamówienie o ID: {order.get("order_id", "BRAK")} - Niepoprawna wartość zamówienia')
        elif order_value <= 0:
            errors.append(f'Zamówienie o ID: {order.get("order_id", "BRAK")} - Wartość zamówienie jest mniejsza bądź równa 0')
    
    raw_status = order.get("status")
    status = normalize_status(raw_status)

    if status is None:
        errors.append(f'Zamówienie ID: {order.get("order_id", "Brak")} - Brakuje klucza statusu zamówienia')
    elif not is_valid_status(status):
        errors.append(f'Zamówienie ID: {order.get("order_id", "Brak")} - Niedozwolony status zamówienia')

    return errors

def validate_orders(orders):

    errors = []

    for order in orders:
        errors.extend(validate_order(order))
    
    return errors

def count_valid_orders(orders):
    count = 0
    
    for order in orders:
        if not validate_order(order):
            count += 1

    return count

        
def count_invalid_orders(orders):

    count = 0 

    for order in orders:
        if validate_order(order):
            count += 1

    return count

def split_orders_by_validity(orders):

    valid_orders = []
    invalid_orders = []

    for order in orders:
        if not validate_order(order):
            valid_orders.append(order)
        else:
            invalid_orders.append(order)

    return valid_orders, invalid_orders

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
    
def normalize_status(status):
    if isinstance(status, str):
        return status.lower().strip()
    return None

    
