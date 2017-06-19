st="Hello"
print st[1:3]
print st[4:7]
print st[-4:-1]
st=st.lower()
print st
st=st.upper()
print st


st=st*2
print st
s=" Hello Viet nam    "
s=s.strip()
print s
s=s.strip("nam")
print s

s= 'Let\'s split the world'
s=s.split(' ')
print s
s= " Cuong , Bon, Na"
s=s.split(',')
print s
s= " Cuong , Bon , Na"
print "Cuong" in s 
print s.find("Cuongdqf")

# String format
statement= " We love {} {} ."
statement=statement.format("Data", "Science")
print statement

#string format 2

statement= " We love {1} {0} ."
statement=statement.format("Data", "Science")
print statement