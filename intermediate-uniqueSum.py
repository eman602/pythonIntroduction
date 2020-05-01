number1 = int(input("please enter your first number: "))
number2 = int(input("please enter your second number: "))
number3 = int(input("please enter your third number: "))


if number1!=number2 and number1!=number3 and number2!=number3:
    my_set={number1, number2, number3}
    if len(my_set)>1:
        print(sum(my_set))
    
elif number1==number2 and number1!=number3:
    print(number3)

elif number2==number3 and number1!=number2:
    print(number1)

else:
    print(0)
