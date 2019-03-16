#re-defining regualar expression import re module

import re

#Method
# match-- match operation at the starting of the string and create match if finds any pattern..
# search--
# findall
# compile

#654 645-5453


#\d-digits
#\w-alphanumeric
#{}-specifing the length

# r'\d{3} \d{3}-\d{4}'


# match1=re.match(r'\d{3} \d{3}-\d{4}','425 873-5463This is my mobile number 423 657-6453')
# print(match1)
# print(match1.group())

#find the 1st pattern it matches at any location in the string..
# match2=re.search(r'\d{3} \d{3}-\d{4}','This is my 535 758-5352mobile number 423 657-6453')
# print(match2)
# print(match2.group())

#find all the matches with pattern and return in a list
# match3=re.findall(r'\d{3} \d{3}-\d{4}','This is my 535 758-5352mobile number 423 657-6453')
# print(match3)


#compile---

pattern=re.compile(r'\d{3} \d{3}-\d{4}')
print(pattern)


# match1=pattern.match('892 039-6362This is my munber 524 752-5362')
# print(match1)
# print(match1.group())


match2=pattern.search('This is my munber 524 752-5362')
print(match2)
print(match2.group())


match3=pattern.findall('892 039-6362This is my munber 524 752-5362')
print(match3)
# print(match1.group())