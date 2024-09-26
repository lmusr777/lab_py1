from math import *

def task_integer7():
    "Дано двозначне число. Знайти суму і добуток його цифр"
    try:
        #input
        num = int(input("Enter two-digit number [10 .. 99]: "))
    except:
        print("Invalid integr number!")
        print("By!")
    else:
        #calculations
        d1 = num % 10
        d2 = num // 10
        sum2 = d1 + d2
        prod2 = d1 * d2
        #output
        print("Sum: ", sum2)
        print("Product: ", prod2)

def task_m3():
    "Calculate expression"
    try:
        #input
        x = float(input("Enter x: "))
    except:
        print("Invalid number!")
        print("By!")
    else:
        try:
            #calculations
            num = pow(sin(x+pi), 2) * pow(2,(1-x))
            denom = 4 * tan(fabs(x)) * sin(radians(28))
            add = 1/3 * log(fabs(x), 2)
            y = num / denom + add
        except:
            print("Calculation error!")
            print("By!")
        else:
            #output
            print("y =  ", y)


def task_boolean10():
    """ Дано два цілих числа: A, B.
    Перевірити істинність висловлювання:
    «Рівне одне з чисел A і B непарне»  """
    try:
        #input
        A = int(input("Enter number A: "))
        B = int(input("Enter number B: "))
    except:
        print("Invalid integr number!")
        print("By!")
    else:
        #calculations
        prepos = ((A%2 == 1) and (B%2 != 1)) or ((A%2 != 1) and (B%2 == 1))
        #output
        print("Exactly one number A or B is odd: ", prepos)


























        
