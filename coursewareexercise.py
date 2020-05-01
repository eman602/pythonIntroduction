def entergrade():
    grade =int(input("please enter your grade:"))

    if grade>=85:
        print("your grade of %d, is a distinction" %grade)

    elif grade>65 and grade<85:
        print("your grade of %d, is a pass" %grade)

    else:
        print("fail")

def awasome_names():
    i=0
    while i<5:
        name = str(input("please enter your name"))
        print(name, "awasome")
        i+=1
