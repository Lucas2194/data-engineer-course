from pathlib import Path
import csv 
from csv_utils import read_orders_from_csv, read_orders_from_csv_way_second, write_orders_to_csv

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
ORDERS_FILE = DATA_DIR / "orders.csv"
PAID_ORDERS_FILE = OUTPUT_DIR / "paid_orders.csv"
INVALID_ORDERS_FILE = OUTPUT_DIR / "invalid_orders.csv"

with open(ORDERS_FILE, "r", encoding = "utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open(ORDERS_FILE, "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)

    print(reader)

    for row in reader:
        print(row)

orders_list = read_orders_from_csv(ORDERS_FILE)

print('To pierwsza funkcja: ')

print(orders_list)

print('A to nowa funkcja: ')

orders_list_two = read_orders_from_csv_way_second(ORDERS_FILE)

print(orders_list_two)

print(f"Liczba zamówień to: {len(orders_list)}")

status_paid = 0
status_pending = 0
status_cancelled = 0
status_unknow = 0 

for order in orders_list:

    if order['status'] == 'paid':
        status_paid += 1
    elif order['status'] == 'pending':
        status_pending += 1
    elif order['status'] == 'cancelled':
        status_cancelled += 1
    else:
        status_unknow += 1

print(f"Zamówien o status paid jest: {status_paid}, zamówień o status pending jest: {status_pending}, zamówień o statusie cancelled jest: {status_cancelled}, zamówień o statusie nieznanym jest {status_unknow}")

invalid_orders = []

for order in orders_list:
    
    try:
        raw_value = float(order['total_amount'])
    except (ValueError, TypeError):
        raw_value = None

    if raw_value is None:
        invalid_orders.append(order)
    elif raw_value <= 0:
        invalid_orders.append(order)

print("Błędne zamówienia:")

for bad_order in invalid_orders:
    print(bad_order)

paid_orders = []

for order in orders_list:

    if order['status'] == 'paid':
        paid_orders.append(order)

print('Opłacone zamówienia')

for paid_order in paid_orders:
    print(paid_order)

write_orders_to_csv(PAID_ORDERS_FILE, paid_orders)
write_orders_to_csv(INVALID_ORDERS_FILE, invalid_orders)