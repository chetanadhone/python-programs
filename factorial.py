def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


print(factorial(4))
# factorial(4) = return 4 * factorial(4-1)
#fcatorial(3) = return 3 * factorial(3-1)
#factorial(2) = return 2 * factorial(1)
#factorial(1) = return 1
#4*3*2*1 = 24
