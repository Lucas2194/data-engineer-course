products = {
    "product_id": 123,
    "name": "Drapak dla kota",
    "price": 149.50,
    "category": 'cats'
}

print(products)
print(products['name'])
print(products['price'])

products['stock_quantity'] = 123
print(products['stock_quantity'])