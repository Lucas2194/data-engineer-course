import csv
from pathlib import Path
from validators import find_missing_columns

def read_orders_from_csv(file_path, required_columns):
    
    orders_list = [] 

    file_path = Path(file_path)

    with open(file_path, "r", encoding="utf-8", newline ="") as file:
        
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("Brakuje nagłówka")

        missing_columns = find_missing_columns(reader.fieldnames, required_columns)

        if missing_columns != []:
            raise ValueError(f"Brakuje nagłówków: {", ".join(missing_columns)}")

        for row in reader:
            orders_list.append(row)

    if not orders_list:
        raise ValueError("Plik ma nagłówek ale nie zawiera danych")

    return orders_list        

def write_orders_to_csv(file_path, orders, fieldnames=None):

    file_path = Path(file_path)
    file_path.parent.mkdir(parents = True, exist_ok = True)

    if not orders:
        print(f"Lista jest pusta. Pomijamy zapis do {file_path}")
        return
    if fieldnames is None:
        fieldnames = list(orders[0].keys())

    with open(file_path, "w", encoding="utf-8", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for order in orders:
            writer.writerow(order)

def write_text_to_file(file_path, text):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok = True)

    with open(file_path, "w", encoding = "utf-8") as file:
        file.write(text)