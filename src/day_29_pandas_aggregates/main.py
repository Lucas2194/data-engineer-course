import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data" / "orders.csv"


def main():
    orders = pd.read_csv(CSV_FILE)

    print("Wersja Pandas:", pd.__version__)
    print("Rozmiar danych:", orders.shape)
    print(orders.head())
    orders.info
    print(orders.columns)
    print(orders.dtypes)
    print(orders["total_amount"].count())

    print('--------------------------------')

    # Zadanie 2 

    print(f"Użycie len : {len(orders)}")
    print(f'Użycie shape : {orders.shape[0]}')
    print(f"Użycie .size {orders['total_amount'].size}")
    print(f"Użycie count : {orders['total_amount'].count()}")

    # Przewidywania przed uruchomieniem : 12,12,12,12. Dlaczego? Bo nie ma żadnych pustych wartości w naszych danych. Najbardziej pasuje count()

    # Zadanie 3 

    paid_mask = orders["status"] == "paid"
    filtred_df = orders.loc[paid_mask]
    total_paid_orders = filtred_df.shape[0]

    print(f"Liczba zamówień z statusem paid to: {total_paid_orders}")

    ## B

    pending_calcelled_orders = orders["status"].isin(["pending", "cancelled"])
    filtred_df = orders.loc[pending_calcelled_orders]
    total_pending_calcelled_orders = filtred_df.shape[0]

    print(f"Liczba zamówień z statusem pending albo cancelled to: {total_pending_calcelled_orders}")

    # Liczenie zawsze wykonujemy po filtrowaniu, inaczej miajoby się to z celem, bo liczylibyśmy całą dataFrame, zamiast nam potrzebną. 

    # Zadanie 4 - Jak coś świadomie wybieram .loc[] inline - uważam że jestem w stanie to już robić. 

    selected_orders = orders.loc[
            (orders["status"].isin(["paid", "pending"])) & (orders["total_amount"].between(100,500)) & (orders["city"] != "Kartuzy")
        ]

    print(f"Zamówienia z statusami paid albo pending, z kwotą pomiędzy 100 a 500, z miastem innym niż kartuzy to: {selected_orders.shape[0]}")
    print(selected_orders["order_id"])

    sum_price = orders["total_amount"].sum()

    print(f"Suma zamówień to: {sum_price}")

    # Typ obiektu to series
    # Typ obiektu po to float 
    # Źródłowy DF nie został zmieniony 

    sum_price_paid = (
        orders.loc[
            orders["status"] == "paid",
            "total_amount",
        ]
        .sum()
    )

    print(f"Suma zamówień z statusem paid: {sum_price_paid}")

    # Kolejność jest taka, ponieważ najpierw należy przefiltrować zamówienia z odpowiednim statusem, a następnie policzyć sumę. Inaczej byłoby bez sensu

    # Zadanie 7 

    mean_orders = round(orders["total_amount"].mean(), 2)

    print(f"średnia wszystkich zamówień to: {mean_orders}")

    # operacja mean agreguje dane
    # operacja round tylko formatuje wynik
    # ponieważ w df/series mogłoby być bez wartości, a wtedy wynik byłoby załamany. 

    # Zadanie 8 

    mean_orders_pending = round(
        orders.loc[
            orders["status"] == "pending",
            "total_amount",
        ]
        .mean(),
        2
    )

    print(f"Zamówienia z statusem pending ich średnia: {mean_orders_pending}")

    # Zadanie 9 

    minimum_order = orders["total_amount"].min()
    maximum_order = orders["total_amount"].max()

    print(f"Maximum : {maximum_order}\nMinimum: {minimum_order}")

    # B 

    maximum_record = (
            orders.sort_values(
            by=["total_amount", "order_id"],
            ascending=[False, True]
        )
        .head(1)
    )

    print(f"Maksymalny rekord : {maximum_record}")

    # Max nie rozwiązuje części B - ponieważ pokazuje jedynie najwyższą wartość, a nie najwyższy rekord 

    # Zadanie 10 

    count_orders = orders["total_amount"].count()
    sum_orders = orders["total_amount"].sum()
    mean_orders = orders["total_amount"].mean()
    min_orders = orders["total_amount"].min()
    max_orders = orders["total_amount"].max()

    print(f"Count: {count_orders}, sum: {sum_orders}, mean: {round(mean_orders, 2)}, min: {min_orders}, max: {max_orders}")

    # Zadanie 11

    amount_summary = round(orders["total_amount"].agg(["count", "sum", "mean", "max"]), 2)

    print(amount_summary)

    # Wynik jest series, ponieważ mamy kilka funkcji agregujących. Z tego jest robina series. Indeks oznacza operacja wykonana na total_amount. Bo to liczba zmienno przecinkowa

    # Zadanie 12 

    selected_amounts = round(
        orders.loc[
            (orders["status"].isin(["paid", "pending"])) & (orders["total_amount"].between(100, 500)) & (orders["city"] != "Kartuzy"),
            "total_amount"
        ]
        .agg(["count", "sum", "mean", "min", "max"]),
        2,
    )

    print(selected_amounts)

    # Weszły te rekordy które mają status paid albo pending, kwota jest między 100 a 500, a miastem nei są kartuzy
    # Każda agregacja widziała tą samą Series. 
    # Wynik rózni się agregacjami. Są wykonane operacja na liczbach. 

    returned_amounts = orders.loc[
        orders["status"] == "returned",
        "total_amount",
    ]

    print(f'''
Operacja len - {len(returned_amounts)}\n
Operacja Count - {returned_amounts.count()}\n
Operacja sum - {returned_amounts.sum()}\n
Operacja Sum Min Count - {returned_amounts.sum(min_count=1)}\n
Operacja mean - {returned_amounts.mean()}\n
Operacja min - {returned_amounts.min()}\n
Operacja max - {returned_amounts.max()}\n

''')

    # Min Count zmienia to, że wymagana jest przynajmniej jakaś wartość. W naszym wypadku było to 1. 
    # sum nie mogliśmy obliczyć w SQLu 
    # Bo 0.0 to zero, a NaN to nie możność policzenia. 
    # Nie, nie jest to to samo. Wyniki byłyby 1,1,0.0,0.0,0,0,0. 

    # Zadanie 14 

    test_amounts = pd.Series([100.0, None, 250, None])

    print(f'''
Operacja len - {len(test_amounts)}\n
Operacja Count - {test_amounts.count()}\n
Operacja sum - {test_amounts.sum()}\n
Operacja Sum Min Count - {test_amounts.sum(min_count=1)}\n
Operacja mean - {test_amounts.mean()}\n
Operacja min - {test_amounts.min()}\n
Operacja max - {test_amounts.max()}\n
Operacja sum skipnaFalse - {test_amounts.sum(skipna=False)}\n
Operacja mean skipnaFalse - {test_amounts.mean(skipna=False)}
''')

    # Różnica polega na rekordach, które są puste - None, w tym wypadku len je liczy, count nie, size nie. 

    # Zadanie 15 

    paid_mask = orders["status"] == "paid"
    pending_mask = orders["status"] == "pending"
    cancelled_mask = orders["status"] == "cancelled"

    paid_orders = orders.loc[
        paid_mask,
        "total_amount",
    ]

    pending_orderse = orders.loc[
        pending_mask,
        "total_amount",
    ]

    cancelled_orders = orders.loc[
        cancelled_mask,
        "total_amount",
    ]

    print(f"Suma rekordów trzech statusów to {len(paid_orders) + len(pending_orderse) + len(cancelled_orders)}, a długość całego orders to {len(orders)}")

    print(f"suma kwot dla poszczególnych zamówień to {round(paid_orders.sum() + pending_orderse.sum() + cancelled_orders.sum(), 2)} a całościowe sum to : {orders["total_amount"].sum()}")

    # Pytania biznesowe 
    # 1 - Ile zamówień z statusem Paid pochodzi z gdańska albo Gdynii. 

    paid_orders_from_gdansk_or_gdynia = (
        orders.loc[
            (orders["status"] == "paid") & ((orders["city"] == "Gdańsk") | (orders["city"] == "Gdynia")),
        ]
    )

    print(f"Zamówień opłaconych z Gdańska lub z Gdyni jest {len(paid_orders_from_gdansk_or_gdynia)}")

    # 2 - Jaka jest łączna wartość zamówień które nie zostały anulowane, ale mają łączną wartość od 100 do 300 włącznie. 

    sum_not_cancelled_orders = (
        orders.loc[
            (orders["status"] != "cancelled") & (orders["total_amount"].between(100, 300)),
            "total_amount",
        ]
        .sum()
    )

    print(f"Wartość zamówień które nie zostały anulowane i mają wartość od 100 do 300 włącznie to : {sum_not_cancelled_orders}")

    # 3 - Jaka jest średnia wartość zamówień z statusem paid pochodzących z Kartuz albo Sopotu. 

    mean_orders_status_paid = (
        orders.loc[
            (orders["status"] == "paid") & (orders["city"].isin(["Kartuzy", "Sopot"])),
            "total_amount",
        ]
        .mean()
    )

    print(f"Średnia wartość zamówień z statusem paid, które są z Sopotu albo Kartuz to : {round(mean_orders_status_paid, 2)}")

    # 4 Jaka jest najniższa wartość zamówień z statusem pending pochodzących z Gdańska i Gdynii. 

    min_orders_status_pending = (
        orders.loc[
            (orders["status"] == "pending") & (orders["city"].isin(["Gdańsk", "Gdynia"])),
            "total_amount",
        ]
        .min()
    )

    print(f"Najniższa wartość przy tej konfiguracji to : {min_orders_status_pending}")

    # Jaka jest najwyższa wartość z trzema warunkami - status - pending/cancelled, Kartuzy/Sopotu, Kwota 50-350

    max_orders_many_statuses = (
        orders.loc[
            (orders["status"].isin(["pending", "cancelled"])) & (orders["city"].isin(["Kartuzy", "Sopot"])) & (orders["total_amount"].between(50, 350)),
            "total_amount",
        ]
        .max()
    )

    print(f"Ta skomplikowana operacja, jego najwyższa kwota to: {max_orders_many_statuses}")

    # Zadanie dodatkowe 

    # A - Suma, suma wszystkich total_amount, Skalar, nie zostaje 
    # B - Też suma, suma wszystkich total_amount z statusem cancelled, skalar, nie 
    # C - najniższa kwota i najwyższa kwota, najniższa i najwyższa kwota w total_amount po filtracji gdzie miastem jest Gdańsk albo Gdynia, Series, nie
    # D - średnia, liczba zaokrąglana do 2 miejcs po przecinku. Średnia wartość total_amount w których kwoty są od 100 do 300 włącznie, skalar, nie
    # E - suma, w tym wypadku 0.0 ponieważ nie ma takiego statusu jak unknown po którym filtrujemy. Skalar, nie zostanie.
    # F - 12 po prostu liczba, nie zmieni df.

    # Mini wyzwania diagnostyczne

    # 1 - Dostanie liczbę wszystkich rekordów - 12 
    # 2 - Nie dostanie - brakuje () przy sum.
    # 3 - Nie dostanie, poneiważ wybrał całą DF a nie tylko total_amounts
    # 4 - Tutaj kolejność jest pomylona, brakuje loc, ogólnie całościowo jest źle. Najpierw maska, potem loc, nastepnie agregacja. 
    # 5 - Otrzyma tylko wartość największego zamówienia. 
    # 6 - Będzie 0.0 w SQL dostaniemy brak wartości, a tutaj w sum 0.0 
    # 7 - całość wyrażenia powinna być opisania w round(...)
    # 8 - Chyba dobrze . 

    # QUIZ 

    # 1 - C
    # 2 - B
    # 3 - A 
    # 4 - B
    # 5 - C 

if __name__ == "__main__":
    main()