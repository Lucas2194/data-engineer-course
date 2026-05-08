product_name = "Kubek z kotem"
quantity = 3 
unit_price = 39.99
shipping_price = 14.99

products_total = quantity * unit_price
order_total = products_total + shipping_price

print(f'Produkt: {product_name}')
print(f'Liczba sztuk: {quantity}')
print(f'Cena produktów {products_total}')
print(f'Dostawa: {shipping_price}')
print(f'Razem do zapłaty {order_total}')

