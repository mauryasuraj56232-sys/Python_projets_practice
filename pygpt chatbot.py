history = [ ]

while True:
	user = input('How can i help you ? ').lower()
	
	if user == 'hello' or user == 'hii':
		response = 'Hii! How can i help you '
		print(response)
	
	elif user == 'how are you':
		response = 'I am doing great ! Thanks for asking'
		print(response)
		
	elif user == 'what is your name':
		response = 'my name is pygpt'
		print(response)
		
	elif user == 'what can you do':
		response = 'I can answer basic question and chat with you '
		print(response)
		
	elif user == 'who created you':
		response = 'I was created as ai chatbot project'
		print(response)
		
	elif user == 'tell me a joke':
		response = 'Why do programmers prefer dark mode ? \nBecause light attract bugs !'
		print(response)
		
	elif user == 'thank you':
		response = 'you re welcome ! '
		print(response)
		
	elif user == 'bye' or user == 'exit':
		response = 'Goodbye ! have a great day'
		print(response)
		break
		
	else:
		response = 'sorry, i dont understand that question '
		print(response)
		
	history.append({'user':user,
	'bot':response

	})

print('======CONVERSATION HISTORY======\n')	
	


for chat in history:

	print('user :',chat['user'])
	print('Bot :',chat['bot'])
