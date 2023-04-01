# PHSX815_Week9

This week continued with minimizing functions, but this time in 3D (or any dimension greater than one). 

The function analyzed in **Minimize3D.py** is $f(x,y) = ax^2 + bx^2 + cxy + d$. 

An analytical solution can be found by taking the gradient and setting it equal to 0.

$\nabla f = (2ax + cy, cx + 2by) = (0, 0)$.

Solving this system of equations only give the trivial solution (0, 0). Plugging this back into our function gives the minimum as $z = d$. 

Note that a minimimum exists for this function only if $4ab > c^2$. Otherwise, it is a maximum.

The code file can be run with the following:

>$ python3 Minimize3D.py -N 10000

You can also mess around wit the following variables.

'-a', '-b', '-c', '-d', which are the coefficients of our quadratic curve.

'-xlowerbound', '-xupperbound', '-ylowerbound', '-yupperbound', which set the upper and lower bounds for each axis on the graph. 

The output is the following:

> The analytical minimum of the quadratic curve is z = 1.0 at (x, y) = (0, 0)

and the graph **3D Quadratic.png**

![3DQuadraticGraph.png](https://github.com/DJDdawg/PHSX815_Week9/blob/main/3D%20Quadratic.png)
