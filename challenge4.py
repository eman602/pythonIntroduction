
def even_numbers():
    
    number = int(input("Please enter a number between 1000 and 3000: "))
    even=[]
    if number>1000 and number<3000:
        for num in range(1000,number):
            if num%2==0:
                even.append(num)
        print(even)
    else:
        return even_numbers()

even_numbers()

