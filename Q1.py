def a_fun():
 	global name
name= 'A'
a_fun()
print (name)
def b_fun():
 	global name
name = 'B'
b_fun()
print (name)

'''
output:-
A
B
'''