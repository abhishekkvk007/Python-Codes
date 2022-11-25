print("***************************           Welcome to The Zodiac Calculator         **************************")
print("Enter the number1: ")
num1=int(input())
print("Enter the number2 : ")
num2=int(input())
print("These are the operators you can use")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    print("This is a Addition Operation")
    print("The sum of the two numbers is :",num1+num2)
if operator=="2":
    print("This is a Subtraction Operation")
    print("The difference of the two numbers is :",num1-num2)
if operator=="3":
    print("This is a Multiplication Operation")
    print("The product of the two numbers is :",num1*num2)
if operator=="4":
    print("This is a Division Operation")
    print("The Divident of the two numbers is :",num1/num2)
if operator=="5":
    print("This is a Modulus Operation")
    print("The Mod of the two numbers is :",num1%num2)




