print('=================Task10.1==============')
def prime():
    a=int(input('Enter the number:\n'))
    if a > 1:
            for n in range(2, a):
                if (a % n == 0):
                    print(a,"is not prime")
                    break
                else:
                    print(a,"is prime")

prime()
#Even function
def even():
    b = int(input("enter the number:\n"))
    for i in range(2,b):
        if (b%2==0):
            print(b,'is even function')
            break
        else:
            print(b,"is not even")
even()
#odd function
def odd():
    c = int(input('enter the number\n'))
    for x in range(2,c):
        if (c%2)==0:
            print(c,"is not odd number")
        else:
            print(c,"is odd number\n")
odd()
def mix(num):
    if (num%2)==0:
        print(num,"is even function")
    else:

        print(num,"is odd number")
    for n in range(2, num):
                if (num % n == 0):
                    print(num,"is not prime")
                    break
                else:
                    print(num,"is prime")
    if num>0:
        print(num,"is positive integer")
    else:print(num,"is negative")
mix(4)