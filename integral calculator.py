import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import sys
import math
from math import *
print("""1) Find logarithmic values of numbers.
2) Find integral of a function.
3) Find the derivative of a function.""")
choice=int(input("What operation would you like to go with: "))
if choice==1:
    c=int(input("Which number's log value would you like to find out: "))
    d=int(input("What should be the base of the logarithm: "))
    print("The log value of",c,"to the base",d,"is",end = " ")
    print(math.log(c,d))

elif choice==2:
    N=int(input("Enter the amount of rectangles you want to be made inside the graph: "))
    a=float(input("Enter the lower limit: "))
    b=float(input("Enter the upper limit: "))
    def Integrate(N,a,b):
        def f(x):
            return sin(x)* sin(x) #Enter the function you want to integrate here
        value=0
        value2=0
        for n in range(1,N+1):
            value += f(a+((n-(1/2))*((b-a)/N)))
        value2=((b-a)/N)*value
        return value2
    print("Your answer is: ")
    print(Integrate(N,a,b))

elif choice==3:
    def function(x):
        return 4*x*x #Enter the function you want to find the derivative of here
    def deriv(x):
        return derivative(function,x)
    y=np.linspace(-5,5)
    plt.plot(y,function(y), color='green',label="Function")
    plt.plot(y,deriv(y),color='black',label="Derivative")
    plt.legend(loc='upper right')
    plt.show()
    
else:
    print("Incorrect input given!!")
    sys.exit()