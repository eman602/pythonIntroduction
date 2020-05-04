def near_function(letter1, letter2):
    first_word= list(letter1)
    second_word=list(letter2)
    


    for i in range(len(first_word)):
        letter = first_word[i]
        del first_word[i]
        print(first_word, i,letter)
        if first_word==second_word:
            return True
        first_word.insert(i,letter)
            
            
            
    return False

print(near_function("dragoon", "dragon"))