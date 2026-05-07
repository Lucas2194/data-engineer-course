order_value = int(input('Podaj wartość zamówienia: '))
order_status = input('Podaj status zamówienia: ')

order_status = order_status.lower()

allowed_status = ['paid', 'cancel', 'pending']
errors = []

if order_value <= 0:
    errors.append('Wartość zamówienia jest mniejsza od 0')
if order_status not in allowed_status:
    errors.append('Nie mamy takiego statusu zamówienia')

if len(erros) == 0:
    print('Nie ma błędów')
else:
    for i in errors:
        print(i)