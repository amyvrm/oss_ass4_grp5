# division of two number

def division(num1, num2):
    try:
        return num1/num2
    except Exception as e:
        return e


if __name__ == "__main__":
    print("Please enter two number for division")

    num1 = int(input("Enter number"))
    num2 = int(input("Enter number"))
    print("Division of two number is: {}".format(division(num1, num2)))
