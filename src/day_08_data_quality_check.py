file_name = input('Podaj nazwę pliku: ')
file_rows = int(input('Podaj liczbę wierszy: '))
file_rows_errors = int(input('Podaj liczbę błędnych wierszy: '))

procent_rows_erros = (file_rows_errors / file_rows) * 100

print('Ocena pliku')
print('-------------')

if procent_rows_erros == 0:
    print('Plik idealny, 0% błędów')
elif procent_rows_erros > 0 and procent_rows_erros <= 5:
    print('Dane w przedziale 0 - 5% są akceptowalne')
elif procent_rows_erros > 5 and procent_rows_erros <= 20:
    print('Dane wymagają sprawdzenia, błędy są między 5 a 20 %')
else:
    print('Błędne dane powyżej 20%, są problematyczne')