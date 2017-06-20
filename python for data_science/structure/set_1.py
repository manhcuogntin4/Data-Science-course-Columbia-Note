#Set allow only unique value, set is unordered
colors=set(['blue', 'green', 'red'])
print colors
colors.add('yellow')
print colors
colors={'blue', 'green', 'red'}
print colors
colors.add('blue')
print colors
#remove an element use discard if element not exist, it does nothing but if use remove may fail
colors.discard('blue')
#colors.remove('blue')

colors_1={'green', 'black'}
colors_2=colors_1.union(colors)
both=colors_1.intersection(colors)
print colors_2
print colors
print both

colors_2=colors_1|colors
print colors_2
both=colors_1&colors
print both