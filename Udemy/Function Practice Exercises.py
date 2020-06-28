def myfunc(word):
    newword = ''
    for index in range(len(word)):
        if (index % 2 == 0):
            newword += word[index].lower()
        else:
            newword += word[index].upper()

    return newword

# print(myfunc('Anthropomorphism'))


'''
LESSER OF TWO EVENS: Write a function that returns the lesser of two
given numbers if both numbers are even, but returns the greater
if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a, b))
    else:
        print(max(a, b))


#lesser_of_two_evens(2, 4)
#lesser_of_two_evens(2, 5)


'''
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words
begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''


def animal_crackers(text):
    # you can combine string methods but take note of the order.
    mylist = text.lower().split()
    print(mylist[0][0] == mylist[1][0])


# animal_crackers('Levelheaded Llama')
# animal_crackers('Crazy Kangaroo')

'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
if one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
'''


def makes_twenty(n1, n2):
    print(20 in [n1, n2] or sum([n1, n2]) == 20)


# makes_twenty(20, 10)
# makes_twenty(12, 8)
# makes_twenty(2, 3)

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald
'''


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


# print(old_macdonald('macdonald'))

'''
MASTER YODA: Given a sentence, return a sentence with the words reversed

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''


def master_yoda(sentence):
    # split and reverse method cannot be combined in 1 line.
    wordlist = sentence.split()
    wordlist.reverse()
    print(" ".join(wordlist))


# master_yoda('I am home')

'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
'''


def almost_there(num):
    print(abs(num - 100) <= 10 or abs(num - 200) <= 10)


# almost_there(90)
# almost_there(104)
# almost_there(150)
# almost_there(209)

'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''


def has_33(nums):
    for i in range(len(nums) - 1):
        # use i+2 because it is range - 1.
        # Python can compare multiple items at the same time.
        if nums[i:i+2] == [3, 3]:
            print('True')
            return

    print('False')


#has_33([1, 3, 3])
#has_33([1, 3, 1, 3])
#has_33([3, 1, 3])

'''
PAPER DOLL: Given a string, return a string where for every character
in the original there are three characters

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''


def paper_doll(text):
    newstring = ''
    for letter in text:
        # Python allows multiplication of string and integer.
        newstring += letter*3

    print(newstring)


# paper_doll('Hello')
# paper_doll('Mississippi')

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''


def blackjack(a, b, c):
    total = a + b + c
    if total <= 21:
        print(total)
    elif total > 21 and (11 in [a, b, c]):
        print(total - 10)
    else:
        print('BUST')


# blackjack(5, 6, 7)
# blackjack(9, 9, 9)
# blackjack(9, 9, 11)

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections
of numbers starting with a 6 and extending to the next 9 (every 6 will be followed
by at least one 9). Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''


def summer_69(arr):
    if 6 in arr:
        # This deletes the section in the list between 6 and 9 (inclusive).
        del(arr[arr.index(6): arr.index(9) + 1])
    print(sum(arr))


# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])

'''
SPY GAME: Write a function that takes in a list of integers and returns True
if it contains 007 in order

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''


def spy_game2(nums):
    # this works but it's tedious.
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    for k in range(j, len(nums)):
                        if nums[k] == 7:
                            print('True')
                            return
    print('False')


def spy_game(nums):
    spy = [0, 0, 7]
    # point of comparison, in the right sequence

    for num in nums:
        if len(spy) != 0 and num == spy[0]:
            # use 0 in pop to always remove the first item.
            spy.pop(0)

    print(len(spy) == 0)


#spy_game([1, 2, 4, 0, 0, 7, 5])
#spy_game([1, 0, 2, 4, 0, 5, 7])
#spy_game([1, 7, 2, 0, 4, 5, 0])


'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist
up to and including a given number

count_primes(100) --> 25
'''


def count_primes(num):
    # 0 and 1  are not considered as prime numbers
    count = 0
    for x in range(2, num):
        for i in range(2, x):
            if x % i == 0:
                break
        # Python allows the use of 'else' condition with 'for' loop.
        # 'else' will be executed when there is no 'break' encountered in the loop.
        else:
            count += 1

    print(count)


# count_primes(100)


'''
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation
of that letter
'''


def print_big(letter):
    # a good example to use dictionary over a list.
    BigLetter = {'a': ['  *  ', ' * * ', '*   *', '*****', '*   *'],
                 'b': ['**** ', '*   *', '**** ', '*   *', '**** '],
                 'c': [' *** ', '*   *', '*    ', '*   *', ' *** ']}

    # asterisk will iterate thru the list.
    print(*BigLetter.get(letter), sep='\n')


# print_big('a')
# print_big('b')
# print_big('c')
