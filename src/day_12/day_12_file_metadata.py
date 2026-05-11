file = {
    "file_name":"orders.csv",
    "rows_count": 5000,
    "error_count": 125,
    "source_system": "windows",
}

print(file["file_name"])
print(f'Liczba wierszy to: {file["rows_count"]}')

errors_percent = (file["error_count"] / file["rows_count"]) * 100

file['error_percent'] = errors_percent

print(file)