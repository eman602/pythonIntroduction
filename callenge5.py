import random
def random_numbers():
    
    my_numbers=[]
    for i in range(100):
        number = random.randint(100,200)
        if number%2==0 and len(my_numbers)<5:
            my_numbers.append(number)
            
    print(my_numbers)

random_numbers()