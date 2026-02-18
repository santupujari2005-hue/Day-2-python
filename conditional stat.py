#CONDITIONAL STATEMENT (if-elif-else)
#if (you can write if statement more then one time)
age=21
if(age>=18):
     print("can vote & apply for license")
if(age>19):
     print("can drive")

#elif (else if) (you can write elif statement more then one time)
light="red"
if(light=="green"):
     print("go")
elif(light=="red"):
     print("stop")
elif(light=="yellow"):
     print("wait")

print("end of code")

#else (only one time you can use else statement)
light="Blue"
if(light=="green"):
     print("go")
elif(light=="red"):
     print("stop")
elif(light=="yellow"):
     print("wait")
else:
     print("linght is brocken")

age=17
if(age>=18):
     print("can vote") #indentation
else:
     print("connot vote")
#example
marks=60
if(marks>=90):
     print("grade=A")
elif(marks>=80 and marks<90):
     print("greade=B")
elif(marks>=70 and marks<80):
     print("greade=C")
else:
     print("grade=D")

#OR you can
marks=input("enter student marks:")
marks=int(marks)
if(marks>=90):
     grade="A"
elif(marks>=80 and marks<90):
     grade="B"
elif(marks>=70 and marks<80):
     grade="C"
else:
     grade="D"

print("grade of the student->",grade)

  #NESTING:
age2=78
if(age2>=18):
     if(age2>=80):
          print("cannot drive")
     else:
          print("can dive")
else:
     print("connot drive")

#Let's Practice
#1.WAP to check if a number entered by the user is odd or even
number=input("enter a number:")
number=int(number)
if(number%2==0):
     print("Number is even")
else:
     print("number is odd")

#2.WAP to find the greatest of 3 numbers entered by the user
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
c=int(input("Enter c number:"))
if(a>b and a>c):
     print("a is greatest of 3 numbers")
elif(b>a and b>c):
     print("b is greatest of 3 numbers")
else:
     print("c is greatest of 3 numbers")
 #3.WAP to check if a number is a multiple of 7 or not.
V=int(input("Enter a number:"))
if(V%7==0):
     print("The number is multiple of 7")
else:
     print("The number is not multiple of 7")


