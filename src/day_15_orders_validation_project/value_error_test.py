
try:
    value = int("abc")
except (ValueError):
    value = None

print(value)