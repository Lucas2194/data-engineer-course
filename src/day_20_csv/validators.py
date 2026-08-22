ALLOWED_STATUSES = ['paid', 'pending', 'cancelled']

def is_valid_status(status):
    return status in ALLOWED_STATUSES

def safe_float(value):
    try:
        return float(value)
    except(TypeError, ValueError):
        return None
    
def normalize_status(status):
    if isinstance(status, str):
        return status.lower().strip()
    return None

def validate_order(order):

    errors = []

    raw_order_value = safe_float(order.get("total_amount"))

    status = normalize_status(order.get("status"))

    if not order.get('order_id'):
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Brak klucza ID zamówienia")
    
    if not order.get('customer_name'):
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Brakuje klucza imienia klienta")
    
    if not order.get('total_amount'):
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Brakuje klucza wartości zamówienia")
    elif raw_order_value is None:
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Niepoprawna wartość zamówienia")
    elif raw_order_value <= 0:
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Wartość zamówienia jest mniejsza bądź równa 0")
    
    if not status:
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Brakuje klucza statusu zamówienia")
    elif not is_valid_status(status):
        errors.append(f"Zamówienie o ID {order.get('order_id', 'BRAK')} - Niepoprawny status zamówienia")

    return errors

def validate_orders(orders):

    all_validation_errors = []
    valid_orders = []
    invalid_orders = []

    for order in orders:
        errors = validate_order(order)

        if not errors:
            valid_orders.append(order)
        else:
            invalid_orders.append(order)
            all_validation_errors.extend(errors)

    return valid_orders, invalid_orders, all_validation_errors

def find_missing_columns(actual_columns, required_columns):
    missing_columns = []
    for required_column in required_columns:
        if required_column not in actual_columns:
            missing_columns.append(required_column)

    return missing_columns
