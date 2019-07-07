'''
	tutorials from corey schafer, https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

	a class is a blueprint for creating instances/object

	methods are basically functions defined in a class

	to define an empty class leave it with the pass parameter
		class Employee:
			pass
'''

class Employee:
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay
		self.email = fname + "." + lname + "@mail.com"

	def fullName(self):
		return '{} {} {}'.format(self.fname, self.lname, self.email)

emp_1 = Employee("Ngugi", "Ephy", 120000)
emp_2 = Employee("Tony", "Stark", 1200000)

# print(emp_1.email)
# print(emp_2.email)

print(emp_1.fullName())