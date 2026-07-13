mobile = { }

a = int(input('Enter how much mobile you want to add in stock ? '))

for i in range(a):
	mobile_name = input('Enter the mobile name ? ')

	mobile_price = int(input('Enter the mobile price ? '))
	
	mobile[mobile_name] = mobile_price
	
print(mobile)

mobile_search = input('Enter the mobile name for search ? ')


if mobile_search in mobile:
	print(f'mobile found {mobile_search , mobile_price}')
	
else:
	print('Sorry not there in stock')

update_mobile_name = input('Enter the name of mobile to update the price ? ')

update_price = int(input('Enter the New price to update the mobile price ? '))


if update_mobile_name in mobile:
    mobile[update_mobile_name] = update_price
    print("Price updated")
else:
    print('Sorry not there in stock')


mobile[update_mobile_name] = update_price

print(mobile)


total = sum(mobile.values())
print(total)
