from pathlib import Path 
import json
from json_utils import read_json_file, get_paid_orders, calculate_orders_total, write_json_file

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# Ścieżki 

ORDERS_FILE = DATA_DIR / "orders.json"
PAID_ORDERS_FILE = OUTPUT_DIR / "paid_orders.json"
SUMMARY_FILE = OUTPUT_DIR / "summary.json"

def main():

    orders = read_json_file(ORDERS_FILE)

    if orders is None:
        return

    print(f"Typ całego orders to: {type(orders)}")
    print(f"Typ pierwszego zamówienia to: {type(orders[0])}")
    print(f"Typ total_amount to: {type(orders[0]["total_amount"])}")
    print(f"Typ tagsów to: {type(orders[0]["tags"])}")
    print(f"Typ ostatniego zamówienia to: {type(orders[-1]["delivery"])}")

    paid_orders = get_paid_orders(orders)

    print(f"Liczba opłaconych zamówień to: {len(paid_orders)}")

    total = calculate_orders_total(paid_orders)
    print(f"Dokładna wartość zamówień to: {total}")

    write_json_file(PAID_ORDERS_FILE, paid_orders)

    summary = {
        "total_orders": len(orders),
        "paid_orders": len(paid_orders),
        "paid_total": total
    }

    write_json_file(SUMMARY_FILE, summary)


    for order in orders:
        if order.get('delivery') is None:
            print(f'{order.get('customer_name')} - brak danych o dostawie')
        else:
            print(f'{order.get('customer_name')} - {order.get('delivery')['city']}')

if __name__ == "__main__":
    main()