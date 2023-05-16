yn="Y"
print("menu")
while yn=="y" or yn=="Y":
    print("||||||| simple callculator ||||||||\n")
    num1 = float(input("enter 1st number:"))
    num2 = float(input("enter 2nd number:"))
    ch = int(input("enter 1 for addition :\nenter 2 for sub :\nenter 3 for mull :\nenter 4 for flore div :\nenter 5 for float div :\nenter 5 for modulus :"))
    if ch==1:
        print(num1,"+",num2,"=",num1+num2)
        yn = input("do you want to continue Y/N:")
        exit("bye bye")
    elif ch==2:
        print(num1,"-",num2,"=",num1-num2)
        yn=input("do you want to continue Y/N:")
        exit("bye bye")
    elif ch==3:
        print(num1,"*",num2,"=",num1*num2)
        yn = input("do you want to continue Y/N:")
        exit("bye bye")
    elif ch==4:
        print(num1,"//",num2,"=",num1//num2)
        yn = input("do you want to continue Y/N:")
        exit("bye bye")
    elif ch==5:
        print(num1,"/",num2,"=",num1/num2)
        yn = input("do you want to continue Y/N:")
        exit("bye bye")
    elif ch==6:
        print(num1,"%",num2,"=",num1%num2)
        yn = input("do you want to continue Y/N:")
        exit("bye bye")
    else:
        print("enter valid option\n")
        yn ="y"
