## excersicse for try and except programm to keep it from crashing

data_valid = False
while data_valid == False:
	grade1 = input("Type the grade of the first test:")
	try:
		grade1 = float(grade1)
	except:
		print("invalid input. Only Number are accepted. Decimal should be seperated with a dot.")
		continue
	if grade1 < 0 or grade1 > 10:
		print("This is Grade should be between 0 and 10")
		continue
	else:
		data_valid = True
		
data_valid = False
while data_valid == False:
	grade2 = input("Type the grade of the second test")
	try:
		grade2 = float(grade2)
	except:
		print("invalid input. Only Number are accepted. Decimal should be seperated with a dot.")
		continue
	if grade2 < 0 or grade2 > 10:
		print("Grade should be 0 and 10")
		continue
	else:
		data_valid = True
		
data_valid = False
while data_valid == False:
	total_number_of_classe = input("Total number of classes: ")
	try:
		total_number_of_classe = int(total_number_of_classe)
	except:
		print("invalid input. Only Number are accepted.")
		continue
	if total_number_of_classe <=0:
		print("Total number of classes cannot be less then zero")
		continue
	else: 
		data_valid = True

data_valid = False
while data_valid == False:
	absences = input("Number of days your are absent")
	try:
		absences = int(absences)
	except:
		print("only integer values are excepted")
		continue
	if absences < 0  or absences > total_number_of_classe:
		print("The number of absence cannot be less then zero or greater then the number of total classes")
		continue
	else:
		data_valid = True
	
averg_grade = (grade1 + grade2)/2
attendence =  (total_number_of_classe - absences) /total_number_of_classe

print("Average grade:", round(averg_grade,2))
print("Attendance rate:", str(round((attendence * 100),2))+'%')

if (averg_grade >= 6 and attendence >= 0.8):
	print("The student has been approved")
elif (averg_grade < 6 and attendence < 0.8):
	print("The student has failed due to average grade ceriteria and less 80 percentage attendence")
elif (attendence >= 0.8):
	print("The student has failed due average rate lower then 6")
else:
	print("The student has failed due to attendence loweer rate")

		