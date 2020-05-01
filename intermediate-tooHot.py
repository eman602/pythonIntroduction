def too_hot(temperature, isSummer):
    isSummer = True
    if temperature>60 and temperature<100 and isSummer:
        return True
    elif isSummer==False and temperature>60 and temperature<90:
        return True
    else:
        return False

print(too_hot(1001, True))