print('===============task6.4==============')
#Design a BMI system in US
def us():
   w = float(input('please enter your weight in kgs'))
   h = float(input('please enter your height in feet'))
   print('your body mass index in us is',(w/(h**2)*703))
us()
# Design a BMI system in metric
def bmi():
     weight = float(input('enter your weight in kgs'))
     height = float(input('enter your height in cm'))
     print('your body mass index in metric is ',(weight/(height**2)))
bmi()
