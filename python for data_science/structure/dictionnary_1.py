#Dictionnary holds key, value pair. Key cannot change (immutable). Dictionary is very fast for doing looking up
#Dictionnary is one of the most useful data structure in Python
dict={("Hanoi", 1998):6, ("Saigon", 2000):8}
print dict
print dict[("Hanoi", 1998)]
print len(dict)
#We can change the value but cannot change the key
dict[(("Hanoi", 1998))]=9
print dict
#To append to dict 
dict[("Car", 2000)]=7
print dict

#To verify if the key is in the dict
x=dict.get(("Car", 2000))
print x
x=dict.get(("Tar", 2000))
print x

x= ("Tar", 2000) in dict
print x
# Delete item in dictionary
print dict.pop(("Car", 2000))
print dict

del(dict[("Hanoi", 1998)])
print dict

# access item in dict
for i in dict: #print only key
	print i
for key, value in dict.items():
	print key
	print value