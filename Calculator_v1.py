# import math library for mathematical operations
import math as mt

def Welcome():
    # A function to output Welcome Message at first Time
    print("******A simple Scientific calculator******")
    print("*****************Welcome*****************")

def interface():
   '''
   Function to display the interface of the calculator
   showing the possible operations and options 
   '''
   print("Choose an operation to excute : ")
   print("You can then choose number of operands to preform the operation")
   print(" 1 : Addition")
   print(" 2 : Subtraction")
   print(" 3 : Multiplication")
   print(" 4 : Division")
   print(" 5 : Modulus(i.e : X % Y)")
   print(" 6 : Power(i.e: X ^ Y)")
   print(" 7 : Factroial(i.e : X!)")
   print(" 8 : Absolute(i.e : |X|)")
   print(" 9 : root(X)")
   print(" 10 : log10(X) ")
   print(" 11 : log2(X)")
   print(" 12 : ln(X)")
   print(" 13 : Sin(x)")
   print(" 14 : Cos(x)")
   print(" 15 : tan(x)")
   print(" 16 : sec(x)")
   print(" 17 : csc(x)")
   print(" 18 : cot(x)")
#**************************************************************************************#        
#**************************************************************************************#        
#**************************************************************************************#

# Start for Definition of Functions For different Operaions

def Add():
    n = int(input("Enter no. of operands to add : "))
    if n<1 :
        print("Invalid no. of operands, Please enter +ve Real integer")
        Add()
    else :
       Sum = 0
       for i in range(n):
         N = list(map(float,input("Enter Number "+ str(i+1) + ": ").split()))
         for element in N:
             Sum+= element
       print("Total Sum of the all Numbers is : ",Sum)

def Subtract():
    n = int(input("Enter no. of operands to subtract : "))
    if n<1 :
        print("Invalid no. of operands, Please enter +ve Real integer")
        Subtract()
    else :   
        N = []
        for i in range(n):
           c = input("Enter Number "+ str(i+1) + ": ")
           N.append(float(c))
        diff = N[0]
        for j in N[1:]:
           diff = diff - j
    print("Total difference between the Numbers is : ",diff)      
    
def Mod():
    print("you will calculate the form ( x % y) :")
    x = float(input("Enter First Number x : "))
    y = float(input("Enter Second Number y : "))
    m = x%y
    print(f"The result of {x} % {y} is : ",m)

def Pow():
    print("you will calculate the form ( x ^ y) :")
    x = float(input("Enter First Number x : "))
    y = float(input("Enter Second Number y : "))
    p = x**y
    print(f"The result of {x} ^ {y} is : ",p)

def Fact():
    print("you will calculate the form X! :")
    x = float(input("Enter the Number x : "))
    fact = 1
    if x==0:
       print(f"The result of {x}! : ",fact) 
    elif (x>=1) and x.is_integer()==True:
        for i in range(1, int(x+1)):
            fact=fact*i
        print(f"The result of {x}! : ",fact)
    else:
        print("Factorial is calculated only for positive integers !!!")
        
def Root():
    x = float(input("Enter the Number to get root for it : "))
    r = float(input("Enter the order of Root (i.e : 2nd or 3rd ..) : "))
    rot = pow(x,1/r)
    if r==2:
        print(f"The square root of {x} is :{rot} ")
    elif r==3:
        print(f"The Cubic Root of {x} is :{rot} ")
    else:
        print(f"The {r}th root of {x} is :{rot} ")

def Abs():
    x = float(input("Enter the number to get absolute for it : "))
    a = abs(x)
    print("Absolute of {x} is : ",a)

def Log10():
    x = float(input("Enter the number to get Log10 for it : "))
    l = mt.log10(x)
    print("Log10 of {x} is : ",l)

def Log2():
    x = float(input("Enter the number to get Log2 for it : "))
    l = mt.log2(x)
    print("Log2 of {x} is : ",l)
    
def Ln():
    x = float(input("Enter the number to get Ln for it : "))
    l = mt.log(x)
    print("Ln of {x} is : ",l)

def Sin():
    theta = float(input("Enter the angle(in degree) to get Sine for it : "))
    thr = mt.radians(theta)
    s = mt.sin(thr)
    print("Sine of {theta} is : ",s)

def Cos():
    theta = float(input("Enter the angle(in degree) to get Cos for it : "))
    thr = mt.radians(theta)
    s = mt.cos(thr)
    print("Cos of {theta} is : ",s)

def Tan():
    theta = float(input("Enter the angle(in degree) to get Tan for it : "))
    thr = mt.radians(theta)
    s = mt.tan(thr)
    print("Tan of {theta} is : ",s)

def Sec():
    theta = float(input("Enter the angle(in degree) to get Sec for it : "))
    thr = mt.radians(theta)
    s = 1 / mt.cos(thr)
    print("Sine of {theta} is : ",s)

def Csc():
    theta = float(input("Enter the angle(in degree) to get Csc for it : "))
    thr = mt.radians(theta)
    s = 1 / mt.sin(thr)
    print("Sine of {theta} is : ",s)

def Cot():
    theta = float(input("Enter the angle(in degree) to get Cot for it : "))
    thr = mt.radians(theta)
    s = 1 / mt.tan(thr)
    print("Sine of {theta} is : ",s)

def Multiply():
    n = int(input("Enter no. of operands to Multiply : "))
    if n<1 :
        print("Invalid no. of operands, Please enter +ve Real integer")
        Multiply()
    else : 
        N = []
        for i in range(n):
           c = input("Enter Number "+ str(i+1) + ": ")
           N.append(float(c))
        res = N[0]
        for j in N[1:]:
           res = res * j
    print("Total Multiplication between the Numbers is : ",res)   
        
        
    
def Divide():
    print("Enter the Two Numbers To Divide in Form X / y : ")
    x = float(input("Enter First Number X : "))
    y = float(input("Enter Second Number y : "))
    if y==0 :
        print("Invalid,, You Cannot Divide by Zero !!!")
        Divide()
    else:
        res = x / y
        print("The division of the two numbers is : ",res)
        
#**************************************************************************************#        
#**************************************************************************************#        
#**************************************************************************************#        
        
def operations():
    '''
    Function To Take input from user and choose the operation
    to excute 
    
    '''
    op = input("Choose an Operation : ")

    if (op =='1'):
        Add()
    elif (op =='2'):
        Subtract() 
    elif (op =='3'):
        Multiply()
    elif (op =='4'):
        Divide()
    elif (op =='5'):
        Mod()
    elif (op =='6'):
        Pow()
    elif (op =='7'):
        Fact()     
    elif (op =='8'):
        Abs()     
    elif (op =='9'):
        Root()    
    elif (op =='10'):
        Log10()    
    elif (op =='11'):
        Log2()  
    elif (op =='12'):
        Ln()    
    elif (op =='13'):
        Sin()   
    elif (op =='14'):
        Cos()  
    elif (op =='15'):
        Tan()
    elif (op =='16'):
        Sec()   
    elif (op =='17'):
        Csc()    
    elif (op =='18'):
        Cot()
    else:
      print("Please Enter A Valid Choice !! ")
      operations()     
    
   
# The main function
if __name__=="__main__":
    Welcome()
    interface()
    operations()
    
    cont = True
    while cont :
        cont = input("Do you Want To continue ?(y/n) :")
        if cont=='y':
            cont = True
            operations()
        else :
            cont = False
            