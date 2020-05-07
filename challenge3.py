def wordorganiser():
    amount=int(input("how many words do you want to enter? "))
    number=0
    my_list=[]
    while number<amount:
        word=str(input("please enter words: "))
        my_list.append(word)
        my_list.sort()
        number+=1
    print(my_list)

wordorganiser()