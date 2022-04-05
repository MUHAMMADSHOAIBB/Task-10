# we have to write a program to solve quadratic equation
#formula of quadratic equation is: ax^2 +bx+c=0
# we have to find the value of x s0  =  −b + √(b2 − 4ac)/2a ,and −b - √(b2 − 4ac)/2a
def quad():
    a = int(input('enter the value of a'))
    b = int(input('enter the value of b'))
    c = int(input('enter the value of c'))
    x = ((-b+(b**2-4*a*c)**(1/2)/2*a))
    y = ((-b-(b**2-4*a*c)**(1/2)/2*a))
    print("the value of x is :",x,"\nThe value of y is:",y)
quad()
