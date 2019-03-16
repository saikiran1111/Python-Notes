# a=[3,6.7,'a',23.33,0]

# for i in a:
# 	try:
# 		print(1/i)
# 	except (TypeError,ZeroDivisionError):
# 		print("Error Occured!!!")

# 	except ZeroDivisionError:
# 		print("ZeroDivisionError Occured!!")

# 	# finally:
# 	# 	print("Finally Block")
# 	else:
# 		print("Else Block")

#try---

#Userdefined Exception
# class ValueSmallError(Exception):
# 	pass
# class ValueLargeError(Exception):
# 	pass
# num1=int(input("Enter num1 value::"))
# while True:
# 	try:
# 		num2=int(input("Enter num2 value::"))
# 		if num2>num1:
# 			raise ValueLargeError
# 		elif num2<num1:
# 			raise ValueSmallError
# 		else:
# 			print("Guessed correctly!!")
# 			break
# 	except ValueLargeError:
# 		print("Guessed Large value!!Try again!!")
# 	except ValueSmallError:
# 		print("Guessed Small value!!Try again!!")
