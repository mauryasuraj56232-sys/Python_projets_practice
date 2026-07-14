import random

choices = ['rock','paper','scissors']

user_choice = input(f'Enter your choice ? {choices}')


if user_choice in choices:
	print(f'You chose {user_choice}')
	
else:
	print('chose for rock,paper,scissors')

computer_choice = random.choice(choices)

print(f'Computer chose {computer_choice}')


if user_choice == computer_choice:
	print('Tie')
	
elif user_choice == 'rock' and computer_choice == 'scissors':
	print('You win')
	
elif user_choice == 'scissors' and computer_choice == 'paper':
	print('You win')
	
elif user_choice == 'paper' and computer_choice == 'rock':
	print('You win')
	
elif computer_choice == 'paper' and user_choice == 'rock':
	print('Computer win')
	
elif computer_choice == 'scissors' and user_choice == 'paper':
	print('Computer win')
	

else:
	print('computer win')
	

print('Thank you for playing rock , paper , scissors\nGAME OVER')
	

	
