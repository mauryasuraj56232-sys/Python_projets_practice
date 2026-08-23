print('======== Menu ========')

menu = {
    'cheese burger': 150,
    'veggie burger': 100,
    'cheese pizza': 170,
    'paneer pizza': 200,
    'corn pizza': 150,
    'soft drink': 70,
    'cholcolate milkshake': 70,
    'apple pie': 200,
    'ice cream': 30
}
print(menu)

order = {}

while True:

    a = input('\nEnter your order (or quit): ').strip().lower()

    if a == 'quit':
        break

    if a not in menu:
        print('Item menu mein nahi hai.')
        continue

    b = input('Enter ADD or REMOVE: ').strip().lower()

    if b == 'add':
        order[a] = menu[a]
        print('Added:', a)
        print('Order:', order)

    elif b == 'remove':
        if a in order:
            del order[a]
            print('Removed:', a)
        else:
            print('Ye item order mein nahi hai.')

    else:
        print('Please enter ADD or REMOVE.')
        
  
total = sum(order.values())
print(f'\nTotal bill is {total}')

def discount():
	discount_percentage = 10
	
	if total >= 1000:
		discount = (total * discount_percentage)/100
		
		final_price = total - discount
		print('discount',discount)
		print('final price', final_price)
	
	else:
		print('Order atlest 1000 and get 10 % discount ')
		
discount()

print(f'your order is {order}')
		