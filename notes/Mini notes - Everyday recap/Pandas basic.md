Te pytania mogą pojawić się na pierwszej rozmowie albo zostać użyte do
sprawdzenia podstaw podczas rozmowy o projekcie.

Pytanie: czym jest Pandas?

Przykładowa odpowiedź:

Pandas to biblioteka Pythona do pracy z danymi tabelarycznymi. Udostępnia
między innymi struktury DataFrame i Series oraz narzędzia do wczytywania,
filtrowania, przekształcania i analizowania danych.

Pytanie: czym różni się DataFrame od Series?

Przykładowa odpowiedź:

Series jest strukturą jednowymiarową, często odpowiadającą jednej kolumnie.
DataFrame jest strukturą dwuwymiarową składającą się z wierszy i kolumn.

Pytanie: co sprawdzasz po wczytaniu pliku CSV?

Przykładowa odpowiedź:

Najpierw oglądam kilka pierwszych rekordów, rozmiar zbioru, nazwy kolumn,
typy danych i liczbę niepustych wartości. W Pandas mogę do tego użyć między
innymi head, shape, columns, dtypes oraz info.

Pytanie: czym różni się filtrowanie w Pandas od WHERE w SQL?

Przykładowa odpowiedź:

WHERE jest częścią zapytania wykonywanego przez silnik bazy danych. W Pandas
tworzę maskę logiczną dla wierszy DataFrame i przekazuję ją na przykład do
loc. Cel może być podobny, ale operacja wykonuje się w innym środowisku.

Pytanie: dlaczego w Pandas używamy & zamiast and?

Przykładowa odpowiedź:

Warunek dla kolumny Pandas tworzy Series wielu wartości True i False. Operator
& łączy dwie takie maski element po elemencie, natomiast zwykłe and służy do
łączenia pojedynczych wartości logicznych.

Nie ucz się tych odpowiedzi słowo w słowo. Powiedz je własnymi słowami i pokaż
na przykładzie orders.

Mini-notatka do zapamiętania

Pandas jest biblioteką Pythona do pracy z danymi tabelarycznymi.

Standardowy import to import pandas as pd.

pd.read_csv(path) wczytuje CSV i zwraca DataFrame.

DataFrame jest strukturą dwuwymiarową: ma wiersze i kolumny.

Series jest strukturą jednowymiarową i często reprezentuje jedną kolumnę.

Indeks nie musi być tym samym co biznesowy identyfikator rekordu.

head() pokazuje początek danych.

shape zwraca krotkę (liczba_wierszy, liczba_kolumn).

len(df) zwraca liczbę wierszy.

columns pokazuje nazwy kolumn.

dtypes pokazuje typ każdej kolumny.

info() daje szybki raport o strukturze DataFrame.

df["column"] zwraca Series.

df[["column"]] zwraca DataFrame.

df[["a", "b"]] wybiera kilka kolumn.

Warunek dla kolumny tworzy maskę wartości True i False.

df.loc[mask] filtruje wiersze.

df.loc[mask, ["a", "b"]] filtruje wiersze i wybiera kolumny.

W Pandas równość zapisujemy przez ==, a w SQL przez =.

Maski łączymy przez & i |, a każdy warunek umieszczamy w nawiasach.

Wynik filtrowania warto zapisywać pod opisową nazwą.

Po wczytaniu danych najpierw je kontrolujemy, a dopiero później transformujemy.