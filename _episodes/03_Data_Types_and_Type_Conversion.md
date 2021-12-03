---
layout: episode
title: Data Types and Type Conversion
permalink: /03_Data_Types_and_Type_Conversion
exercises: 5
keypoints: ['Every value has a type.', 'Use the built-in function `type` to find the type of a value.', 'Types control what operations can be done on values.', 'Strings can be added and multiplied.', "Strings have a length (but numbers don't).", 'Must convert numbers to strings or vice versa when operating on them.', 'Can mix integers and floats freely in operations.', 'Variables only change value when something is assigned to them.']
objectives: ['Explain key differences between integers and floating point numbers.', 'Explain key differences between numbers and character strings.', 'Use built-in functions to convert between integers, floating point numbers, and strings.']
questions: ['What kinds of data do programs store?', 'How can I convert one type to another?']
teaching: 5
---

## Every value has a type
*   Every value in a program has a specific type.
*   Integer (`int`): represents positive or negative whole numbers like 3 or -512.
*   Floating point number (`float`): represents real numbers like 3.14159 or -2.5.

## Use the built-in function `type to find the type of a value
*   Works on variables and values



~~~
print(type(52))
~~~
{: .language-python}

    <class 'int'>


~~~
fitness = 'average'
print(type(fitness))
~~~
{: .language-python}

    <class 'str'>

## Types control what operations (or methods) can be performed on a given value.
* You can subtract numbers


~~~
print(5 - 3)
~~~
{: .language-python}

    2

* You cannot subtract strings


~~~
print('hello' - 'h')
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-35e8597b28d6> in <module>
    ----> 1 print('hello' - 'h')
    

    TypeError: unsupported operand type(s) for -: 'str' and 'str'


## You can use the “+” and “*” operators on strings.
“Adding” character strings concatenates them.



~~~
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)
~~~
{: .language-python}

    Ahmed Walsh

*  multiplication is repeated addition


~~~
separator = '=' * 10
print(separator)
~~~
{: .language-python}

    ==========

## Strings have a length (but numbers don't)
*  The built-in function `len` counts the number of characters in a string.
*  Numbers don’t have a length (not even zero).


~~~
print(len(full_name))
~~~
{: .language-python}

    11


~~~
print(len(52))
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-8e77a6522867> in <module>
    ----> 1 print(len(52))
    

    TypeError: object of type 'int' has no len()


## Must convert numbers to strings or vice versa when operating on them.
* Cannot add numbers and strings, because the result is ambiguous.



~~~
print(1 + '2')
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-013270d67d3d> in <module>
    ----> 1 print(1 + '2')
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



~~~
print(1 + int('2'))
print(str(1) + '2')
~~~
{: .language-python}

    3
    12

## Can mix integers and floats freely in operations.
Python 3 automatically converts integers to floats as needed.


~~~
print('half is', 1 / 2.0)
print('three squared is', 3.0 ** 2)
~~~
{: .language-python}

    half is 0.5
    three squared is 9.0

## Variables only change value when something is assigned to them.



~~~
first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)
~~~
{: .language-python}

    first is 2 and second is 5

## Exercise 1
What type of value is 3.4 ? How can you find out?


~~~
type(3.4)
~~~
{: .language-python}




~~~
float
~~~
{: .output}



## Exercise 2
What is the type of the value 3.25 + 4 ?


~~~
print(type(3.25 + 4))
~~~
{: .language-python}

    <class 'float'>

## Exercise 3

What type of value (integer, floating point number, or character string) would you use to represent each of the following? Try to come up with more than one good answer for each problem. For example, in # 1, when would counting days with a floating point variable make more sense than using an integer?

  1. Number of days since the start of the year.
  2. Time elapsed from the start of the year until now in days.
  3. Serial number of a piece of lab equipment.
  4. A lab specimen’s age
  5. Current population of a city.
  6. Average population of a city over time.

## Truncate division to the nearest integer with `//`


~~~
print("5 / 3  = ", 5/3 )
print("5 // 3 = ", 5//3 )
~~~
{: .language-python}

    5 / 3  =  1.6666666666666667
    5 // 3 =  1

## Strings to numbers


~~~
print("string to float:", float("3.4"))
print("float to int:", int(3.4))
~~~
{: .language-python}

    string to float: 3.4
    float to int: 3

## Exercise 3
What is the displayed with this command

    print("string to float:", float("Hello world!"))



~~~
print("string to float:", float("Hello world!"))

~~~
{: .language-python}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-17-8b7db3f305e2> in <module>
    ----> 1 print("string to float:", float("Hello world!"))
    

    ValueError: could not convert string to float: 'Hello world!'


## Exercise 4
What is the displayed with this command

    print("fractional string to int:", int("3.4"))


~~~
print("fractional string to int:", int("3.4"))
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-18-617dc59d7f19> in <module>
    ----> 1 print("fractional string to int:", int("3.4"))
    

    ValueError: invalid literal for int() with base 10: '3.4'


## Exercise 5
Which of the following will print 2?

    first = 1.0
    second = "1"
    third = "1.1"
  
  1. first + float(second)
  2. float(second) + float(third)
  3. first + int(third)
  4. first + int(float(third))
  5. int(first) + int(float(third))
  6. 2.0 * second

## Complex numbers can be used with a `j`


~~~
1.0 + 2.0j
~~~
{: .language-python}




~~~
(1+2j)
~~~
{: .output}




~~~
2.0j
~~~
{: .language-python}




~~~
2j
~~~
{: .output}




~~~
val = 2.0 + 3j
print("The real part is ",val.real)
print("The imaginary part is ",val.imag)
~~~
{: .language-python}

    The real part is  2.0
    The imaginary part is  3.0
