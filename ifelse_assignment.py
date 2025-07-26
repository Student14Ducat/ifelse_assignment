#python assignment 
# if else (conditional statement)

# (1)program to calculate the electricity bill

units=int(input("enter used electricity unit:  "))

if units<= 100:
    bill=0

if units >100 and units <= 200:
   bill=(units-100)*5
if units>200:
    bill=100*5
    bill=(units-200)*10
print("total electricity bill: rupees",bill)  

#OUTPUT--->
# enter used electricity unit:  500
# total electricity bill: rupees 3000

#enter used electricity unit:  90
#total electricity bill: rupees 0

#enter used electricity unit:  150
#total electricity bill: rupees 250



#(2)program to calculate percentage

percentage=float(input("enter your percentage: "))

if percentage>90:
    print("your grade: A ")
if percentage>80 and percentage<=90:  
     print("your grade: B ")
if percentage>60 and percentage<=80:
      print("your grade: C ")
if percentage<60:          
      print("your grade: D ")

#OUTPUT--->
#enter your percentage: 88.99
#your grade: B 

#enter your percentage: 33
#your grade: D 

#(3)youngest age program
age1=int(input("enter the age of person 1:  "))
age2=int(input("enter the age of person 2:  "))
age3=int(input("enter the age of person 3:  "))
age4=int(input("enter the age of person 4:  "))

youngest=age1

if age2<youngest:
     youngest=age2
if age3<youngest:
     youngest=age3
if age4<youngest:
     youngest=age4 

print("the youngest person age is: " ,youngest)

#OUTPUT-->
#enter the age of person 1:  20
#enter the age of person 2:  23
#enter the age of person 3:  27
#enter the age of person 4:  30
#the youngest person age is:  20


#(4) calculate bonus,salary of a company

salary=float(input("enter your salary: "))
years=float(input("enter your years: "))

if years>10:
     bonus=0.10*salary
if years>=6 and years<=10:
     bonus=0.08*salary
if years<6:
     bonus=0.05*salary

print("your bonus is: ",bonus)

#OUTPUT--->
#enter your salary: 20000
#enter your years: 8
#your bonus is:  1600.0

#(5) second largest number
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
numbers = [a, b, c]
numbers.sort()
print("this is a second largest number",numbers[1])

#OUTPUT-->
#enter first number: 22
#enter second number: 33
#enter third number: 11
#this is a second largest number 22


#(6) calculate the net amount

price=int(input("enter the market price: "))

if price>10000:
     discount=0.20*price
if price > 7000 and price<= 10000:
     discount=0.15*price
if price<=7000:
     discount=0.10*price  
net_amount=price-discount
print("discount:rupees ",discount)
print("net amount:rupees ",net_amount )

#OUTPUT--->
#enter the market price: 5000
#discount:rupees  500.0
#net amount:rupees  4500.0

#(7)calculate marks

english=int(input("enter english marks: "))
math=int(input("enter math marks: "))
science=int(input("enter science marks: "))
sst=int(input("enter social studies  marks: "))

if english>80 and math>80 and science>80 and sst>80:
     stream="science stream"
elif english>80 and math>50 and science>50:
     stream="commerce stream"
elif english>80 and sst>80:
     stream="humanities stream"   
else:
     stream="no stream"
print("student belong to the : ",stream)                 

#OUTPUT--->
#enter english marks: 85
#enter math marks: 90
#enter science marks: 88
#enter social studies  marks: 92
#student belong to the :  science stream

#(8) a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"

num=int(input("enter the number: "))
if (num%5==0):
     print("Hello")
else:
     print("Bye")    

#OUTPUT--->
# enter the number: 55
#Hello

# enter the number: 22
# Bye


#(9)a program to check whether the last digit of a number(entered by user) is divisible by 3 or not
 
# Ask user to enter a number
num = int(input("Enter any number: "))
last_digit = num % 10

if last_digit % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")

#OUTPUT-->
#Enter any number: 776
#Last digit is divisible by 3

#Enter any number: 342
#ast digit is not divisible by 3

#(10)program to check whether a number entered is three-digit number or not

num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("It is a three-digit number.")
else:
    print("It is NOT a three-digit number.")

#OUTPUT--->
# Enter a number: 877
#It is a three-digit number.    