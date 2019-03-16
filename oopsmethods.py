#instance method--Contains self as default argument and can be accessed only with the object is called instance method

#class method
#static method

class Sample:
	a=12

	# def __init__(self,a):
	# 	self.a=a
	# 	pass
	def data(self,name,age):#instance method
		self.name=name
		return "{} has {} years".format(name,age)

	def data1(self,address):
		return "{} is from {}".format(self.name,address)

	@classmethod #Decorator #classnethod
	def data2(cls,company,location):
		cls.company=company
		return "{} is at {}".format(company,location)

	def data3(cls,branch):
		return "{} has subbranch at {}".format(cls.company,branch)

	@staticmethod
	def data4(player,sports):
		return "{}{} plays {}".format(Sample.a,player,sports)

obj=Sample()
# print(obj.a)
# print(obj.data('Ramesh',23))

# print(Sample.data('Ramesh',23))
# print(obj.data1('Hyderabad'))

# print(obj.data2("Accenture",'Kondapur'))
# print(Sample.data2("Microsoft",'DLF'))
# print(obj.data3('Uppal'))

# print(obj.a) #instance attribute
# print(Sample.a) #class Attribute
print(obj.data4('Sachin','cricket'))
print(Sample.data4('Dhoni','cricket'))