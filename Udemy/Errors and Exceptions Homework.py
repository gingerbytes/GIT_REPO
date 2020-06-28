'''
Problem 1

Handle the exception thrown by the code below by using try and except blocks.
'''


def powerstring():
    for i in ['a', 'b', 'c']:
        try:
            print(i**2)
        except:
            print('You are processing a string')


# powerstring()

'''
Problem 2

Handle the exception thrown by the code below by using try and except blocks.
Then use a finally block to print 'All Done.'
'''


def divisionerror():
    x = 5
    y = 0

    try:
        z = x/y
    except:
        print('Division error')
    finally:
        print('All Done')


# divisionerror()

'''
Problem 3

Write a function that asks for an integer and prints the square of it.
Use a while loop with a try, except, else block to account for incorrect inputs.

'''


def ask():
    userinput = ''
    while True:
        # Try must have an operation with a result to be validated if Error or not.
        try:
            userinput = int(input("Give a number: "))
        except ValueError:
            print("That is not a number, try again.")
            continue
        else:
            print(userinput ** 2)
            break


ask()
