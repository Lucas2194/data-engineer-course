file_names = []
first_file_name = input('Podaj nazwę pierwszego pliku')
second_file_name = input('Podaj nazwę drugiego pliku')
third_file__name = input('Podaj nazwę trzeciego pliku')

file_names.append(first_file_name)
file_names.append(second_file_name)
file_names.append(third_file__name)

for i in file_names:
    print(i)

print(len(file_names))