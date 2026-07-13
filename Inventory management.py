inventory = [ ]

a = int(input('enter the num of product ? '))

for i in range(a):
	add = input('enter the name of product ? ')
	inventory.append(add)
	
print(inventory)

r = input('enter the product name for remove ?')


inventory.remove(r)
print(inventory)

search = input('enter the priduct name for search : ')

if search in inventory:
	print(f'found {search}')

else:
	print('not found')

	