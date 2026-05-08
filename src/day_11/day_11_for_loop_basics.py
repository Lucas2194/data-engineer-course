statuses = ["paid", "pending", "wrong_status", "cancelled"]
allowed_statuses = ["paid", "pending", "cancelled", "refunded"]

errors = []

for status in statuses:
    if status not in allowed_statuses:
        errors.append(f"Nieznany status: {status}")

print(errors)