import random as rand

x = rand.randrange(1,100)
UserCorrect = False

while(UserCorrect == False):
    print('Please input a number')
    user = input()
    user_int = int(user)

    if (user_int == x):
        print('Equal!')
        quit()

    if (user_int > x):
        print("Greater Than")

    if (user_int < x):
        print('Less than')




