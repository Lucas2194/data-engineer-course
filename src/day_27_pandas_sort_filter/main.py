from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "orders.csv"


def main():
    orders = pd.read_csv(CSV_FILE)

    print("Rozmiar danych:", orders.shape)
    print(orders.head())

    print(orders.columns)
    print(orders.dtypes)

    # Zadanie 1 
    # Wierszy jest 12, kolumn jest 5, total_amount jest typem float64, pierwszym jest order_id: 1001, ostatnim order_id: 1012 

    # Zadanie drugie 

    amounts_ascending = orders.sort_values(
        by="total_amount",
        ascending=True,
    )
    print("-----------------------\n\n\n\n")

    print(amounts_ascending[["order_id", "customer_name", "total_amount"]])

    # Zadanie trzecie

    print("-----------------------\n\n\n\n")

    amounts_descending = orders[["order_id", "customer_name", "total_amount"]]
    amounts_descending = amounts_descending.sort_values(
        by="total_amount",
        ascending=False,
    )

    # Odpowiedź na pytanie dodatkowe - ascending = False 

    print(f"Kwoty malejąco:\n---------------------------\n {amounts_descending}")

    # Zadanie 4

    sorting_by_many_columns = orders.sort_values(
        by = ["city", "total_amount", "order_id"],
        ascending=[True, False, True],
    )

    print(f"Sortowanie po wielu kolumnach:\n---------------------\n{sorting_by_many_columns}")

    # Pytania dodatkowe - Za miasto odpowiada True, pierwsza wartość. Za kwotę odpowiada druga, False. Dodaliśmy order_id, bo kolejność ma znaczenie. W przypadku remisu, musimy mieć coś unikatowego

    # Zadanie 5 

    mask_paid_orders = orders.loc[
        orders["status"] == "paid",
        ["order_id", "customer_name", "total_amount", "status"]
    ]

    sorted_total_amount = mask_paid_orders.sort_values(
        by=["total_amount", "order_id"],
        ascending=[False, True]
    )

    print(f"Sortowanie i filtrowanie z dwóch masek:\n--------------------\n{sorted_total_amount}")

    # Zadanie 6

    three_biggest_orders = orders.sort_values(
        by="total_amount",
        ascending=False,
    )

    print(f"\n-----------------\nTrzy największe zamówienia to:\n----------------\n: {three_biggest_orders[["order_id", "customer_name", "total_amount"]].head(3)}")

    ## odpowiedź na pytanie - ponieważ najpierw musimy posorotwać, a następnie sprawdzić 3 pierwsze rekordy. 

    # Zadanie 7 

    four_cheapest_orders = (
        orders.loc[
            orders["status"] == "paid",
            ["order_id", "customer_name", "total_amount", "status"]
        ]
        .sort_values(
            by="total_amount",
            ascending=True
        )
        .head(4)
    )

    print(f"\n----------\nCztery najtańsze zamówienia to:\n----------\n{four_cheapest_orders}")

    # Zadamoe 8 

    two_citys = orders.loc[
        orders["city"].isin(["Gdańsk", "Gdynia"]),
        ["order_id", "customer_name", "city", "total_amount"]
    ]

    print(f"\n-------\nZamówienia z Gdańska i Gdynii\n---------\n{two_citys}")

    # Zwraca maskę True/False 

    # Zadanie 9 

    two_statuses = (
        orders.loc[
            orders["status"].isin(["pending", "cancelled"]),
            ["order_id", "customer_name", "status", "total_amount"],
        ]
        .sort_values(
            by=["total_amount", "order_id"],
            ascending = [False, True]
        )
    )

    print(f"Zamówienia z statusami pending i cancelled\n--------------\n{two_statuses}")

    # Zadanie 10

    outside_city = (
        orders.loc[
            ~orders["city"].isin(["Kartuzy", "Sopot"]),
            ["order_id", "customer_name", "city"],
        ]
        .sort_values(
            by="order_id"
        )
    )

    print(f"Zamówienia spoza Kartuz i Sopotu:\n------------\n{outside_city}")

    # operator ~ odwraca maskę - True -> False, False -> True

    ## Zadanie 11

    amount_between = (
        orders.loc[
            orders["total_amount"].between(120, 260),
            ["order_id", "customer_name", "total_amount"],
        ]
        .sort_values(
            by=["total_amount", "order_id"],
            ascending=True,
        )
    )

    print(f"Zamówienai z kwotą pomiędzy 120 a 260:\n---------\n{amount_between}")

    besides_amount = (
        orders.loc[
            ~orders["total_amount"].between(100, 300),
            ["order_id", "customer_name", "total_amount"],
        ]
        .sort_values(
            by=["total_amount", "order_id"],
            ascending=True,
        )
    )

    print(f"Zamówienia z kwotami które nie wchodzą do przedziału 100 - 300:\n---------\n:{besides_amount}")

    report = (
        orders.loc[
            (orders["status"].isin(["paid", "pending"])) & (orders["total_amount"].between(100, 500)) & (orders["city"] != "Kartuzy"),
            ["order_id", "customer_name", "total_amount", "status", "city"], 
        ]
        .sort_values(
            by=["total_amount", "order_id"],
            ascending=[False, True],
        )
        .head(4)
    )

    print(f"Finalny raport:\n-----------\n{report}")

    # Zadanie 14 - Jutro dokończę, nie mam dzisiaj siły na pytania biznesowe własne. Ale rozumiem całą ideę. Korzystam też z łańcuchów, bo wydaje mi się, że to potrafię i nie sprawia mi problemu. Także oceń proszę, jakbym nie musiał tego rozbijać. 

    # Zadanie dodatkowe bez uruchomienia 

    # A - Wynik będzie posorotwany według kwoty malejąco, liczba wierszy wszystkie - 12 
    # B - Wynikiem będzie posorotowane 2 wiersze, po kwocie, rosnąco
    # C - Wynikiem będzie maska True/False. 
    # D - Wynikiem będą wszystkie wiersze z kwotą z przedziału 120, 260, dwie kolumny. Niekoniecznie posorotwane, bo nei ma sort, więc pewnie po indeksie DF
    # E - Tutaj jest teoretycznie błąd, bo najpierw powininśmy sorotwać no a potem head, ale program się wykona, tylko posortuje 3 pierwsze rekordy według wartości, malejąco. Także 3 wiersze

    # Znajdź problem

    # 1 False nie powinno być "" to typ Bool a nie str
    # 2 Tyle ile wartości w by, tyle powinno być w ascending. Brakuje True/False. Ewentualnie bez nawiasów można zapisać jedną wartość. Rrzypiszę się do każdego wtedy
    # 3 używamy .isin a nie in.
    # 4 nie używamy not tylko ~ 
    # 5 head powinno być po sorotwaniu, tak posortujemy jedynie 3 pierwsze wiersze, zamiast wszystkich. Także nie da nam 3 najiekszych wartości, tak jak zmienna opisana
    # 6 Teoretycznie wszystko jest ok, ale zmieniamy całe orders, a nie chcemy tego robić. Powinniśmy mieć nową zmienną do tego. Np. sorted_orders_by_amount_desc

    # QUIZ 

    # 1 - B
    # 2 - B
    # 3 - C 
    # 4 - B 
    # 5 - B 

if __name__ == "__main__":
    main()