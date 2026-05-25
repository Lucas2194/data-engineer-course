import csv
from pathlib import Path

def read_orders_from_csv(file_path):
    
    orders_list = [] 

    with open(file_path, "r", encoding="utf-8") as file:
        
        reader = csv.DictReader(file)

        for row in reader:
            orders_list.append(row)

    return orders_list        

def read_orders_from_csv_way_second(file_path):
    
    with open(file_path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)
        orders_list = list(reader)

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