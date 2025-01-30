#####################################################################
# Jan Berglund - 01_discussion.py
#
# Veckouppgift 4
# Vecka 5, 27/1
# 1 Läsa och förstå kod - diskutera i grupp
#####################################################################


"""
1 Läsa och förstå kod - diskutera i grupp

Skriv ner vad du tror kommer skrivas ut.
Skriv sedan in koden i din IDE, exakt som den står, och kör den.
Fick du samma resultat som du trodde? Om inte, varför?
"""


# Start next
def gogo():
    input('\nPress Enter to continue')


# End it all
def endend():
    input('\n\nPress Enter to finish!')


# *******************************************************************

gogo()

# 1a

print('\nThis is "1a"\n')

# foo will be called with "hej" as input "t"
# The foo function will only print what is stated
# "hej" will be printed
# Calling foo function will only ever print "hej",
# no matter which input.
# I.e. no need for an input to foo

def foo(t):
    print('test')

foo('hej')


# *******************************************************************

gogo()

# 1b

print('\nThis is "1b"\n')

# fun1 is defined, but never called (used)
# The print statement will print "3 5"

def fun1(x, y):
    return x * y

print(3, 5)


# *******************************************************************

gogo()

# 1c

print('\nThis is "1c"\n')

# Will print the return value based on the input
# Answer will be "15"

def fun2(x, y):
    return x * y

print(fun2(3, 5))


# *******************************************************************

gogo()

# 1d

print('\nThis is "1d"\n')

# "First" x (2) will be passed into the function, returning 10
# "Second" y (3) will be passed, returning 15
# "Third" 10 + 15 (25) will be passed, returning 125
# a will become 125, which is then printed

def fun3 (i):
    return 5 * i

x = 2
y = 3
a = fun3(fun3(x) + fun3(y))
print(a)


# *******************************************************************

gogo()

# 1e

print('\nThis is "1e"\n')

# The function is never used
# a is 5, then 7, then printed

a = 5
def fun4(a):
    a += 1

a += 2
print(a)


# *******************************************************************

gogo()

# 1f

print('\nThis is "1f"\n')

# goo2 will return foo2(3)
# 3 as input to foo2 == 18
# a will be 18

def foo2(i):
    return  2*i*i

def goo2(x, y):
    return x(y)

a = goo2(foo2, 3)
print(a)


# *******************************************************************

gogo()

# 1g

print('\nThis is "1g"\n')

# First 5.5 is checked to be a float, returning and printing
# 'True'
# Second 42 is checked to be an int, returning and printing
# 'True'
# 'False' will never be returned in this case
# Improvement could be to add an else, including the last
# return, as well as adding text as to what was true

def is_number(x):
    if isinstance(x, int):
        print('Integer found!')
        return True
    elif isinstance(x, float):
        print('Float found!')
        return True
    else:
        print('Not int or float!')
        return False

print(is_number(5.5))
print(is_number(42))
print(is_number('a'))


# *******************************************************************

gogo()

# 1h

print('\nThis is "1h"\n')

# Will return a list, containing only the elements which have more
# than 4, but less than 8 characters
# how's, going, coding

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

test_out = average_words(['sup', 'how\'s', 'it', 'going', 'reflecting',
                          'on', 'programs', 'and', 'coding'])

print(test_out)


# *******************************************************************

gogo()

# 1i

print('\nThis is "1i"\n')

# 1. Find the smallest number
# 2. -11, 0, 0 as is now, correct -11, not applicable, 100


def find_min(numbers):
    if len(numbers) > 0:
        counter = numbers[0]
        for item in numbers:
            if item < counter:
                counter = item
        print(f"The smallest item is: {counter}")
        return counter
    else:
        print('This won\'t work')

find_min([10, 3, -4, -11])
find_min([])
find_min([100])


# *******************************************************************


endend()
