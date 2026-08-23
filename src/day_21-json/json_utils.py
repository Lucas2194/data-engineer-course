import json
from pathlib import Path

def read_json_file(file_path):
    path = Path(file_path)

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {path}")
        return None
    except json.JSONDecodeError as error:
        print(f"Plik nie zawiera poprawnego JSON-a {path}")
        print(f"Szcegóły: {error}")
        return None

def write_json_file(file_path, data):

    path = Path(file_path)
    path.parent.mkdir(parents = True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def normalize_status(status):
    if isinstance(status, str):
        return status.lower().strip()
    return None

def get_paid_orders(orders):
    paid_orders = []

    for order in orders:
        if normalize_status(order.get('status')) == 'paid':
            paid_orders.append(order)

    return paid_orders 

def calculate_orders_total(orders):

    total = 0.0

    for order in orders:
        total = total + order['total_amount']

    return total 
