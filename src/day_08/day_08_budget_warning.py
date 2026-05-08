monthly_income = int(input('Podaj Twój miesięczny przychód: '))
rent = float(input('Podaj ile wydajesz miesięcznie na mieszkanie: '))
transport = float(input('Podaj ile miesięcznie wydajesz na środki lokomocji: '))
food = float(input('Podaj ile misięcznie wydajesz na jedzenie'))

total_spendings = rent + transport + food
savings_procent = (total_spendings/monthly_income) * 100

print(savings_procent)
print('Ocena sytuacji')
print('------------')

if savings_procent >= 100:
    print('budżet jest na minusie, ciężka sytuacja')
elif savings_procent < 10:
    print('Oszczędności na poziomie 10%, bardzo mały bufor')
elif savings_procent < 30:
    print('Oszczędności na poziomie 10-30%, rozsądny poziom')
else:
    print('Oszczędności na poziomie wyższym niż 30%, gratulacje')