def print_errors(errors):
    print('! --- Raport Walidacji --- !')
    if not errors:
        print('Brak błędów')
    else:
        for error in errors:
            print(error)


def print_summary(orders, errors):
    
    print(f'liczba zamówień to: {len(orders)}')
    print(f'Liczba błędów to: {len(errors)}')

    if not errors:
        print('Dane mogą iść dalej')
    else:
        print('Dane wymagają poprawy')