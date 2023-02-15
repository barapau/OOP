#StudentProgram
import studentClass as sc 

studentid = 1001
name = 'John'
dob = '10/11/2001'
classification = 'junior'

#create an instance
student1 = sc.Student(studentid, name, dob, classification)

student1.calc_age()
student1.calc_register()

print(f"Student age is: {student1.get_age()}")
print(f"Student can register between is: {student1.get_register()}")