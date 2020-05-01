def is_it_a_leap_year(year):
    if year%4==0:
        print("hi")
        if year%400==0 or year%100!=0:
            print("%d is a leap year" %year)
        else:
            print("%d is not a leap year" %year)

    else:
        print("%d is not a leap year" %year)

print(is_it_a_leap_year(1845))