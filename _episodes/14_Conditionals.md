---
layout: episode
title: Conditionals
permalink: /14_Conditionals
exercises: 15
keypoints: ['Use `if` statements to control whether or not a block of code is executed.', 'Conditionals are often used inside loops.', 'Use `else` to execute a block of code when an `if` condition is *not* true.', 'Use `elif` to specify additional tests.', 'Conditions are tested once, in order.', "Create a table showing variables' values to trace a program's execution."]
objectives: ['Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators).', 'Trace the execution of unnested conditionals and conditionals inside loops.']
questions: ['How can programs do different things for different data?']
teaching: 10
---

## Use `if ` statements to control whether or not a block of code is executed.
*   An `if` statement (more properly called a *conditional* statement)
    controls whether some block of code is executed or not.
*   Structure is similar to a `for` statement:
    *   First line opens with `if` and ends with a colon
    *   Body containing one or more statements is indented (usually by 4 spaces)


~~~
mass = 3.54
if mass > 3.0:
    print(mass, 'is large')

mass = 2.07
if mass > 3.0:
    print (mass, 'is large')
~~~
{: .language-python}

## Conditionals are often used inside loops.


~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
~~~
{: .language-python}

## Conditionals are often used inside functions



~~~
def larger_of(a,b):
    if a > b :
        return a
    else:
        return b
        
~~~
{: .language-python}

## Use `else` to execute a block of code when an if condition is not true.
*   `else` can be used following an `if`.
*   Allows us to specify an alternative to execute when the `if` *branch* isn't taken.


~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
~~~
{: .language-python}

## Use elif to specify additional tests.
*   May want to provide several alternative choices, each with its own test.
*   Use `elif` (short for "else if") and a condition to specify these.
*   Always associated with an `if`.
*   Must come before the `else` (which is the "catch all").


~~~
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is HUGE')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
~~~
{: .language-python}

## Conditions are tested once, in order.
*   Python steps through the branches of the conditional in order, testing each in turn.
*   So ordering matters.


~~~
grade = 85 # is an A? right?
if grade >= 60:
    print('grade is C')
elif grade >= 70:
    print('grade is B')
elif grade >= 80:
    print('grade is A')
~~~
{: .language-python}

## Compound Relations Using `and`, `or`, and Parentheses


~~~
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    print("mass=",mass[i], ", velocity=", velocity[i])
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")
    print()
~~~
{: .language-python}

## Exercise 1
Are these the same tests?

   1. if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20:
   2. if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
   3. if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):


## Exercise 2
Fill in the blanks so that this program creates a new list containing zeroes where the original list’s values were negative and ones where the origina list’s values were positive.

    original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
    result = ____
    for value in original:
        if ____:
            result.append(0)
        else:
            ____
    print(result) # [0,1,1,1,0,1]


~~~
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value < 0:
        result.append(0)
    else:
        result.append(1)
print(result) # [0,1,1,1,0,1]
~~~
{: .language-python}


~~~
#numpy is fun
import numpy
print((numpy.array(original) >= 0)*1)
~~~
{: .language-python}

## Exercise 3 : initializing values
Modify this program so that it finds the largest and smallest values in the list no matter what the range of values originally is.


    values = [4, 25, 68, 87, 50, 25, 80, 69, 35, 91, 8, 33, 7, 5, 50, 20, 8, 93, 55, 23, 27, 21, 93, 59, 50, 20, 55, 34, 45, 1, 81, 19, 71, 95, 34, 27, 69, 39, 59, 61, 76, 39, 3, 65, 19, 27, 69, 87, 7, 71]
    smallest, largest = None, None
    for v in values:
        if ____:
            smallest, largest = v, v
        ____:
            smallest = min(____, v)
            largest = max(____, v)
    print(smallest, largest)


~~~
values = [4, 25, 68, 87, 50, 25, 80, 69, 35, 91, 8, 33, 7, 5, 50, 20, 8, 93, 55, 23, 27, 21, 93, 59, 50, 20, 55, 34, 45, 1, 81, 19, 71, 95, 34, 27, 69, 39, 59, 61, 76, 39, 3, 65, 19, 27, 69, 87, 7, 71]
smallest, largest = None, None
for v in values:
    if smallest is None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)
~~~
{: .language-python}
