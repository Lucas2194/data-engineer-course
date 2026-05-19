from data import get_orders
from validator import validate_orders, split_orders_by_validity
from reports import build_errors_report, build_summary_report
from file_utils import write_text_to_file, append_text_to_file, read_text_from_file
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
NOTES_FILE = DATA_DIR / "notes.txt"
VALIDATION_REPORT_FILE = REPORTS_DIR / "validation_report.txt"
LOG_FILE = REPORTS_DIR / "log.txt"

with open(VALIDATION_REPORT_FILE, "w", encoding = "utf-8") as file:
    file.write("Pierwszy raport walidacji")

with open(NOTES_FILE, "r", encoding = "utf-8") as file:
    content = file.read()



print(content)

write_text_to_file(VALIDATION_REPORT_FILE, "Oto nowy nadpisany tekst")
append_text_to_file(VALIDATION_REPORT_FILE, "\nKolejna linia")

content_notes = read_text_from_file(NOTES_FILE)
content_report = read_text_from_file(VALIDATION_REPORT_FILE)

print(content_notes)
print(content_report)

print(Path.cwd())
print(Path(__file__).parent)



def main():

    orders = get_orders()
    errors = validate_orders(orders)
    report = build_errors_report(errors)
    summary_report = build_summary_report(orders, errors)
    report += summary_report
    valid_list, invalid_list = split_orders_by_validity(orders)
    
    write_text_to_file(VALIDATION_REPORT_FILE, report)
    append_text_to_file(LOG_FILE, "Program zakończył działanie\nZakończyła się Validacja pliku.\n")

if __name__ == '__main__':
    main()