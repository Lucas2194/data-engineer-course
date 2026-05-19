from data import get_orders
from validator import validate_orders, split_orders_by_validity
from reports import build_errors_report, build_summary_report
from file_utils import write_text_to_file, append_text_to_file, read_text_from_file

with open("reports/validation_report.txt", "w", encoding = "utf-8") as file:
    file.write("Pierwszy raport walidacji")

with open("data/notes.txt", "r", encoding = "utf-8") as file:
    content = file.read()

print(content)

write_text_to_file("reports/validation_report.txt", "Oto nowy nadpisany tekst")
append_text_to_file("reports/validation_report.txt", "\nKolejna linia")

content_notes = read_text_from_file("data/notes.txt")
content_report = read_text_from_file("reports/validation_report.txt")

print(content_notes)
print(content_report)

def main():

    orders = get_orders()
    errors = validate_orders(orders)
    report = build_errors_report(errors)
    summary_report = build_summary_report(orders, errors)
    report += summary_report
    valid_list, invalid_list = split_orders_by_validity(orders)
    
    write_text_to_file("reports/validation_report.txt", report)
    append_text_to_file("reports/log.txt", "Program zakończył działanie\nProgram zakończył działanie.\n")

if __name__ == '__main__':
    main()