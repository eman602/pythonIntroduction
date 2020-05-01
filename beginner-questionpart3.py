#7
my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list[0])
print(len(my_list))

#8
#for i in my_list:
 #   print(i)

#9
number = int(input("please enter an integer: "))
new_list=[]

for i in my_list:
    for n in range(number):
        new_list.append(i)
        another_list=[]
        for n in new_list:
            another_list.append(n*10)

print(new_list)
print(another_list)

