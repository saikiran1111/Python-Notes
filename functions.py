#set of statements that will do a specific task

#defining a fucntions

# def functionname():
# 	statement

# def addition():
# 	print(3+4+5+6)

# addition()

# def addition(a,b):
# 	print(a+b)

# addition(3,4)

# addition(5,6)

#passing arguments

#1.Default arguments

# def addition(a,b=10):
# 	print(a+b)

# addition(5)

# def addition(a=6,b=7):
# 	print(a+b)

# addition(5)

#2.Positional Arguments

# def addition(a,b,c):
# 	print(a+b*c)

# addition(5,6,7)
# addition(7,8,9)

#3.Keyword Arguments

# def addition(a,b,c):
# 	print(a+b*c)


# addition(c=4,a=12,b=23)

# # addition(3,8,b=23)

# addition(a=23,c=12,b=14)


#4.Arbitrary Positional Arguments

# def addition(*b):
# 	print(b)
# 	count=0
# 	for i in b:
# 		count=count+i
# 	print(count)

# addition(3,4,5)
# addition(6,7,8,9)
# addition(11,12,13,14,15)


#5.Arbitrary Keyword Arguments

# def addition(**b):
# 	print(b)
# 	count=0
# 	for i in b:
# 		# print(i)
# 		count=count+b[i]
# 	print(count)


# addition(a=1,c=3,d=5)
# addition(e=2,f=4,g=6,h=10)
# addition(i=11,j=12,k=13,l=14,m=15)

#Return Statement

# def addition(a,b):
# 	print(a+b)
# 	return a+b
# 	print(a+b)

# addition(4,5)


#Recursion

# def factorial(a):
# 	if a==1:
# 		return 1
# 	else:
# 		return a*factorial(a-1)

# print(factorial(5))


#lambda functions or Anonymous functions


# b=lambda x,y:x*y

# print(b(4,5))
# a=[3,4,5,6,7]
# print(list(map(lambda x:x%2==0,a)))
# print(tuple(map(lambda x:x%2==0,a)))


# print(list(filter(lambda x:x%2==1,range(2,20))))



