the_reader=[]
def numbertoword(number):
    less_than_20 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
             18: 'Eighteen', 19: 'Nineteen', 20:'twenty'}
    
    more_than_20 = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety', 100:'hundred'}

    more_than_100 ={1:'hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8: 'eight hundred',9:'nine hundred'}

    more_than_1000={1:'thousand', 2:'two thousand', 3:'three thousand', 4:'four thousand', 5: 'five thousand', 6:'six thousand', 7:'seven thousand',
    8:'eight thousand', 9:'nine thousand'}

    if number<=20:
        print(less_than_20[number])

    if number ==100:
        print(more_than_20[100])
    
    if number>20 and number<100:
        word= str(number)
        my_list = list(word)
        my_number=list(map(int, my_list))
        if checklength(my_number)==2:
            the_reader.append(more_than_20[my_number[0]])
            #print(more_than_20[my_number[0]])
            del my_number[0]
            the_reader.append(less_than_20[my_number[0]])
            checklength(my_number)
        print(list_to_words(the_reader))

    if number>100 and number<1000:
        word= str(number)
        my_list = list(word)
        my_number=list(map(int, my_list))
        if my_number[1]==0:
            the_reader.append(more_than_100[my_number[0]])
            del my_number[0]
            the_reader.append("and")
            del my_number[0]
            the_reader.append(less_than_20[my_number[0]])
            print(my_number)
            print(list_to_words(the_reader))
            #the_reader.append(less_than_20[my_number[0]])
        if my_number[1]==1:
            the_reader.append(more_than_100[my_number[0]])
            del my_number[0]
            the_reader.append("and")
            res=int("".join(map(str,my_number)))
            the_reader.append(less_than_20[res])
        if checklength(my_number)==3 and my_number[1]!=0 and my_number[1]!=1:
            the_reader.append(more_than_100[my_number[0]])
            #print(more_than_20[my_number[0]])
            del my_number[0]  
            the_reader.append("and")
            print(my_number)
            the_reader.append(more_than_20[my_number[0]])
            del my_number[0]
            the_reader.append(less_than_20[my_number[0]])
            #checklength(my_number)
            
        print(list_to_words(the_reader))



def checklength(list):
    return len(list)
def list_to_words(list):
    return ' '.join(list)



numbertoword(315)

