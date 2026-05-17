def get_orders():
    return [
        {
            'order_id': 2001,
            'order_value': 149.99,
            'status': 'paid'
        },  # 1. Poprawne
        {
            # 2. Błąd: brak order_id
            'order_value': 25.50,
            'status': 'new'
        },
        {
            'order_id': 2003,
            # 3. Błąd: brak order_value
            'status': 'shipped'
        },
        {
            'order_id': 2004,
            'order_value': -15.00,   # 4. Błąd: order_value < 0
            'status': 'paid'
        },
        {
            'order_id': 2005,
            'order_value': 300.00
            # 5. Błąd: brak statusu
        },
        {
            'order_id': 2006,
            'order_value': 89.99,
            'status': 'zablokowane'  # 6. Błąd: niedozwolony status
        },
        {
            'order_id': 2007,
            'order_value': 0,        # 7. Błąd: order_value == 0
            'status': 'new'
        },
        {
            'order_id': 2008,
            'order_value': 999.00,
            'status': 'shipped'
        },
        {
            'order_id': 2009,
            'order_value': '249.99',
            'status': ' PAID '
        },
        {
            'order_id': 2010,
            'order_value': 'abc',
            'status': 'paid'
        },
        {
            'order_id': 2012,
            'order_value': '0',
            'status': 'cancel'
        },
        {
            'order_id' : 2013,
            'order_value': 150,
            'status': 123
        }

    ]