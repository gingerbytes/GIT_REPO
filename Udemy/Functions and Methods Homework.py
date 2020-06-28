'''
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as (4/3)(3.1416)(r**3)

vol(2)
33.49333333333333
'''
import string


def vol(rad):
    print(4/3*3.14*rad**3)


# vol(2)

'''
Write a function that checks whether a number is in a given range
(inclusive of highand low)
'''


def ran_check(num, low, high):
    print(num in range(low, high + 1))


# ran_check(7, 2, 7)

'''
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
'''


def up_low(s):
    # use dictionary counter instead of separate variable integer counter.
    dictr = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            dictr['upper'] += 1
        elif char.islower():
            dictr['lower'] += 1

    print(s + '\n')
    print(f'No. of Upper case characters :  {dictr["upper"]}')
    print(f'No. of Lower case Characters :  {dictr["lower"]}')


#up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''


def unique_list(lst):
    print([item for item in set(lst)])


# unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])

'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''


def multiply(numbers):
    print(math.prod(numbers))


# multiply([1, 2, 3, -4])

'''
Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.
'''


def palindrome(s):
    # remove spaces in the string.
    print(s.replace(" ", "") == s[::-1].replace(" ", ""))


# palindrome('racecar')
#palindrome('nurses run')

'''
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: Look at the string module
'''


def ispangram(str1, alphabet=string.ascii_lowercase):
    # get unique characters only from the string via set().
    # set all letters to lower case.
    # append to list if it's character.
    # sort list then convert back to string again.

    alphalist = [char for char in set(str1.lower()) if char.isalpha()]
    alphalist.sort()
    str1 = ''.join(alphalist)

    print(alphabet == str1)


#ispangram("The quick brown fox jumps over the lazy dog.")
#ispangram("Jackdaws love my big sphinx of quartz.")
#ispangram("Sympathizing would fix Quaker objectives!")
