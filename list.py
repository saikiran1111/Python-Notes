a=[4,7.8,"python",[4,5,6]]

# print([1,2,3]+[4,5,6])
# print([1,2,3]*4)
#Accessing elements in list is by using indexing

# print(a[2])
# print(a[0:3])
# print(a[0:4:2])

# print(a[2][3])

# a[2]="program"
# print(a)

# del a[3][1]
# print(a)

# a[0:3]=['a','b','c','d','e']
# print(a)

# del a[0:4]
# print(a)

a=[3,4,5,6,3,"python",[11,12,13,14]]

# a.append(25)

# print(a)

# a.append([45,55,65])

# print(a)

# a.extend('hyderabad')

# print(a)

# a.extend([75,85,95])

# print(a)

# a.insert(4,'count')

# print(a)

#removing elements

# print(a.remove(6))

# print(a)

# print(a.pop(3))

# print(a)

# a.clear()

# print(a)

# print(a.count(3))

# print(a.index(3))
# print(max(a))
# print(min(a))


# a.sort()

# print(a)
# a.sort(reverse=True)

# print(a)
# a.reverse()
# # print(a)

# b=a
# print(a)
# print(b)
# b.append(9)
# print(a)
# print(b)

# b=a.copy()
# print(a)
# print(b)
# b.append(9)
# print(a)
# print(b)
b=[]
for i in range(2,50):
	if i%2==0:
		b.append(i)
	else:
		b.append(i*3)

print(b)

#List comprehension

print([i if i%2==0 else i*3 for i in range(2,50)])

