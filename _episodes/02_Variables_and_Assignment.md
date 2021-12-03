---
layout: episode
title: Variables and Assignment
permalink: /02_Variables_and_Assignment
exercises: 10
keypoints: ['Use variables to store values.', 'Use `print` to display values.', 'Variables persist between cells.', 'Variables must be created before they are used.', 'Variables can be used in calculations.', 'Use an index to get a single character from a string.', 'Use a slice to get a substring.', 'Use the built-in function `len` to find the length of a string.', 'Python is case-sensitive.', 'Use meaningful variable names.']
objectives: ['Write programs that assign scalar values to variables and perform calculations with those values.', 'Correctly trace value changes in programs that use scalar assignment.']
questions: ['How can I store data in programs?']
teaching: 10
---

## Use variables to store values

*   Variables are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Variable names can only contain letters, digits, and underscore. They cannot start with a digit.


~~~
age = 42
first_name = 'Ahmed'
~~~
{: .language-python}

## Use `print` to display values
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (i.e., the things to print) in parentheses.


~~~
print(first_name,"is",age,"years old")
~~~
{: .language-python}

    Ahmed is 42 years old

## Variables must be created before they can be used
If a variable doesn’t exist yet, or if the name has been mis-spelled, Python reports an error.



~~~
print(last_name)
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-a637c5453549> in <module>
    ----> 1 print(last_name)
    

    NameError: name 'last_name' is not defined


The last line of an error message is usually the most informative.

## Variables persist between use


~~~
myval = 1
myval2 = 2
print(myval)
~~~
{: .language-python}

    1


~~~
print(myval2) #the variable persisted in memory
~~~
{: .language-python}

    2

## Variables can be used in calculations
We can use variables in calculations just as if they were values.


~~~
age = age + 3
print(first_name, "will graduate at", age,".")
~~~
{: .language-python}

    Ahmed will graduate at 45 .

## Use an index to get a single character from a string.
* We can treat the string as a list of characters.
* Each position in the string is given a number starting from 0.
* Use the position’s index in square brackets to get the character at that position.


~~~
atom_name = 'helium'
print(atom_name[0])
~~~
{: .language-python}

    h

## Use a slice to get a substring
*   A part of a string is called a substring. A substring can be as short as a
    single character. Also called a slice in Python.
*   We take a slice by using `[start:stop]`, where `start` is replaced with the
    index of the first element we want and `stop` is replaced with the index of
    the element just after the last element we want.
*   The difference between stop and start is the slice's length.


~~~
atom_name = 'sodium'
print(atom_name[0:3])
~~~
{: .language-python}

    sod

## Use the built-in function `len` to find the length of a string.


~~~
print(len('helium'))
~~~
{: .language-python}

    6

## Python is case-sensitive.
*   Python thinks that upper- and lower-case letters are different, so `Name` and `name` are different variables.


~~~
myval = 2
print(myVal)
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-143d5c8c8732> in <module>
          1 myval = 2
    ----> 2 print(myVal)
    

    NameError: name 'myVal' is not defined


## Use meaningful variable names.
*   Python doesn't care what you call variables as long as they obey the rules
*   Use meaningful variable names to help other people understand what the program does.


~~~
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
~~~
{: .language-python}

    Ahmed is 42 years old

## Exercise 1
What is the final value of `position` below?

    initial = 'left'
    position = initial
    initial = 'right'



~~~
initial = 'left'
position = initial
initial = 'right'
print(initial)
~~~
{: .language-python}

    right

## Exercise 2
Which is a better variable name, `m`, `min`, or `minutes`?
e.g. which of these lines are most clear

    ts = m * 60 + s
    tot_sec = min * 60 + sec
    total_seconds = minutes * 60 + seconds

## Exercise 3
What does the following program print?

    atom_name = 'carbon'
    print('atom_name[1:3] is:', atom_name[1:3])


~~~
atom_name = 'carbon'
print('atom_name[1:3] is:', atom_name[1:3])
~~~
{: .language-python}

    atom_name[1:3] is: ar

# Exercise 4
Assuming the following definitions

    thing = "The Cat in the Hat"
    low = 4
    high = 8
    negative = -10
    
  1. What does thing[low:high] do?
  2. What does thing[low:] (without a value after the colon) do?
  3. What does thing[:high] (without a value before the colon) do?
  4. What does thing[:] (just a colon) do?
  5. What does thing[low:negative] do?
  6. What happens when you choose a high value which is out of range? (i.e., try thing[0:25])


~~~
thing = "The Cat in the Hat"
low = 4
high = 8
negative = -10

print("thing[low:high] = "    ,thing[low:high])
print("thing[low:] = "        ,thing[low:])
print("thing[:high] = "       ,thing[:high])
print("thing[:] = "           ,thing[:])
print("thing[low:negative] = ",thing[low:negative])
print("thing[0:25] = "        ,thing[0:25])
~~~
{: .language-python}

    thing[low:high] =  Cat 
    thing[low:] =  Cat in the Hat
    thing[:high] =  The Cat 
    thing[:] =  The Cat in the Hat
    thing[low:negative] =  Cat 
    thing[0:25] =  The Cat in the Hat
