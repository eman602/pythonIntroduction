#Question 10
def enter_a_number(number, choice):
    if choice=="double":
        return number+number
    if choice=="triple":
        return number+number+number

print(enter_a_number(10,"double"))

