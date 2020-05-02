count=0


my_list=[]
new_list=[]
for i in range (1,3000000):
    my_list.append(i)
    prime=0
    for n in my_list:
        if i%n==0:
            prime+=1

            #print(i,n,prime)
            if prime<=2:
                new_list.append(n)
                another=set(new_list)
                another.remove(1)

                count+=1
                print(count)


#print(another)
print(len(another))