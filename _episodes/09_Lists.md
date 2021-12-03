---
layout: episode
title: Lists
permalink: /09_Lists
exercises: 10
keypoints: ['A list stores many values in a single structure.', "Use an item's index to fetch it from a list.", "Lists' values can be replaced by assigning to them.", 'Appending items to a list lengthens it.', 'Use `del` to remove items from a list entirely.', 'The empty list contains no values.', 'Lists may contain values of different types.', 'Character strings can be indexed like lists.', 'Character strings are immutable.', 'Indexing beyond the end of the collection is an error.']
objectives: ['Explain why programs need collections of values.', 'Write programs that create flat lists, index them, slice them, and modify them through assignment and method calls.']
questions: ['How can I store multiple values?']
teaching: 10
---

## A list stores many values in a single structure.
*   Use a *list* to store many values together.
    *   Contained within square brackets `[...]`.
    *   Values separated by commas `,`.
*   Use `len` to find out how many values are in a list.



~~~
pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))
~~~
{: .language-python}

    pressures: [0.273, 0.275, 0.277, 0.275, 0.276]
    length: 5

## Use an item’s index to fetch it from a list.
Just like strings


~~~
print('zeroth item of pressures:', pressures[0])
print('fourth item of pressures:', pressures[4])
~~~
{: .language-python}

    zeroth item of pressures: 0.273
    fourth item of pressures: 0.276

## Lists’ values can be replaced by assigning to them.



~~~
pressures[0] = 0.265
print('pressures is now:', pressures)
~~~
{: .language-python}

    pressures is now: [0.265, 0.275, 0.277, 0.275, 0.276]

## Appending items to a list lengthens it.
*   `append` is a *method* of lists.
    *   Like a function, but tied to a particular object.
*   Use `object_name.method_name` to call methods.
    *   Deliberately resembles the way we refer to things in a library.
*   We will meet other methods of lists as we go along.
    *   Use `help(list)` for a preview.


~~~
primes = [2, 3, 5]
print('primes is initially:', primes)
~~~
{: .language-python}

    primes is initially: [2, 3, 5]


~~~
primes.append(7)
primes.append(9)
print('primes has become:', primes)
~~~
{: .language-python}

    primes has become: [2, 3, 5, 7, 9]

## Extending a list with another list combines them
*   `extend` is similar to `append`, but it allows you to combine two lists.  For example:



~~~
teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
~~~
{: .language-python}

    primes is currently: [2, 3, 5, 7, 9]


~~~
primes.extend(teen_primes)
print('primes has now become:', primes)
~~~
{: .language-python}

    primes has now become: [2, 3, 5, 7, 9, 11, 13, 17, 19]


~~~
primes.append(middle_aged_primes)
print('primes has finally become:', primes)
~~~
{: .language-python}

    primes has finally become: [2, 3, 5, 7, 9, 11, 13, 17, 19, [37, 41, 43, 47]]

## Use `del` to remove items from a list entirely.


~~~
primes = [2,3,5,7,9]
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)
~~~
{: .language-python}

    primes before removing last item: [2, 3, 5, 7, 9]
    primes after removing last item: [2, 3, 5, 7]

## The empty list contains no values.
*   Use `[]` on its own to represent a list that doesn't contain any values.



~~~
empty = []
print(empty, len(empty))
~~~
{: .language-python}

    [] 0

## Lists may contain values of different types.
* A single list may contain numbers, strings, and anything else.



~~~
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3., 'Modify lists.']
~~~
{: .language-python}

## Character strings can be indexed like lists.



~~~
element = 'carbon'
print('zeroth character:', element[0])
print('third character:', element[3])
~~~
{: .language-python}

    zeroth character: c
    third character: b

## BUT Character strings are immutable.
*   Cannot change the characters in a string after it has been created.
    *   *Immutable*: can't be changed after creation.
    *   In contrast, lists are *mutable*: they can be modified in place.
*   Python considers the string to be a single value with parts,
    not a collection of values.


~~~
primes = [2,3,5,7,8]
element = 'karbon'
print(primes, element)
~~~
{: .language-python}

    [2, 3, 5, 7, 8] karbon


~~~
primes[4]=9
print(primes)
~~~
{: .language-python}

    [2, 3, 5, 7, 9]


~~~
element[0] = 'c'
print(element)
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-14b31d429927> in <module>
    ----> 1 element[0] = 'c'
          2 print(element)


    TypeError: 'str' object does not support item assignment


## Indexing beyond the end of the collection is an error.
*   Python reports an `IndexError` if we attempt to access a value that doesn't exist.


~~~
print('99th element of element is', element[99])
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-16-c3bdf414b991> in <module>
    ----> 1 print('99th element of element is', element[99])
    

    IndexError: string index out of range



~~~
print('99th element of primes is', primes[99])
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-17-ca0ee2c15e84> in <module>
    ----> 1 print('99th element of primes is', primes[99])
    

    IndexError: list index out of range


## From Strings to Lists and Back


~~~
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
~~~
{: .language-python}

    string to list: ['t', 'i', 'n']
    list to string: gold

## Exercise 1
If `low` and `high` are both non-negative integers, how long is the following list ?

    values[low:high]


~~~
primes = [2,3,5,7,9,11,13,17,19]
low = 3
high = 7
print("length is ",len(primes[low:high]), "and high - low is ",high - low)
~~~
{: .language-python}

    length is  4 and high - low is  4

# Exercise 2
What does the following program print?

    element = 'helium'
    print(element[-1])


~~~
element = 'helium'
print(element[-1])
~~~
{: .language-python}

    m

  1. How does Python interpret a negative index?
  2. If a list or string has N elements, what is the most negative index that can safely be used with it, and what location does that index represent?
  3. If values is a list, what does del values[-1] do?
  4. How can you display all elements but the last one? (Hint: you will need to combine slicing and negative indexing.)

# Exercise 3
If there are 5 entries in the list, what does primes[-7] print?

    primes = [2,3,5,7,9]


~~~
primes = [2,4,5,7,9]
print(primes[-7])
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-21-dc3b1faef53d> in <module>
          1 primes = [2,4,5,7,9]
    ----> 2 print(primes[-7])
    

    IndexError: list index out of range


## Slices can be used to *step* through a list


~~~
primes = [2,3,5,7,9,11,13,17,19]
print("all primes: ",primes)
print("every other prime: ",primes[::2])
print("primes backwards: ",primes[::-1])
~~~
{: .language-python}

    all primes:  [2, 3, 5, 7, 9, 11, 13, 17, 19]
    every other prime:  [2, 5, 9, 13, 19]
    primes backwards:  [19, 17, 13, 11, 9, 7, 5, 3, 2]

## Exercise 4
What does the following program print?

    element = 'lithium'
    print(element[0:20])
    print(element[-1:3])


~~~
element = 'lithium'
print("element[0:20] =",element[0:20])
print("element[-1:3] =",element[-1:3])
~~~
{: .language-python}

    element[0:20] = lithium
    element[-1:3] = 

## Exercise 5: Sort and Sorted
What do these two programs print? In simple terms, explain the difference between `sorted(letters)` and `letters.sort()`.

    # Program A
    letters = list('gold')
    result = sorted(letters)
    print('letters is', letters, 'and result is', result)

    # Program B
    letters = list('gold')
    result = letters.sort()
    print('letters is', letters, 'and result is', result)




~~~
# Program A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
# Program B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)

~~~
{: .language-python}

    letters is ['g', 'o', 'l', 'd'] and result is ['d', 'g', 'l', 'o']
    letters is ['d', 'g', 'l', 'o'] and result is None

## Exercise 6: Copying (or Not)
What do these two programs print? In simple terms, explain the difference between `new = old` and `new = old[:]`.

    # Program A
    old = list('gold')
    new = old      # simple assignment
    new[0] = 'D'
    print('new is', new, 'and old is', old)
    
    # Program B
    old = list('gold')
    new = old[:]   # assigning a slice
    new[0] = 'D'
    print('new is', new, 'and old is', old)


~~~
# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)

# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)
~~~
{: .language-python}

    new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
    new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
