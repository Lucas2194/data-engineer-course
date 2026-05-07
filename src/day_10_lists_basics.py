products = ['orders.csv', 'orders_one.csv', 'orders_two.csv']
print(products)
count = 0

for i in products:
    print(i)

print(products[0])
print(products[-1])
print(len(products))
products.append('orders_three.csv')
print(products)

if 'orders.csv' in products:
    print('orders.csv jest na liście')
else:
    print('Nie ma orders.csv na liście')

    