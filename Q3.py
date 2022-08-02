a_var = 10
b_var = 15
e_var = 25
d_var = 100
def a_func(a_var):
 print("in a_func a_var =", a_var)
b_var = 100 + a_var
d_var = 2 * a_var
print("in a_func b_var =", b_var)
print("in a_func d_var =", d_var)
print("in a_func e_var =", e_var)
b_var= b_var + 10
c_var = a_func(b_var)
print("a_var =", a_var)
print("b_var =", b_var)
print("c_var =", c_var)
print("d_var =", d_var)

'''
Output:-
in a_func b_var = 110
in a_func d_var = 20
in a_func e_var = 25
in a_func a_var = 120
a_var = 10
b_var = 120
c_var = None
d_var = 20
'''