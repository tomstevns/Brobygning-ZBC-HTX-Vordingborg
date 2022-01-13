

"""Solving Two Equations for Two Unknows
Solving Two Equations for Two Unknows
Solving to equations for two unknown can be accomplished using SymPy. Consider the following set of two equations with two variables:

x+y−5=0
x−y+3=0
To solve this system of two equations for the two unknowns,
x and y
, first import the SymPy package. From the SymPy package,
the functions symbols, Eq and solve are needed."""


from sympy import symbols, Eq, solve

x, y = symbols('x y')
#Now define the two equations as SymPy equation objects.
#In [3]:
eq1 = Eq(x + y - 5)
eq2 = Eq(x - y + 3)
"""we can use SymPy's solve() function to compute the value of
x
 and
y
. The first argument passed to the solve() function is a tuple of the two equations (eq1, eq2). The second argument passed to the solve() function is a tuple of the variables we want to solve for (x, y).
In [4]:"""
solve((eq1,eq2), (x, y))
"""Out[4]:
{x: 1, y: 4}
"""
"""The solution is in the form of a Python dictionary. The dictionary keys are the variables and the dictionary values are the numerical solutions.
We can access the solution out of the solution dictionary using regular dictionary indexing.
"""
#In [5]:
sol_dict = solve((eq1,eq2), (x, y))
print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')

