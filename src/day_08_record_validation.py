order_id = int(input('Podaj numer zamówienia: '))
order_value = int(input('Podaj wartość zamówienia: '))
payment_status = input('Podaj status zamówienia')

payment_status_lower = payment_status.lower()

if order_value <= 0:
    print('Rekord błędny')
elif payment_status_lower == 'paid' and order_value > 0:
    print('Rekord poprawny')
elif payment_status_lower == 'pending':
    print('Rekord oczekuje na płatność')
elif payment_status_lower == 'cancelled':
    print('Zamówienie anulowane')
    