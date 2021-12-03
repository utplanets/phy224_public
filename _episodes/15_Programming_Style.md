---
layout: episode
title: Programming Style
permalink: /15_Programming_Style
exercises: 5
keypoints: ['Follow standard Python style in your code.', 'Use docstrings to provide online help.']
objectives: ['Provide sound justifications for basic rules of coding style.', 'Refactor one-page programs to make them more readable and justify the changes.', 'Use Python community coding standards (PEP-8).']
questions: ['How can I make my programs more readable?', 'How do most programmers format their code?', 'How can programs check their own operation?']
teaching: 10
---

## Follow standard Python style in your code.
* Use 4 spaces as indentation
* Don't use 'from module import *' to import everything
* Use parentheses to make statements clear
* Use spaces to make code readable
* Document your code with comments

## Use docstrings to provide online help on your own functions
* If the first thing in a function is a character string that is not assigned to a variable, Python attaches it to the function as the online help.
* Called a docstring (short for “documentation string”).


~~~
def average(values):
    "Return average of values, or None if no values are supplied."
    
    if len(values) == 0:
        return None
    return sum(values) / average(values)

help(average)
~~~
{: .language-python}

    Help on function average in module __main__:
    
    average(values)
        Return average of values, or None if no values are supplied.



~~~
help(average)
~~~
{: .language-python}

    Help on function average in module __main__:
    
    average(values)
        Return average of values, or None if no values are supplied.



~~~
#multi-line strings are allowed

def distance(gravity, time): 
    """Return distance travelled under constant acceleration from gravity
    
    gravity: acceleration due to gravity (m/s^2)
    time : time travelled (seconds).
    
    returns: distance travelled in metres."""

    return 0.5 * gravity * time**2

help(distance)
~~~
{: .language-python}

    Help on function distance in module __main__:
    
    distance(gravity, time)
        Return distance travelled under constant acceleration from gravity
        
        gravity: acceleration due to gravity (m/s^2)
        time : time travelled (seconds).
        
        returns: distance travelled in metres.


## Exercise 1
What does this program do? Re-write to make it more readable and re-usable. **Make sure it still works**. Compare your rewrite with your neighbours.

    from math import *
    n=10
    r=10
    x=[]
    y=[]
    for i in range(n):
        x.append(r*cos(pi*i*2/9))
        y.append(r*sin(pi*i*2/9))
    print(x)
    print(y)
    


~~~
from math import *
n=10
r=10
x=[]
y=[]
for i in range(n):
    x.append(r*cos(pi*i*2/9))
    y.append(r*sin(pi*i*2/9))
print(x)
print(y)
~~~
{: .language-python}

    [10.0, 7.660444431189781, 1.7364817766693041, -4.999999999999998, -9.396926207859083, -9.396926207859085, -5.000000000000004, 1.7364817766692997, 7.660444431189779, 10.0]
    [0.0, 6.4278760968653925, 9.84807753012208, 8.660254037844389, 3.420201433256689, -3.4202014332566866, -8.660254037844384, -9.848077530122081, -6.427876096865396, -2.4492935982947065e-15]


~~~
from math import cos,sin
#Initialize variables
def make_circle(radius, number_of_points):
    x,y = [], []
    for i in range(number_of_points):
        theta = 2*pi*(i/(number_of_points-1))
        x.append(radius*cos(theta))
        y.append(radius*sin(theta))
    return x, y

x,y = make_circle(10, 10)
print(x)
print(y)
~~~
{: .language-python}

    [10.0, 7.660444431189781, 1.7364817766693041, -4.999999999999998, -9.396926207859083, -9.396926207859085, -5.000000000000004, 1.7364817766692997, 7.660444431189779, 10.0]
    [0.0, 6.4278760968653925, 9.84807753012208, 8.660254037844389, 3.420201433256689, -3.4202014332566866, -8.660254037844384, -9.848077530122081, -6.427876096865396, -2.4492935982947065e-15]
