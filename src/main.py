from validator import is_valid_status, validate_order, validate_orders
from data import get_orders
from report import print_errors, print_summary

print(is_valid_status('shipping'))
print(is_valid_status('paid'))
print(is_valid_status('no'))

orders = get_orders()

print(f"Liczba zamówie to {len(orders)}")

for order in orders:
    print(f"identyfikator zamówienia to: {order.get('order_id', 'Nieznany')}")
    print(f"Status zamówienia to: {order.get('status', 'Nieznany')}")

errors = ['Brak id zamówienia', 'Brak statusu zamówienia']
errors_second = []

print_errors(errors)
print_errors(errors_second)

errors_order = validate_order(orders[2])

print_errors(errors_order)

errors_final = validate_orders(orders)

print_errors(errors_final)

print_summary(orders, errors_final)


