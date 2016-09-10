# functions

def errhandler():
    print("Your input has not been recognised")
    exit(1)


def add(num1, num2):
    return num1 + num2


def subs(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def endapp():
    print("\n the end \n")
    exit()


# main
operations = {"+", "-", "*", "/"}


def main():
    op = input('Operation to perform? (+ , - , * , / , q -> quit ) :')
    while op in operations:
        if op == 'q':
            endapp()
        else:
            """check if digit"""
            num1 = input("1st Number =  ")
            if num1 == 'q': endapp()
            while not num1.isdigit():
                if num1 == 'q': endapp()
                num1 = input("1st Number must be numeric, please reenter =  ")

            num2 = input("2nd Number =  ")
            if num2 == 'q': endapp()
            while not num2.isdigit():
                if num2 == 'q': endapp()
                num2 = input("2nd Number must be numeric, please reenter =  ")
            num1 = int(num1)
            num2 = int(num2)
            selector = {
                "+": add(num1, num2),
                "-": subs(num1, num2),
                "*": multiply(num1, num2),
                "/": divide(num1, num2)
            }
            resultado = selector.get(op)
            print('The result is  ', num1, ' ', op, ' ', num2, ' = ', resultado)
            # print('The result is  %d %s %d %s = ' % num1,op,num2,resultado)
            return


main()
