---
layout: episode
title: Built-in Functions and Help
permalink: /04_Built-in_Functions_and_Help
exercises: 10
keypoints: ['Use comments to add documentation to programs.', 'A function may take zero or more arguments.', 'Commonly-used built-in functions include `max`, `min`, and `round`.', 'Functions may only work for certain (combinations of) arguments.', 'Functions may have default values for some arguments.', 'Use the built-in function `help` to get help for a function.', 'The Jupyter Notebook has two ways to get help.', 'Every function returns something.', "Python reports a syntax error when it can't understand the source of a program.", 'Python reports a runtime error when something goes wrong while a program is executing.', "Fix syntax errors by reading the source code, and runtime errors by tracing the program's execution."]
objectives: ['Explain the purpose of functions.', 'Correctly call built-in Python functions.', 'Correctly nest calls to built-in functions.', 'Use help to display documentation for built-in functions.', 'Correctly describe situations in which SyntaxError and NameError occur.']
questions: ['How can I use built-in functions?', 'How can I find out what they do?', 'What kind of errors can occur in programs?']
teaching: 15
---

## Use comments to add documentation to programs.



~~~
# This sentence isn't executed by Python.
adjustment = 0.5   # Neither is this - anything after '#' is ignored.
~~~
{: .language-python}

## A function may take zero or more arguments.
* An argument is a value passed into a function.
* `len`, `int`, `float` each take one argument.
* `print` takes zero or more.



~~~
print('before') # 1
print() # 0 
print('after',"this") #2
~~~
{: .language-python}

    before
    
    after this

## Commonly-used built-in functions include `max`, `min`, and `round`.
*   Use `max` to find the largest value of one or more values. 
*   Use `min` to find the smallest.
*   Letters are compared using the order 0-9, a-z, A-Z.


~~~
print(max(1,2,3))
print(min('a','A','b'))
~~~
{: .language-python}

    3
    A

## Functions may only work for certain (combinations of) arguments.
*   max and min must be given at least one argument.
*   The arguments must be meaningfully comparable


~~~
print(max(1,'a'))
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-a9f2333f1e52> in <module>
    ----> 1 print(max(1,'a'))
    

    TypeError: '>' not supported between instances of 'str' and 'int'


* We've already seen that `int` doesn't take strings with decimal points



~~~
print(int("3.4"))
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-ba8d7dd18d3b> in <module>
    ----> 1 print(int("3.4"))
    

    ValueError: invalid literal for int() with base 10: '3.4'


## Functions may have default values for some arguments.
* round will round off a floating-point number, by default to zero decimal places


~~~
round(3.712)
~~~
{: .language-python}




~~~
4
~~~
{: .output}



*  We can specify the number of decimal places with the second argument.


~~~
round(3.712,1)
~~~
{: .language-python}




~~~
3.7
~~~
{: .output}



## Use the built-in function `help` to get help for a function.
Every built-in function has online documentation.



~~~
help(round)
~~~
{: .language-python}

    Help on built-in function round in module builtins:
    
    round(number, ndigits=None)
        Round a number to a given precision in decimal digits.
        
        The return value is an integer if ndigits is omitted or None.  Otherwise
        the return value has the same type as the number.  ndigits may be negative.


## Python reports a syntax error when it can’t understand the source of a program.
Won't even try to run the program if it can't be parsed.


~~~
name = 'Feng
~~~
{: .language-python}


      File "<ipython-input-9-55063da583f6>", line 1
        name = 'Feng
                    ^
    SyntaxError: EOL while scanning string literal




~~~
# An extra '=' in the assignment.
age = = 52
~~~
{: .language-python}


      File "<ipython-input-10-ccc3df3cf902>", line 2
        age = = 52
              ^
    SyntaxError: invalid syntax




~~~
print("hello world"
~~~
{: .language-python}


      File "<ipython-input-11-fe69f65f3ba9>", line 1
        print("hello world"
                           ^
    SyntaxError: unexpected EOF while parsing



mis-spelling appears as a `name error`. Python doesn't know it's mis-spelled, it thinks the variable hasn't been defined.


~~~
age = 53
remaining = 100 - aege # mis-spelled 'age'
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-1214fb6c55fc> in <module>
          1 age = 53
    ----> 2 remaining = 100 - aege # mis-spelled 'age'
    

    NameError: name 'aege' is not defined


## Every function returns something.
*   Every function call produces some result.
*   If the function doesn't have a useful result to return,
    it usually returns the special value `None`.


~~~
result = print('example')
print('result of print is', result)
~~~
{: .language-python}

    example
    result of print is None

## Exercise 1
Explain the order of the operations in the following code. When does the addition and subtraction happen? When are the functions called? What is the value of `radiance`

    radiance = 1.0
    radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))

## Exercise 2
If every function returns something, why don't `max` and `min` return `None` if they are given no arguments?

## Exercise 3
Python counts characters in a string from zero, and `len` returns the length of the string. Print the last character of this variable

     name = "James Bond"


~~~
name = "James Bond"
print( name[len(name) - 1])
~~~
{: .language-python}

    d
