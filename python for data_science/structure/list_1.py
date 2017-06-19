list=[9,8, 11]
print list
list.append(16)
print list
list[1]=10
print list
list.pop(1)
print list
list.remove(9)
print list
list_1=[1,2,3]
list_2=[4,5,6]
#list_1.extend(list_2)
print list_1
list_2.extend(list_1)
print list_2


list_1=[1,2,3]
list_2=[4,5,6]

for x,y in zip(list_1, list_2):
	print "x=",x, "y=", y
