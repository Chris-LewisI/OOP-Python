# FOR LOOPS
# Rather than defining the iteration of a for loop like in Java or C,
# Python iterates through every item in a sequence in the order they
# are initialized.
words = ['cat', 'window', 'demonstrate']
for w in words:
    print(w, len(w))

# RANGE
# If iterating over numbers is necessary the range function comes in handy.
# Works just like indices in an array.
for i in range(5):
    print(i)

# Or can work from a specified range of numbers where the first argument is
# included but the second argument is excluded.
for i in range(5, 10):
    print(i)

# You can also combine the range and length functions.
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# BREAK
# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# Finding prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# CONTINUE
# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# WHILE
# The concept behind a while loop is for code to be repeated continuously while a certain
# condition is met (True). Once the condition is no longer True, the loop stops.
loop_count1=0
while loop_count1<5:
    print(loop_count1)
    loop_count1+=1