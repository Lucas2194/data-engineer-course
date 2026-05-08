age = int(input('Podaj swój wiek: '))
ticket = input('Czy posiadasz bilet (TAK/NIE): ')

ticket = ticket.lower()

if age >= 18 and ticket == 'tak':
    print('Możesz wejść')
else:
    print('Niestety, nie możesz wejść')

    