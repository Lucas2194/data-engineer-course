file_name = input('Podaj nazwę pliku: ')
file_row = int(input('Podaj liczbę wierszy:'))
file_row_errors = int(input('Podaj liczbę błędnych wierszy: '))

correct_rows = file_row - file_row_errors

print(f'Raport jakości pliku {file_name}')
print('---------------------------')
print(f'Poprawne wiersze {file_row - file_row_errors}')
print(f'Błędne wiersze {file_row_errors}')
print(f'Procent błędnych wierszy {round((file_row_errors / file_row) * 100, 3)}%')
print(f'Procent poprawnych wierszy to {round((correct_rows / file_row) * 100, 3)}%')