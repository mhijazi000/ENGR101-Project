#Name: Mohammad Hijazi
#Project Title: SmartCalculator

#Description: This program is called SmartCalculator because it is more than just a Calculator, it can perform some unit conversions on inputs and it can perform arithmetics.

import time



#Opening statement to introduce the user to this program
print ("Today's Date:", time.strftime("%d/%m/%Y"))
print ("Welcome to the SmartCalculator!")
print (" ")

#Here the program tests the student's course to make sure he's eligible to use this SmartCalculator2
Course_Code = int(input("Please Enter your course code: "))
if Course_Code >= 200:  #all student in courses below 200 are not eligible to use this calculator
  print("You're eligible to use SmartCalculator")
else:
  print("Sorry! You're NOT eligible to use SmartCalculator")
  quit()

#infinite loop to keep the program runing until the user decides to exit by selecting 4
while 1:  
 print (" ")

#Here are the options availabe for the student
 Start = str(input(" Press '1' for Arithmetic Calculator \n Press '2' for Derivative Calculator\n Press '3' for Integral Calculator \n Press '4' for Characterstic Equation Calculator \n Press '5' for Binary to Digital Calculator\n Press '6' for Digital to Binary Calculator \n Press '7' for Degree Convertor\n Press '8' for Speed Convertor \n Press '9' for Factorial Calculator \n Press '10' to  EXIT\n"))
 print (" ")


#If '1' is chosen then open up the Arithmetic Calculator  
 if Start in ['1']:
  print("You're using the Arithmetic Calculator")
  First = float(input("Please ENTER the first number"))
  Operation = str(input("Please ENTER the operation Symbol"))
  Second = float(input("Please ENTER the second number"))
 
  def Add(a, b):  #Addition Function
    return a + b
    
  def Sub(a, b):  #Subtraction Function
    return a - b
    
  def Mul(a, b):  #Multiplication Function
    return a * b
    
  def Div(a, b):  #Division Function
    return a / b
    
  if Operation in ['+']:
    x = Add(First,Second)
    print("Answer: " ,First ,Operation ,Second ," = " ,x)
    print (" ")

  elif Operation in ['-']:
    x = Sub(First,Second)
    print("Answer: " ,First ,Operation ,Second ," = " ,x)
    print (" ")
  
  elif Operation in ['*', 'x']:
    x = Mul(First,Second)
    print("Answer: " ,First ,Operation ,Second ," = " ,x)
    print (" ")
   
  elif Operation in ['/']:
    x = Div(First,Second)
    print("Answer: " ,First ,Operation ,Second ," = " ,x)
    print (" ")
   
 
 
 #If '2' is chosen then open up the Derivative Calculator
 elif Start in ['2']:
  print("You're using the Derivative Calculator")
  def Term_Derv(p, q):
   if p in [0]:
    print("Derivative =",0)
  
   elif p in [1]:
    print("Derivative =",q)
  
   else:
    New_power=p - 1
    New_qo = q*p
    print("Derivative =",New_qo,"x^",New_power) 
    
  power = float(input("Enter the term's power (x^power):"))
  qo = float(input("Enter the term's Quoficient(Quoficient*x):"))

  Term_Derv(power,qo)
  
 #If '3' is chosen then open up the Integral Calculator
 elif Start in ['3']:
  print("You're using the Derivative Calculator")
  def Term_Integ(p, q):
   if p in [0]:
    print("Integral =",0)
  
   else:
    New_power=p + 1
    New_qo = (q/New_power)
    print("Integral =",New_qo,"x^",New_power,"+ C")
   
  power = float(input("Enter the term's power (x^power):"))
  qo = float(input("Enter the term's Quoficient(Quoficient*x):"))

  Term_Integ(power,qo)

 elif Start in ['9']:
   print("You're using factorial Calculator")
   def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)
   fact = int(input("Please enter the number"))
    
   fa=facto(fact)
   print(fact,"! = ",fa)
  
 #If '4' is chosen then open up the Characterstic Equation Calculator
 elif Start in ['4']:
   print("You're using the Characterstic Equation Calculator")
   def Characterstic_Equ(a,b,c):
    print("")
    print("The Given Equation:",a,"x^2 + " ,b ,"x +",c,"= 0" )
    X1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    X2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
    print("X1=",X1)
    print("X2=",X2)
  
   print("The Characterstic Equation is in the form of ax^2 + bx + c = 0")

   ayy = float(input("Please Enter a:"))
   bee= float(input("Please Enter b:"))
   cee= float(input("Please Enter c:"))

   f=Characterstic_Equ(ayy,bee,cee)
   
 #If '5' is chosen then open up the Binary to Digital Convertor
 elif Start in ['5']:
   print("You're Using the Binary to Digital Calculator")
   
   def BinToDec(b):
     decimal = 0
     for digit in b:
       decimal = decimal*2 + int(digit)
     print ("The Decimal number for",b," = ", decimal)
   
   Binary_Number = input("Enter the Binary number: ")
   BinToDec(Binary_Number)
 
 #If '6' is chosen then open up the Digital to Binary Convertor
 elif Start in ['6']:
  print("You're Using the Digital to Binary Calculator")
 
  def DecToBin(n):
    p = n
    k = []
    while (n>0):
      a = int(float(n%2))
      k.append(a)
      n = (n-a)/2
      string = ""
      for i in k[::-1]:
        string=string+str(i)
    print('The Binary number for %d is %s'%(p, string))

  Decimal_Number =int(input("Please Enter the Decimal number: "))
  DecToBin(Decimal_Number)
 #If '7' is chosen then open up the Degree Convertor
 elif Start in ['7']:
   print("You're using the Degree Convertor")  
  
   def C_to_F(a):
     return (a*1.8)+32
   def F_to_C(a):
     return (a-32)/1.8 
  
   print(" ") 
    
   Degree_Unit = str(input(" Celcius to Fahrenheit Press '1'\n Fahrenheit to Celcius Press '2'\n"))
   if Degree_Unit in ['1']:
        Degree_Value = float(input("Please ENTER the degree in  Celcius"))
        y = C_to_F(Degree_Value)
        print("Tempareture = " ,y ,"Fahrenheit")
        print (" ")
       
   elif Degree_Unit in ['2']:
        Degree_Value = float(input("Please ENTER the degree in Fahrenheit"))
        y = F_to_C(Degree_Value)
        print("Tempareture = " ,y ,"Celcius")
        print (" ")
        
 #If '8' is chosen then open up the Speed Converter      
 elif Start in ['8']:
   print("You're using the Speed Convertor")
  
   def Kmphr_to_mps(a):
     return a*0.2777
   def mps_to_Kmphr(a):
     return a/0.2777
    
   print(" ") 
    
   Speed_Unit = str(input(" Km/hr to m/s Press '1'\n m/s to km/hr Press '2'\n"))
  
   if Speed_Unit in ['1']:
        Speed_Value = float(input("Please ENTER the Speed in Km/hr "))
        z = Kmphr_to_mps(Speed_Value)
        print("Speed = " ,z ,"m/s")
        print (" ")
       
   elif Speed_Unit in ['2']:
        Speed_Value = float(input("Please ENTER the degree in m/s"))
        z = mps_to_Kmphr(Speed_Value)
        print("Speed = " ,z ,"Km/hr")
        print (" ")

  
 #If '9' is chosen then exit the program        
 elif Start in ['10']:
   quit()





