#Minimize a function using Scipy minimize packages

#import packages
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys

def quadratic(x, y, a, b, c, d):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    z = a*x**2 + b*y**2 + c*x*y + d
    return z
    
def quadraticmin(x, y, a, b, c, d): #calculate minimum/maximum value
    a = float(a) 
    b = float(b)
    c = float(c)
    d = float(d)
    quadmin = d
    return quadmin

if __name__ == "__main__":
    
    #initialize 
    xlowerbound = -1
    xupperbound = 1
    
    ylowerbound = -1
    yupperbound = 1
    	
    a = 1 
    b = 1
    c = 1
    d = 1
    
    #4ab - c^2 > 0 for minimum to exist
    
    N = 1000
    	
    # read the user-provided seed from the command line
    if '-a' in sys.argv:
    	p = sys.argv.index('-a')
    	a = float(sys.argv[p+1])
        
    if '-b' in sys.argv:
        p = sys.argv.index('-b')
        b = float(sys.argv[p+1])
        
    if '-c' in sys.argv:
        p = sys.argv.index('-c')
        c = float(sys.argv[p+1])
        
    if '-d' in sys.argv:
        p = sys.argv.index('-d')
        d = float(sys.argv[p+1])
    
    if '-xlowerbound' in sys.argv:
        p = sys.argv.index('-xlowerbound')
        xlowerbound = float(sys.argv[p+1])
        
    if '-xupperbound' in sys.argv:
        p = sys.argv.index('-xupperbound')
        xupperbound = float(sys.argv[p+1])
        
    if '-ylowerbound' in sys.argv:
        p = sys.argv.index('-ylowerbound')
        ylowerbound = float(sys.argv[p+1])
        
    if '-yupperbound' in sys.argv:
        p = sys.argv.index('-yupperbound')
        ypperbound = float(sys.argv[p+1])
    
    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])   
        
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   -a [number]	coefficient of x^2 term.")
        print ("   -b [number]  coefficient of y^2 term")
        print ("   -c [number]  coefficiento f xy term")
        print ("   -c [number]  z-intercept")
        print ("   -xlowerbound [number]  Lower Bound of x-axis on graph")
        print ("   -xupperbound [number]  Upper Bound of x-axis on graph")
        print ("   -ylowerbound [number]  Lower Bound of y-axis on graph")
        print ("   -yupperbound [number]  Upper Bound of y-axis on graph")
        print ("   -N [number]  Number of points plotted in graph")
        print
        sys.exit(1)
    
    #create array of x and y-values
    x = np.linspace(xlowerbound, xupperbound, num=N)
    y = np.linspace(ylowerbound, yupperbound, num=N)
          
    #calculate analytical solution
    analmin =  quadraticmin(x, y, a, b, c, d)
    analx = (0, 0)
    
    print(f"The analytical minimum of the quadratic curve is z = {analmin} at (x, y) = {analx}")
    
    #Scipy Minimize
    def f(x, y):
        return a*x**2 + b*y**2 + c*x*y + d #constants are defined previously

    #plot function
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    ax.contour3D(X, Y, Z, 50, cmap='viridis')
    ax.scatter(0, 0, d, color='r')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');
    
    ax.view_init(elev=5, azim=20)

    plt.show() 
