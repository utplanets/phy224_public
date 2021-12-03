---
layout: episode
title: Numpy and Scipy
permalink: /06_Numpy
exercises: 10
keypoints: ['Use the numpy library to get basic statistics out of tabular data.', 'Print numpy arrays.', 'Use mean, sum, std to get summary statistics.', 'Add numpy arrays together.', 'Study the scipy website', 'Use scipy to integrate tabular data.']
objectives: ['Import the numpy library.', 'Understand the NDArray object.', 'Import the numpy library.', 'Get some basic information about a numpy and scipy objects and methods.']
questions: ['How do I deal with tabular scientific data?']
teaching: 40
---

## Numpy is the main Python library for scientific computation
* Numpy provides a new data type, the `array`
* `arrays` are multi-dimensional collections of data of the same intrinsic type (int, float, etc.)

## Import numpy before using it
* `numpy` is **not** built in, but is often installed by default.
* use `import numpy` to import the entire package.
* use `from numpy import ...` to import some functions.
* use `import numpy as np` to use the most common alias.


~~~
import numpy as np
import numpy
from numpy import cos

print(numpy.cos, np.cos, cos)
~~~
{: .language-python}

    <ufunc 'cos'> <ufunc 'cos'> <ufunc 'cos'>

## Use `numpy.zeros` to create empty arrays


~~~
f10 = numpy.zeros(10)
i10 = numpy.zeros(10, dtype=int)
print("default array of zeros: ", f10)
print("integer array of zeros: ", i10)
~~~
{: .language-python}

    default array of zeros:  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    integer array of zeros:  [0 0 0 0 0 0 0 0 0 0]

## Use `numpy.ones` to create an array of ones.


~~~
print("Using numpy.ones    : ", numpy.ones(10))
~~~
{: .language-python}

    Using numpy.ones    :  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

## Using `numpy.arange` to generate sets of numbers
* arange takes from one to three arguments. By default arange will generate numbers starting from 0 with a step of 1
* `arange(N)` generates numbers from 0..N-1
* `arange(M,N)` generates numbers from M..N-1
* `arange(M,N,P)` generates numbers from M..N-1 including only ever Pth number.

generate an array of numbers from 1 to 10

generate an array of numbers from 0 to 10


~~~
numpy.arange(10)
~~~
{: .language-python}




~~~
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
~~~
{: .output}



generate an array of numbers from 1 to 10


~~~
numpy.arange(1,10)
~~~
{: .language-python}




~~~
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
~~~
{: .output}



generate an array of odd numbers from 1 to 10


~~~
numpy.arange(1,10,2)
~~~
{: .language-python}




~~~
array([1, 3, 5, 7, 9])
~~~
{: .output}



**incorrectly** generate an array of odd numbers from 1 to 10, backwards


~~~
numpy.arange(1,10,-2)
~~~
{: .language-python}




~~~
array([], dtype=int64)
~~~
{: .output}



generate an array of even numbers from 10 to 2, backwards


~~~
numpy.arange(10,1,-2)
~~~
{: .language-python}




~~~
array([10,  8,  6,  4,  2])
~~~
{: .output}



## Numpy arrays have a `size`
* Numpy arrays have a `size` parameter associated with them



~~~
a = numpy.arange(10)
print("a.size is", a.size)
~~~
{: .language-python}

    a.size is 10

## Numpy arrays have a `shape`
* Numpy arrays have a `shape` parameter associated with them
* You can change the shape with the `reshape` method


~~~
a = numpy.arange(10)
print("a's shape is ",a.shape)

b=a.reshape(5,2)
print("b's shape is ",b.shape)
~~~
{: .language-python}

    a's shape is  (10,)
    b's shape is  (5, 2)

## Numpy arrays can be treated like single numbers in arithmetic
* Arithmetic using numpy arrays is *element-by-element*
* Matrix operations are possible with functions or methods.
* The size and shape of the arrays should match.


~~~
a = numpy.arange(5)
b = numpy.arange(5)
print("a=",a)
print("b=",b)
print("a+b=",a+b)
print("a*b=",a*b)
~~~
{: .language-python}

    a= [0 1 2 3 4]
    b= [0 1 2 3 4]
    a+b= [0 2 4 6 8]
    a*b= [ 0  1  4  9 16]


~~~
c = numpy.ones((5,2))
d = numpy.ones((5,2)) + 100
d
~~~
{: .language-python}




~~~
array([[101., 101.],
       [101., 101.],
       [101., 101.],
       [101., 101.],
       [101., 101.]])
~~~
{: .output}




~~~
c + d
~~~
{: .language-python}




~~~
array([[102., 102.],
       [102., 102.],
       [102., 102.],
       [102., 102.],
       [102., 102.]])
~~~
{: .output}



* Arrays need to have the same shape to be used together


~~~
e = numpy.ones((2,5))
c+e #c and e have different shapes
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-14-411d6bb0faff> in <module>
          1 e = numpy.ones((2,5))
    ----> 2 c+e #c and e have different shapes
    

    ValueError: operands could not be broadcast together with shapes (5,2) (2,5) 



~~~
print(e)
~~~
{: .language-python}

    [[1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]]

## The Numpy library has many functions that work on `arrays`
* Aggregation functions like `sum`,`mean`,`size`



~~~
a=numpy.arange(5)
print("a = ", a)
~~~
{: .language-python}

    a =  [0 1 2 3 4]

Add all of the elements of the array together.


~~~
print("sum(a) = ", a.sum())
~~~
{: .language-python}

    sum(a) =  10

Calculate the average value of the elements in the array.


~~~
print("mean(a) = ", a.mean())
~~~
{: .language-python}

    mean(a) =  2.0

Calculate something called `std` of the array.


~~~
print("std(a) = ", a.std()) #what is this?
~~~
{: .language-python}

    std(a) =  1.4142135623730951

Calculate the `sin` of each element in the array


~~~
print("np.sin(a) = ", np.sin(a))
~~~
{: .language-python}

    np.sin(a) =  [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]

* Note that the `math` library does not work with `numpy` arrays


~~~
import math
print("math.sin(a) = ", math.sin(a))
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-d1f037c9223e> in <module>
          1 import math
    ----> 2 print("math.sin(a) = ", math.sin(a))
    

    TypeError: only size-1 arrays can be converted to Python scalars


## Check the `numpy` help and webpage for more functions
https://docs.scipy.org/doc/numpy/reference/routines.html

## Use the `axis` keyword to use the function over a subset of the data.
* Many functions take the `axis` keyword to perform the aggregation of that dimension


~~~
a = numpy.arange(10).reshape(5,2)
print("a=",a)
print("mean(a)="  ,numpy.mean(a))
print("mean(a,0)=",numpy.mean(a,axis=0))
print("mean(a,1)=",numpy.mean(a,axis=1))
~~~
{: .language-python}

    a= [[0 1]
     [2 3]
     [4 5]
     [6 7]
     [8 9]]
    mean(a)= 4.5
    mean(a,0)= [4. 5.]
    mean(a,1)= [0.5 2.5 4.5 6.5 8.5]

## Use square brackets to access elements in the array
* Single integers in square brackets returns one element
* ranges of data can be accessed with slices


~~~
a=numpy.arange(10)
~~~
{: .language-python}

Access the fifth element


~~~
a[5]
~~~
{: .language-python}




~~~
5
~~~
{: .output}



Access elements 5 through 10


~~~
a[5:10]
~~~
{: .language-python}




~~~
array([5, 6, 7, 8, 9])
~~~
{: .output}



Access elements from 5 to the end of the array


~~~
a[5:]
~~~
{: .language-python}




~~~
array([5, 6, 7, 8, 9])
~~~
{: .output}



Access all elements from the start of the array to the fifth element.


~~~
a[:5]
~~~
{: .language-python}




~~~
array([0, 1, 2, 3, 4])
~~~
{: .output}



Access every 2nd element from the 5th to the 10th


~~~
a[5:10:2]
~~~
{: .language-python}




~~~
array([5, 7, 9])
~~~
{: .output}



Access every -2nd element from the 5th to the 10th. (**incorrect**)



~~~
a[5:10:-2]
~~~
{: .language-python}




~~~
array([], dtype=int64)
~~~
{: .output}



* Access every -2nd element from the 10th to the 5th. (**correct**)


~~~
a[10:5:-2]
~~~
{: .language-python}




~~~
array([9, 7])
~~~
{: .output}



## Exercise 1
There is an `arange` function and `linspace` function, that take similar arguments. Explain the difference. For example, what does the following code do?

    print (numpy.arange(1.,9,3))
    print (numpy.linspace(1.,9,3))


~~~
print (numpy.arange(1.,9,3))
print (numpy.linspace(1.,9,3))
~~~
{: .language-python}

    [1. 4. 7.]
    [1. 5. 9.]

* `arange` takes the arguments *start, stop, step*, and generates numbers from *start* to *stop* (excluding *stop*) stepping by *step* each time.
* `linspace` takes the arguments *start, stop, number*, and generates numbers from *start* to *stop* (including *stop*) with *number* of steps.

## Exercise 2
Generate a 10 x 3 array of random numbers (using `numpy.random.randn`). From each column, find the minimum absolute value. Make use of `numpy.abs` and `numpy.min` functions. The result should be a one-dimensional array.


~~~
a = numpy.random.randn(30).reshape(10,3)
print("a is ", a)
~~~
{: .language-python}

    a is  [[ 1.58892983  2.58439008  1.61861843]
     [-0.28303057  0.57369164 -0.64936983]
     [-0.08659006 -0.7244811  -0.82387512]
     [-0.3923705  -0.01850684  1.04478031]
     [-1.6540591  -2.58758121 -0.07830954]
     [-1.0516081  -1.34443688  0.59432557]
     [-0.41612675 -0.91907727 -0.5662153 ]
     [ 1.62108774  0.76359253 -1.07599141]
     [ 1.20358067  0.22846612  1.17882226]
     [ 1.78962118  0.97536824  1.05817893]]


~~~
print("min(a) along each column is ", numpy.min( numpy.abs( a ), axis=0))
~~~
{: .language-python}

    min(a) along each column is  [0.08659006 0.01850684 0.07830954]

## Use the `scipy` library for common scientific and numerical methods
* `scipy` contains functions to generate random numbers, calculate Fourier transforms, integrate
* Check the `scipy` website for more help: https://docs.scipy.org/doc/scipy/reference/

## Example : integrate y=x^2 from 0 to 10


~~~
x = numpy.arange(11) #including 10
y = x**2
import scipy.integrate
#by default, trapz assumes the independent variable is a list of integers from 0..N
int_x2 = scipy.integrate.trapz(y)
print("integral of x^2 from 0 to 10 = ", int_x2)#This value should be 10**3/3 = 333.333
~~~
{: .language-python}

    integral of x^2 from 0 to 10 =  335.0

## Exercise 3
Why isn't the integral of $x^2$ above exactly 333.333?


~~~
x = numpy.linspace(0,10,1000) # finer grid
y=x**2
print("integral of x^2 from 0 to 10 = ", scipy.integrate.trapz(y) )#This value should be 10**3/3 = 333.333
~~~
{: .language-python}

    integral of x^2 from 0 to 10 =  33300.01668335002

## Exercise 4
Why is the integral 100 times bigger than expected?


~~~
print("integral of x^2 from 0 to 10 = ", scipy.integrate.trapz(y,x) )#This value should be 10**3/3 = 333.333
~~~
{: .language-python}

    integral of x^2 from 0 to 10 =  333.333500333834

We'll come back to `scipy.optimize` later, when we fit models to experimental data.

More details: http://paris-swc.github.io/advanced-numpy-lesson/
