#Inheritance--Child class getting properties from parent class
#Single inheritance
# class Parent:
# 	a=15
# 	def data(self):
# 		return 12+Parent.a

# class Child(Parent):
# 	b=45
# 	a=23
# 	def data1(self):
# 		return 76-45
# obj=Child()
# print(obj.b)
# print(obj.a)
# print(obj.data())

#Multiple Inheritance--Single class getting properties from multiple classes
# class First:
# 	course="Python"
# 	def data(self):
# 		return "{} is trending".format(self.course)

# class Second:
# 	# course="django"
# 	def data(self):
# 		return"trending course is {}".format(self.course)
# class Third(Second,First):
# 	# course="devops"
# 	pass

# obj=Third()
# print(obj.course)
# print(obj.data())


#Multilevel Inheritance

# class First:
# 	course="Python"
# 	def data(self):
# 		return "{} is trending".format(self.course)

# class Second(First):
# 	course="django"
# 	# def data(self):
# 	# 	return"trending course is {}".format(self.course)
# class Third(Second):
# 	# course="devops"
# 	pass

# obj=Third()
# obj1=Second()
# obj2=First()
# print(obj.course)
# print(obj.data())

# print(issubclass(Third,First))

# print(issubclass(First,Second))

# print(isinstance(obj2,Third))
# print(isinstance(obj1,First))


#Method Overloading--Not supported in Python
# class First:
# 	# def addition(self,c,d,e):
# 	# 	self.c=c
# 	# 	self.d=d
# 	# 	self.e=e
# 	# 	return self.c+self.d+self.e
# 	# def addition(self,a,b):
# 	# 	self.a=a
# 	# 	self.b=b
# 	# 	return self.a+self.b

# 	def addition(self,*b):
# 		count=0
# 		for i in b:
# 			count=count+i
# 		return count

# obj=First()
# print(obj.addition(3,4,5,6))
# print(obj.addition(3,4,5))
# print(obj.addition(3,4))

