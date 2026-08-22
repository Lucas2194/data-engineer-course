from pathlib import Path
import csv 
from csv_utils import read_orders_from_csv, write_orders_to_csv, write_text_to_file
from validators import  validate_orders
from reports import build_validation_report
from transformers import transform_orders
import sys

# Foldery 

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
TEST_CASES = DATA_DIR / "test_cases"
# Ścieżki

ORDERS_FILE = DATA_DIR / "orders.csv"
PAID_ORDERS_FILE = OUTPUT_DIR / "paid_orders.csv"
INVALID_ORDERS_FILE = OUTPUT_DIR / "invalid_orders.csv"
VALID_ORDERS_FILE = OUTPUT_DIR / "valid_orders.csv"
VALIDATION_REPORT_FILE = OUTPUT_DIR / "validation_raport.txt"
TRANSFORMED_ORDERS_FILE = OUTPUT_DIR / "transformed_orders.csv"
TEST_A = TEST_CASES / "orders_not_found.csv"
TEST_B = TEST_CASES / "orders_empty.csv"
TEST_C = TEST_CASES / "orders_missing_status.csv"
TEST_D = TEST_CASES / "orders_header_only.csv"
TEST_E = TEST_CASES / "orders_invalid_row.csv"
PIPELINE_ERROR = OUTPUT_DIR / "pipeline_error.txt"

# Definicja kolumn

BASIC_ORDER_FIELDNAMES = ['order_id', 'customer_name', 'total_amount', 'status']
TRANSFORMED_ORDER_FIELDNAMES = ['order_id', 'customer_name', 'total_amount', 'status', 'is_paid', 'amount_category']

def main():
    
    try:
        orders = read_orders_from_csv(ORDERS_FILE, BASIC_ORDER_FIELDNAMES)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, csv.Error, ValueError) as error:
        print(f"pipeline został zatrzymany z powodu: {error}, ścieżka wejściowa: {ORDERS_FILE}")
        error = f'''
STATUS: FAILED
Ścieżka wejściowa {ORDERS_FILE}
Nazwa typu wyjątku {type(error).__name__}
Pipeline został zatrzymany z powodu: {error}
'''
        write_text_to_file(PIPELINE_ERROR, error)
        sys.exit(1)
    valid_orders, invalid_orders, errors = validate_orders(orders)

    total_count = len(orders)
    valid_count = len(valid_orders)
    invalid_count = len(invalid_orders)

    report = build_validation_report(total_count, valid_count, invalid_count, errors)

    write_orders_to_csv(VALID_ORDERS_FILE, valid_orders)
    write_orders_to_csv(INVALID_ORDERS_FILE, invalid_orders)

    write_text_to_file(VALIDATION_REPORT_FILE, report)

    transformed_orders = transform_orders(valid_orders)

    write_orders_to_csv(TRANSFORMED_ORDERS_FILE, transformed_orders, TRANSFORMED_ORDER_FIELDNAMES)

    print(f''' 
STATUS: \033[32mSUKCES\033[0m
PIPELINE CSV zakończony poprawnie.
Wczytano {len(orders)} zamówień.
Poprawnych zamówień jest {valid_count}.
Błędne zamówienia {invalid_count}.
Ilość przekształconych zamówień to: {len(transformed_orders)}.
Zapisano plik: {VALIDATION_REPORT_FILE}
''')

if __name__ == "__main__":
    main()
