# A program that allows the user to input the sides of any triangle, and then
# return whether the triangle is a Pythagorean Triple or not
start = True
count = 0

while start:
    if count == 0:
        question = input("Do you want to begin? Y/N: ")
        play = question[0]
    if play.upper()!='Y':
        start = False
        break

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

    question = input("Do you want to try another? Y/N: ")
    play = question[0]
    if play.upper() != 'N':
        start = True
    else:
        start = False
        break

    count+=1
