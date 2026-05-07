file_name = input('Podaj nazwę pliku: ')
count_rows = int(input('Podaj liczbę wierszy: '))
percent_errors = float(input('Podaj procent błednych wierszy: '))

errors = []

if file_name == '':
    errors.append('Lista jest pusta')
if count_rows <= 0:
    errors.append('Liczba wierszy jest mniejsza lub równa 0')
if percent_errors > 5:
    errors.append('Procent Błędów jest większy niż 5')

if len(errors) == 0:
    print('Plik wygląda poprawnie')
else:
    for i in errors:
        print(i)