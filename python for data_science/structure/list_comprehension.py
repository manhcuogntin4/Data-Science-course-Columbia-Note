import random
list=[i**2 for i in range(0,10)]
print list
list_2=[random.randint(0,5) for i in range(0,10)]
print list_2

dict={i:i**2 for i in range(0,10)}
print dict

dict={i: chr(i) for i in range(65,91)}
print dict