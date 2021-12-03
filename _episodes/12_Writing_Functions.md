---
layout: episode
title: Writing Functions
permalink: /12_Writing_Functions
exercises: 15
keypoints: ['Break programs down into functions to make them easier to understand.', 'Define a function using `def` with a name, parameters, and a block of code.', 'Defining a function does not run it.', 'Arguments in call are matched to parameters in definition.', 'Functions may return a result to their caller using `return`.']
objectives: ['Explain and identify the difference between function definition and function call.', 'Write a function that takes a small, fixed number of arguments and produces a single result.']
questions: ['How can I create my own functions?']
teaching: 10
---

## Break programs down into functions to make them easier to understand.
*   Human beings can only keep a few items in working memory at a time.
*   Understand larger/more complicated ideas by understanding and combining pieces.
*   Enables *re-use*. Write one time, use many times.

## Define a function using `def` with a name, parameters, and a block of code.
*   Begin the definition of a new function with `def`.
*   Followed by the name of the function, (letters, numbers, underscore).
*   Then *parameters* in parentheses. Empty parentheses if the function doesn't take any inputs.
*   Then a colon.
*   Then an indented block of code.


~~~
def print_greeting():
    print('Hello!')
~~~
{: .language-python}

## Defining a function does not run it.
you must call it to use it.


~~~
print_greeting()
~~~
{: .language-python}

    Hello!

## Arguments in call are matched to parameters in definition.
*   Functions are most useful when they can operate on different data.
*   If you don't name the arguments when using them in the call, the arguments will be matched to
parameters in the order the parameters are defined in the function.


~~~
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19) #The function assumes the year is 1871, month is 3, and day is 19
~~~
{: .language-python}

    1871/3/19

## You can give the arguments in a different order if you name them


~~~
print_date(month=3, day=19, year=1871)
~~~
{: .language-python}

    1871/3/19


~~~
print_date(1871, 19, month=3) #Why doesn't this work?
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-7e0dd74c4fde> in <module>
    ----> 1 print_date(1871, 19, month=3) #Why doesn't this work?
    

    TypeError: print_date() got multiple values for argument 'month'



~~~
print_date(1871, month=3, 19) #Why doesn't this work?
~~~
{: .language-python}


      File "<ipython-input-6-a89b5fcb76e8>", line 1
        print_date(1871, month=3, 19) #Why doesn't this work?
                                  ^
    SyntaxError: positional argument follows keyword argument



## Functions may return a result to their caller using `return`.
*   Use `return ...` to give a value back to the caller.
*   May occur anywhere in the function.
*   But functions are easier to understand if `return` occurs:
    *   At the start to handle special cases.
    *   At the very end, with a final result.


~~~
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
~~~
{: .language-python}


~~~
a = average([1,3,4])
print("average of values: ", a)
~~~
{: .language-python}

    average of values:  2.6666666666666665


~~~
print('average of empty list:', average([]))
~~~
{: .language-python}

    average of empty list: None

## **Every** function returns something, some return 'None'


~~~
result = print_date(1871, 3, 19)
print('result of call is:', result)
~~~
{: .language-python}

    1871/3/19
    result of call is: None

## Functions need to be indented like for loops


~~~
def another_function(loop_limit):
    for counter in range(loop_limit):
        print(counter)
~~~
{: .language-python}


~~~
another_function(10)
~~~
{: .language-python}

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

## Exercise 1
What does the following program print?

    def report(pressure):
        print('pressure is', pressure)
    
    print('calling', report, 22.5)


~~~
def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5) #This doesn't call the function 'report'
~~~
{: .language-python}

    calling <function report at 0x7feee05daca0> 22.5

## Exercise 2
Create a function that takes a list, and returns the sum and the sum of the values squared



~~~
def sum_sum_squared(values):
    sum_values = 0
    sum_square_values = 0
    for value in values:
        sum_values = sum_values + value
        sum_square_values = sum_square_values + value**2
    result = [sum_values, sum_square_values]
    return result

sum_sum_squared([1,2,3,4])
~~~
{: .language-python}




~~~
[10, 30]
~~~
{: .output}




~~~
# Can't we just use numpy?
import numpy
def sum_sum_squared_numpy(values):
    v = numpy.array(values)
    return v.sum(), (v**2).sum()

sum_sum_squared_numpy([1,2,3,4])
~~~
{: .language-python}




~~~
(10, 30)
~~~
{: .output}



## Exercise 3

Fill in the blanks to create a function that takes a list of numbers as an argument and returns the first negative value in the list. What does your function do if the list is empty?

    def first_negative(values):
        for v in ____:
            if ____:
                return ____


~~~
def first_negative(values):
    for v in values:
        if v < 0:
            return v
first_negative([1,2,-2,2])
~~~
{: .language-python}




~~~
-2
~~~
{: .output}




~~~
first_negative([])
~~~
{: .language-python}
