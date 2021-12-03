---
layout: episode
title: Variable Scope
permalink: /13_Variable_Scope
exercises: 10
keypoints: ["The scope of a variable is the part of a program that can 'see' that variable."]
objectives: ['Identify local and global variables.', 'Identify parameters as local variables.', 'Read a traceback and determine the file, function, and line number on which the error occurred, the type of error, and the error message.']
questions: ['How do function calls actually work?', 'How can I determine where errors occurred?']
teaching: 10
---

## The scope of a variable is the part of a program that can ‘see’ that variable.
* There are only so many sensible names for variables.
* The part of a program in which a variable is visible is called its `scope`.


~~~
pressure = 103.9

def adjust(t):
    #This function can see the GLOBAL variable pressure
    temperature = t * 1.43 / pressure 
    return temperature
~~~
{: .language-python}


*   `pressure` is a *global variable*.
    *   Defined outside any particular function.
    *   Visible everywhere.
*   `t` and `temperature` are *local variables* in `adjust`.
    *   Defined in the function.
    *   Not visible in the main program.
    *   Remember: a function parameter is a variable
        that is automatically assigned a value when the function is called.


~~~
print('adjusted:', adjust(0.9))
print('temperature after call:', temperature) # I can't see the temperature variable inside the function.
~~~
{: .language-python}

    adjusted: 0.01238691049085659


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-ac8a50df68b6> in <module>
          1 print('adjusted:', adjust(0.9))
    ----> 2 print('temperature after call:', temperature) # I can't see the temperature variable inside the function.
    

    NameError: name 'temperature' is not defined


## Local and Global Variable Use


~~~
#A local variable with the same name gets priority
limit = 100

def clip(value,limit):
    return min(value, limit)

value = 22.5
print(clip(value,10))
~~~
{: .language-python}

    10


~~~
#A local variable with the same name gets priority
temperature = 37
def save_temperature(temp):
    #saves the value of temperature given to the function.
    temperature = temp
    return

print("temperature is", temperature)
save_temperature(25)
print("temperature is", temperature)
~~~
{: .language-python}

    temperature is 37
    temperature is 37
