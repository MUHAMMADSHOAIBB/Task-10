print('=================Task10.5=======================')
while True:
 def Atmmov():
    print("ATM Machine")
    Amount = 5000
    print('select the option 1,2,3,4')
    option = int(input('1.check balnce ,2.withdraw , 3.deposit amount,4.exit'))
    if option == 1:
        print('your current balance is:', Amount)
    elif option == 2:
        x = int(input("Enter amount to withdraw"))
        if x > Amount:
            print('Insufficient balance')
        else:
            print('Amount withdrawn successfully!')

    elif option == 3:
        y = int(input('Enter the amount you want to deposit'))
        Amount += y
        print('Amount Deposited successfully!')
        print('Your new balance is: ', Amount)
    elif option == 4:
        print('exit')
    else:
        print('Invalid choice')
 Atmmov()
