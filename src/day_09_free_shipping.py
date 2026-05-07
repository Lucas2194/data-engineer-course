order_value = float(input('Podaj wartość zamówienia: '))
free_shiping_code = input('Czy posiadasz kod darmowej dostawy?(TAK/NIE)')

free_shiping_code = free_shiping_code.lower()

if order_value > 200 or free_shiping_code == 'tak':
    print('Przysługuje Ci darmowa dostawa')
else:
    print('Niestety, ale darmowa dostawa Ci nie przysługuje')
