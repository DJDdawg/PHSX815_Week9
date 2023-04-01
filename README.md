# PHSX815_Week9

This week continued with minimizing functions, but this time in 3D (or any dimension greater than one). 

The function analyzed in **Minimize3D.py** is $f(x,y) = ax^2 + bx^2 + cxy + d$. 

An analytical solution can be found by taking the gradient and setting it equal to 0.

$\nabla f = (2ax + cy, cx + 2by) = (0, 0)$.

Solving this system of equations only give the trivial solution (0, 0).

A minimimum exists for this function only if $4ab > c^2$.
