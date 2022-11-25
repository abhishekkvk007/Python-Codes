replace1=""
print("***************************           Welcome to The Zodiac Calculator         **************************")
flag="Print"
print("Enter the number1: ")
num1=int(input())
print("Enter the number2: ")
num2=int(input())
print("These are the operators you can use")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
result=0
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    replace1="Addition"
    result=num1+num2
if operator=="2":


    if num1<num2:
        flag="Do not print"
        print("cannot subtract the First number is less than the Second number")
    else:
        flag="Print"
        replace1="Subtraction"
        result=num1-num2
if operator=="3":
    replace1="Multiplication"
    result=num1*num2
if operator=="4":
    replace1="Division"
    result=num1//num2
if operator=="5":
    replace1="Modulus"
    result=num1%num2
if flag=="Print":
 print("The Result of",replace1,"of",num1,"and",num2,"is",result)

