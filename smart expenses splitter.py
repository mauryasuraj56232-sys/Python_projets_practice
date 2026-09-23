num_person = int(input('Enter the number of person ? '))

person = { }
for _ in range(num_person):
	person_name = input(f'Enter the person name ? ' )
	
	person[person_name] = 0
	
num_expense = int(input('How many expenese ? '))

if num_expense <= 50:

	for i in range(num_expense):
		paid_name = input('Enter name who paid ? ')
		paid_value = int(input('How much paid ? '))
		if paid_name in person:
			person[paid_name] = person[paid_name] + paid_value
			print(person)
	

		else:
			print('Invalid person')
		
else:
	print('Invalid number of person')
	
total = 0

for _ in person.values():
	total = total + _
	
print('======TOTAL======')
print(total)


fair_amount = total / num_person
print('======FAIR AMOUNT======')
print(fair_amount)

print('======BALANCE======')

balance = { }

for name,amount in person.items():
	single_fair_amount = amount - fair_amount
	
	balance[name] = single_fair_amount
	print(balance)
	
Creditors = { }
Debtors = { }

for name_person,total_balance in balance.items():
	if total_balance > 0:
		Creditors[name_person] = total_balance
		print(Creditors)
		
	elif total_balance < 0:
		Debtors[name_person] = total_balance
		print(Debtors)
		
	else:
		print(name_person,total_balance)
		
		
print('======TRANSACTION======')
total_transaction = [ ]

for debtor_name, debtor_amount in Debtors.items():
	for creditor_name, creditor_amount in Creditors.items():
		debtor_positive = abs(debtor_amount)
		
		transaction = min(debtor_positive,creditor_amount)
		
		total_transaction.append((debtor_name,creditor_name,transaction))
		
	print(total_transaction)
			
		
	remaining_debt = debtor_positive - transaction
	
	remaining_credit = creditor_amount - transaction
	
	
	Debtors[debtor_name] = remaining_debt
	
	Creditors[creditor_name] = remaining_credit
	
	if remaining_debt == 0:
		print(' Debtors payment complete')
		break
		
	elif remaining_credit == 0:
		print('creditor payment complete')
		
	else:
		print('payment is not done ')