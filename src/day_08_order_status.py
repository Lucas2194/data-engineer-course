status = input('Podaj status zamówienia (paid, pending, cancelled, refunded): ')
status_lower = status.lower()

print(status_lower)
if status_lower == 'paid':
    print('Zamówienie opłacone')
elif status_lower == 'pending':
    print('Zamówienie w trakcje realizacji')
elif status_lower == 'cancelled':
    print('Zamówienie zostało anulowane')
elif status_lower == 'refunded':
    print('Zamówienie zostało zrefundowane')
else:
    print('Status nierozpoznawalny')