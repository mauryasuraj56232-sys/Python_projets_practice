def welcome (func):
	def wrapper ():
		print('WELCOME')
		func()
		print('FINISH')
	return wrapper


@welcome
def student_result():
	student = []
	marks = []
	
	print("Subject 1 = Maths")
	print("Subject 2 = Science")
	print("Subject 3 = English")
	
	s = int(input("Enter how many students? "))
	
	for i in range(s):
	    student_name = input("Enter student name: ")
	
	    student_marks = []
	
	    for n in range(3):
	        mark = int(input(f"Enter marks of subject {n+1}: "))
	
	        if mark < 0 or mark > 100:
	            print("Invalid marks!")
	            break
	
	        student_marks.append(mark)
	
	    else:
	        student.append(student_name)
	        marks.append(student_marks)
	
	print("\nStudents:", student)
	print("Marks:", marks)
	
	
	def search():
	    """Search student and print marks, percentage and grade"""
	
	    student_search = input("\nEnter student name to search: ")
	
	    if student_search in student:
	        index = student.index(student_search)
	
	        print(f"\nStudent Found: {student[index]}")
	        print(f"Marks: {marks[index]}")
	
	        obtain_marks = sum(marks[index])
	        total_marks = len(marks[index]) * 100
	        percentage = (obtain_marks / total_marks) * 100
	
	        print(f"Percentage: {percentage:.2f}%")
	
	        if percentage >= 90:
	            print("Grade: A")
	
	        elif percentage >= 75:
	            print("Grade: B")
	
	        elif percentage >= 60:
	            print("Grade: C")
	
	        elif percentage >= 40:
	            print("Grade: D")
	
	        else:
	            print("Grade: Fail")
	
	    else:
	        print("Student not found!")
	
	
	search()
	
student_result()