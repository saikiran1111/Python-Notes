# class First:
# 	def data(self,a,b,c):
# 		self.a=a
# 		self.b=b
# 		self.c=c
# 		return self.a+self.b+self.c

# class Second(First):
# 	def data(self,a,b):
# 		self.a=a
# 		self.b=b
# 		return self.a-self.b

# obj=Second()
# print(obj.data(5,6,7))

#Datahiding--Restricting the access to the data outside of class(hiding data)

# class First:
# 	a=45#public variables
# 	__b=76#private variables
# 	_c=87#
# 	def __data(self,name,age):
# 		self.name=name
# 		self.age=age
# 		return "{} has {} years {} ,{}".format(self.name,self.age,self.a,self._c)
# obj=First()
# print(obj.a)
# print(obj._First__data('ramesh','3662662'))
# # print(obj.__b)#not possible to access outside of class
# print(obj._c)

