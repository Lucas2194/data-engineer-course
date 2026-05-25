def get_amount_category(amount):

    if amount < 100:
        return 'small'
    elif amount <= 299.99:
        return 'medium'
    else:
        return 'large'
    
def transform_order(order):
    # Tworzymy puste, NOWE pudełko
    transformed = {}

    # Przepisujemy dane ze starego słownika, od razu je czyszcząc
    transformed['order_id'] = int(order['order_id'])
    transformed['customer_name'] = order['customer_name'].strip()
    transformed['total_amount'] = float(order['total_amount'])
    transformed['status'] = order['status'].strip().lower()

    # Tworzymy pole is_paid (Python sam wstawi tu True lub False)
    transformed['is_paid'] = (transformed['status'] == 'paid')

    # Przekazujemy OCZYSZCZONĄ już kwotę do Twojej funkcji
    transformed['amount_category'] = get_amount_category(transformed['total_amount'])

    # Zwracamy nowiutki, idealnie czysty słownik
    return transformed

def transform_orders(orders):
    
    transformed = []

    for order in orders:
        transformed.append(transform_order(order))

    return transformed

