monthly_income = 5000
rent = 1800
food = 1200
transport = 400
subscriptions = 150 

total_expenses = rent + food + transport + subscriptions
money_left = monthly_income - total_expenses
saving_rate_procent = money_left / monthly_income * 100

print("Miesięczny raport Finansowy:")

print(f'Przychód: {monthly_income}')
print(f'Wydatki: {total_expenses}')
print(f'Zostaje: {money_left}')
print(f'Stopa oszczędzania: {round(saving_rate_procent, 3)}%')



