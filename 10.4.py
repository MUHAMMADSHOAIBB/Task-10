print('================Task 10.4=======================')
import math
def radius():
    print('Calculate the radius o a circle')
#formula of radius of a circle is:r = c/2PI
user= int(input("eneter the value of c:\n"))
r = user/2*math.pi
print("the radius of circle is:",r)
# diamter of circle
#formula of diameter of circle is d = 2*radius
r = int(input('enter the value of radius:'))
d = 2*r
print("the value of radius is:",d)