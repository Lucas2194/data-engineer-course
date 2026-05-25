def build_validation_report(total_count, valid_count, invalid_count, errors):
    
    # Budujemy bazowy tekst używając potrójnych cudzysłowów
    report = f"""! --- Raport walidacji pliku CSV --- !

Liczba wszystkich zamówień to: {total_count}
Liczba zamówień poprawnych to: {valid_count}
Liczba zamówień błędnych to: {invalid_count}

--- Szczegóły błędów ---
"""

    # Dołączamy błędy do raportu (jeśli jakieś są)
    if not errors:
        report += "Plik jest w 100% poprawny. Brak błędów!\n"
    else:
        for error in errors:
            report += f"- {error}\n"  # Każdy błąd w nowej linijce od myślnika

    # ZWRACAMY cały zbudowany tekst, żeby główny program mógł go np. zapisać do pliku
    return report