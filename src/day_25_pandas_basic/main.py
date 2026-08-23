from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "orders.csv"


def main():
    orders = pd.read_csv(CSV_FILE)

    # Rozwiązania zadań zapisuj poniżej.
    print(type(orders))

    print(f"Liczba wierszy i kolumny to: {orders.shape}")
    print(f"Liczba wierszy to {len(orders)}")
    print(f"Nazwa kolumny to: {orders.columns}")
    print(f"Typy kolumn to {orders.dtypes}")

    print(f"Ogólny raport: \n ")

    orders.info()

    customer_name_as_series = orders["customer_name"]
    print(f"Jako series:\n{customer_name_as_series}")

    customer_name_as_df = orders[["customer_name"]]

    print(f"Jako df:\n {customer_name_as_df}")

    basic_orders_view = orders[["order_id", "customer_name", "status"]]

    print(f"Wynik z wybranych kolumnt to:\n{basic_orders_view}\na shape to:\n{basic_orders_view.shape}")

    paid_orders = orders.loc[
        orders["status"] == "paid",
    ]

    print(f"DF z statusami jedynie paid:\n{paid_orders}")

    high_value_orders = orders.loc[
        orders["total_amount"] > 200,
        ["order_id", "customer_name", "total_amount"],
    ]

    print(f"DF z wartościami powyżej 200 i 3 kolumnami:\n {high_value_orders}")

    gdansk_orders = orders.loc[
        orders["city"] == "Gdańsk",
        ["customer_name", "city", "status"],
    ]

    print(f"DF z zamówieniami jedynie z Gdańska:\n{gdansk_orders}")

    paid_high_value_orders = orders.loc[
        (orders["status"] == "paid") & (orders["total_amount"] > 150), 
        ["order_id", "customer_name", "total_amount"],
    ]

    print(f"DF z zamówieniami opłaconymi oraz kwotą powyżej 150:\n{paid_high_value_orders}")

    unfinished_orders = orders.loc[
        (orders["status"] == "pending") | (orders["status"] == "cancelled"),
        ["order_id", "customer_name", "status"],
    ]

    print(f"DF z zamówieniami o statusie pending albo cancelled:\n{unfinished_orders}")

    orders_outside_kartuzy = orders.loc[
        orders["city"] != "Kartuzy",
        ["order_id", "customer_name", "city"],
    ]

    print(f"DF z zamówieniami spoza Kartuz:\n{orders_outside_kartuzy}")

    print(f'''
RAPORT KONTROLNY
Wszystkie zamówienia: {len(orders)}
Liczba kolumn: {len(orders.columns)}
Zamówienia paid: {len(paid_orders)}
Zamówienia powyżej 200: {len(high_value_orders)}
Zamówienia pending lub cancelled: {len(unfinished_orders)}
''')

# Zadanie dodatkowe A - Series - 1 , B - DF 1 , C - DF - 2 D - Series - 1 , E - DF - 2 




    
if __name__ == "__main__":
    main()