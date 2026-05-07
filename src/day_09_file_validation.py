file_name = input('Podaj nazwę pliku: ')
rows = int(input('Podaj liczbę wierszy: '))
rows_erros = float(input('Podaj procent błędnych wierszy (Sama liczba): '))

if file_name != '' and rows > 0 and rows_erros <= 5:
    print('Plik można przetwarzać')
else:
    print('Wymaga sprawdzenia')

    
