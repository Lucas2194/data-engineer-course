monthly_income = float(input('Jaki jest Twój miesięczny przychód: '))
rent = float(input('Jaka jest opłata za Twoje mieszkanie: '))
food_cost = float(input('Jaki jest koszt jedzenia: '))
transport_cost = float(input('Jaki jest koszt transporti: '))

expenses = rent + food_cost + transport_cost
money_left = monthly_income - expenses
savings = (money_left / monthly_income) * 100

print('Raport')
print('-----------------')
print(f'Twoje wydatki to: {expenses} zł')
print(f'Zostaje Tobie w miesiącu: {money_left}')
print(f'Oszczędności: {round(savings, 3)}%')