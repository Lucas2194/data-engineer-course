from validator import validate_orders, count_valid_orders, count_invalid_orders, split_orders_by_validity
from data import get_orders
from report import print_summary, print_valid_invalid_summary
from pathlib import Path

print(Path.cwd())
print(Path(__file__).parent)

def main():
    orders = get_orders()
    errors_final = validate_orders(orders)
    valid_orders = count_valid_orders(orders)
    invalid_orders = count_invalid_orders(orders)
    print_summary(orders, errors_final)
    print_valid_invalid_summary(valid_orders, invalid_orders)
    valid_list, invalid_list = split_orders_by_validity(orders)
    print(f"Poprawne zamówienia to : {valid_list}")
    print(f"Niepoprawne zamówienai to: {invalid_list}")
    
if __name__ == '__main__':
    main()







