# A program that allows the user to input the sides of any triangle, and then
# return whether the triangle is a Pythagorean Triple or not

while True:
    question = input("Do you want to continue? Y/N: ")
    if question.upper() != 'Y' and question.upper() != 'N':
        print("Please type Y or N")
    elif question.upper() == 'Y':
        a = input("Please enter the opposite value: ")
        print("you entered " + a)

        b = input("Please enter the adjacent value: ")
        print("you entered " + b)

        c = input("Please enter the hypotenuse value: ")
        print("you entered " + c)

        if int(a) ** 2 + int(b) ** 2 == int(c) ** 2:
            print("The triangle is a pythagorean triangle")
        else:
            print("The triangle is not a pythagorean triangle")
    else:
        break


