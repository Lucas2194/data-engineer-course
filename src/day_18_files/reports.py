def build_errors_report(errors):
    
    report = '! --- Raport Walidacji --- !\n'

    if not errors:
        report += 'Brak błędów\n'
    else:
        for error in errors:
            report += f'- {error}\n'
    
    return report

def build_summary_report(orders, errors):
    
    report = ' ! --- Podsumowanie --- !\n'

    report += f'Liczba wszystkich zamówień to : {len(orders)}\n'
    report += f'Liczba błędów to : {len(errors)}\n'

    if not errors:
        report += 'Brak błędów'
    else:
        report += 'Dane wymagają poprawy'

    return report
    
            
