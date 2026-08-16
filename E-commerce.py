cart = {}

n = int(input('Enter how much product you want to add? '))

for _ in range(n):
    product = input('\nEnter product name: ')
    product_price = int(input('Enter the product price: '))

    cart[product] = product_price


a = input('\nEnter ADD or REMOVE: ').strip().lower()

if a == 'add':
    product = input('Enter product name: ')
    product_price = int(input('Enter product price: '))

    cart[product] = product_price
    print(cart)

elif a == 'remove':
    remove_product = input('Enter the product name to remove: ')

    if remove_product in cart:
        del cart[remove_product]
        print(cart)
    else:
        print('Sorry, there is no such product to remove.')

else:
    print('Invalid choice.')
    
total_price = sum(cart.values())
print(f'Total price is {total_price}')

def discount ():
	discount_percentage = 20
	
	if total_price >= 5000:
		discount = (total_price*discount_percentage)/100
		
		final_price = total_price - discount
		
		print('Total price',total_price)
		print('Discount',discount)
		print('Final price',final_price)
		
	else:
		print('\nshoping First atlest 5000 then get 20% discount ')
		
discount()

print(cart)
		