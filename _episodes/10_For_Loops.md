---
layout: episode
title: For Loops
permalink: /10_For_Loops
exercises: 15
keypoints: ['A *for loop* executes commands once for each value in a collection.', 'The first line of the `for` loop must end with a colon, and the body must be indented.', 'Indentation is always meaningful in Python.', 'A `for` loop is made up of a collection, a loop variable, and a body.', 'Loop variables can be called anything (but it is strongly advised to have a meaningful name to the looping variable).', 'The body of a loop can contain many statements.', 'Use `range` to iterate over a sequence of numbers.', 'The Accumulator pattern turns many values into one.']
objectives: ['Explain what for loops are normally used for.', 'Trace the execution of a simple (unnested) loop and correctly state the values of variables in each iteration.', 'Write for loops that use the Accumulator pattern to aggregate values.']
questions: ['How can I make a program do many things?']
teaching: 10
---

## A for loop executes commands once for each value in a collection.
*   A *for loop* tells Python to execute some statements once for each value in a list,
    a character string,
    or some other collection.
*   "for each thing in this group, do these operations"


~~~
for number in [2, 3, 5]:
    print(number)
~~~
{: .language-python}

    2
    3
    5


~~~
# this is equivalent to
print(2)
print(3)
print(5)
~~~
{: .language-python}

    2
    3
    5

## The first line of the for loop must end with a colon, and the body must be indented.
*   The colon at the end of the first line signals the start of a *block* of statements.
*   Python uses indentation rather than `{}` or `begin`/`end` to show *nesting*.
    *   Any consistent indentation is legal, but almost everyone uses four spaces.


~~~
for number in [2, 3, 5]:
print(number)
~~~
{: .language-python}


      File "<ipython-input-3-3a0b55365d6d>", line 2
        print(number)
        ^
    IndentationError: expected an indented block



## Indentation is always meaningful in Python.


~~~
firstName="Jon"
  lastName="Smith"
~~~
{: .language-python}


      File "<ipython-input-4-fac7a181dff6>", line 2
        lastName="Smith"
        ^
    IndentationError: unexpected indent



## A for loop is made up of a collection, a loop variable, and a body.
*   The collection, `[2, 3, 5]`, is what the loop is being run on.
*   The body, `print(number)`, specifies what to do for each value in the collection.
*   The loop variable, `number`, is what changes for each *iteration* of the loop.


~~~
for number in [2, 3, 5]:
    print(number)
~~~
{: .language-python}

    2
    3
    5

## The body of a loop can contain many statements.
Long `for` loops can be hard to understand.


~~~
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)
~~~
{: .language-python}

    2 4 8
    3 9 27
    5 25 125

## Use `range` to iterate over a sequence of numbers.
*   The built-in function `range` produces a sequence of numbers.
    *   *Not* a list: the numbers are produced on demand
        to make looping over large ranges more efficient.
*   `range(N)` is the numbers 0..N-1
    *   Exactly the legal indices of a list or character string of length N


~~~
print('a range is not a list:', range(0, 3))
for number in range(0,3):
    print(number)
~~~
{: .language-python}

    a range is not a list: range(0, 3)
    0
    1
    2

## Use an accumulator to turn many values into one.
*   A common pattern in programs is to:
    1.  Initialize an *accumulator* variable to zero, the empty string, or the empty list.
    2.  Update the variable with values from a collection.


~~~
# Sum the first 10 integers.
total = 0
for number in range(10):
   total = total + (number + 1)
print(total)
~~~
{: .language-python}

    55

## Exercise 1: Reversing a String
Fill in the blanks in the program below so that it prints “nit” (the reverse of the original character string “tin”).

    original = "tin"
    result = ____
    for char in original:
        result = ____
    print(result)


~~~
original = "tin"
result = ""
for char in original:
    result = char + result
print(result)
~~~
{: .language-python}

    nit

## Exercise 2: Practice Accumulating
Fill in the blanks in the program below to print the total length of strings in the list

    # Total length of the strings in the list:
    total = 0
    for word in ["red", "green", "blue"]:
        ____ = ____ + len(word)
    print(total)


~~~
# Total length of the strings in the list:
total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)
~~~
{: .language-python}

    12

## Exercise 3
Fill in the blanks in the program below to print the a list of length of each string in the list

    lengths = ____
    for word in ["red", "green", "blue"]:
        lengths._____(____)

    print(lengths)


~~~
lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)
~~~
{: .language-python}

    [3, 5, 4]

## Exercise 4
Fill in the blanks in the program below to print a concatenated string of all words in the list.

    words = ["red", "green", "blue"]
    result = ____
    for ____ in ____:
        ____
    print(result)


~~~
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)
~~~
{: .language-python}

    redgreenblue

## Exercise 5
Create an acronym by taking the first letter of each word and converting to uppercase : ["red", "green", "blue"] => "RGB". **write the whole thing**


~~~
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word[0].upper()
print(result)
~~~
{: .language-python}

    RGB
