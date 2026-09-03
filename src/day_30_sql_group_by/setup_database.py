import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "orders.csv"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_FILE = DATABASE_DIR / "orders.db"


def main():
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    orders = []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            orders.append(
                (
                    int(row["order_id"]),
                    row["customer_name"],
                    float(row["total_amount"]),
                    row["status"],
                    row["city"],
                )
            )

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS orders")

    cursor.execute(
        """
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT NOT NULL,
            city TEXT NOT NULL
        )
        """
    )

    cursor.executemany(
        """
        INSERT INTO orders (
            order_id,
            customer_name,
            total_amount,
            status,
            city
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        orders,
    )

    connection.commit()
    connection.close()

    print(f"Utworzono bazę: {DATABASE_FILE}")
    print(f"Dodano rekordów: {len(orders)}")


if __name__ == "__main__":
    main()