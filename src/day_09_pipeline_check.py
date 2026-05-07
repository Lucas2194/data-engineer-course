data_source = input('Podaj nazwę źródła danych: ')
count_rows = int('Podaj liczbę pobranych rekordów: ')
count_rows_erros = int('Podaj liczbę błędnych rekordów: ')
base_status = input('Czy połączenie z bazą działa: (TAK/NIE)')

base_status = base_status.lower()
count_rows_erros_procent = (count_rows_erros / count_rows ) * 100
if data_source != '' and count_rows > 0 and count_rows_erros_procent <= 5 and base_status == 'tak':
    print('Wszystko jest ok :)')