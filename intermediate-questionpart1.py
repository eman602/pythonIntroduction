number1 = int(input("please enter a number: "))
number2= int(input("Please enter a second number: "))

if number1>21 or number2>21:
    print(0)

if number1<=21 and number2<=21:
    my_list=[21, number1,number2]
    my_list.sort()
    print(my_list[1])


