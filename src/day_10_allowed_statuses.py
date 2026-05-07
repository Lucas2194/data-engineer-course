allowed_status = ['paid', 'pending', 'cancelled', 'refunded']
user_status = input('Podaj status swojego zamówienia: ')
user_status = user_status.lower()

if user_status in allowed_status:
    print('Status jest poprawny')
else: 
    print('Status jest niepoprawny')

