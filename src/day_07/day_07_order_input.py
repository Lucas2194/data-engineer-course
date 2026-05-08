product_name = input('Podaj nazwę produktu: ')
quantity = int(input('Podaj liczbę sztuk: '))
price_per_piece = float(input('Podaj cenę za sztukę: '))

total_order = quantity * price_per_piece

print(f'Całościowa wartość zamówienia to: {round(total_order, 3)}zł.')

