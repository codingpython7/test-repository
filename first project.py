def main():
    x=10
    user = input('Please Input Number')
    user_int = int(user)

    if (user_int == x):
        print('Equal!')

    if (user_int > x):
        print("Greater Than")

    if (user_int < x):
        print('Less than')


if(__name__== '__main__'):
    main()