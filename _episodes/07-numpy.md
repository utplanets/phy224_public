---
title: "Numpy and Scipy"
teaching: 40
exercises: 10
questions:
- "How do I deal with tabular scientific data?"
objectives:
- "Import the numpy library."
- "Understand the NDArray object."
- "Import the numpy library."
- "Get some basic information about a numpy and scipy objects and methods."
keypoints:
- "Use the numpy library to get basic statistics out of tabular data."
- "Print numpy arrays."
- "Use mean, sum, std to get summary statistics."
- "Add numpy arrays together."
- "Study the scipy website"
- "Use scipy to integrate tabular data."
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

~~~
<ufunc 'cos'> <ufunc 'cos'> <ufunc 'cos'>
~~~
{: .output}


## Use `numpy.zeros` to create empty arrays


~~~
f10 = numpy.zeros(10)
i10 = numpy.zeros(10, dtype=int)
print("default array of zeros: ", f10)
print("integer array of zeros: ", i10)
~~~
{: .language-python}

~~~
default array of zeros:  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
integer array of zeros:  [0 0 0 0 0 0 0 0 0 0]
~~~
{: .output}

## Use `numpy.ones` to create an array of ones.

~~~
print("Using numpy.ones    : ", numpy.ones(10))
print("is the same thing as: ", numpy.zeros(10)+1)
~~~
{: .language-python}

~~~

Using numpy.ones    :  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
is the same thing as:  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
~~~
{: .output}

## Using `numpy.arange` to generate sets of numbers
* arange takes from one to three arguments. By default arange will generate numbers starting from 0 with a step of 1
* `arange(N)` generates numbers from 0..N-1
* `arange(M,N)` generates numbers from M..N-1
* `arange(M,N,P)` generates numbers from M..N-1 including only ever Pth number.


~~~
numpy.arange(10)
~~~
{: .language-python}
~~~
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
~~~
{: .output}

* generate an array of numbers from 1 to 10

~~~
numpy.arange(1,10)
~~~
{: .language-python}
~~~
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
~~~
{: .output}

* generate an array of odd numbers from 1 to 10

~~~
numpy.arange(1,10,2)
~~~
{: .language-python}
~~~
array([1, 3, 5, 7, 9])
~~~
{: .output}

* **incorrectly** generate an array of odd numbers from 1 to 10, backwards

~~~
numpy.arange(1,10,-2)
~~~
{: .language-python}
~~~
array([], dtype=int64)
~~~
{: .output}

* generate an array of even numbers from 10 to 2, backwards

~~~
numpy.arange(10,1,-2)
~~~
{: .language-python}
~~~
array([10,  8,  6,  4,  2])
~~~
{: .output}


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
~~~
a's shape is  (10,)
b's shape is  (5, 2)
~~~
{: .output}

## Numpy arrays can be treated like single numbers in arithmetic
* Arithmetic using numpy arrays is *element-by-element*
* Matrix operations are possible with functions or methods.
* The size and shape of the arrays should match.


~~~
a = numpy.arange(5)
b = numpy.arange(5)
print("a=",a)
print("b=",b)
print("a*b=",a*b)
print("a+b=",a+b)
~~~
{: .language-python}
~~~
a= [0 1 2 3 4]
b= [0 1 2 3 4]
a*b= [ 0  1  4  9 16]
a+b= [0 2 4 6 8]
~~~
{: .output}


~~~
c = numpy.ones((5,2))
d = numpy.ones((5,2)) + 100
c+d
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


~~~
e = c.reshape(2,5)
c+e #c and e have different shapes
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-46-0e32881b9afe> in <module>()
      1 e = c.reshape(2,5)
----> 2 c+e #c and e have different shapes

ValueError: operands could not be broadcast together with shapes (5,2) (2,5) 
---------------------------------------------------------------------------
~~~
{: .error}

## The Numpy library has many functions that work on `arrays`
* Aggregation functions like `sum`,`mean`,`size`



~~~
a=numpy.arange(5)
print("a = ", a)
~~~
{: .language-python}
~~~
a =  [0 1 2 3 4]
~~~
{: .output}

* Add all of the elements of the array together.

~~~
print("sum(a) = ", a.sum())
~~~
{: .language-python}
~~~
sum(a) =  10
~~~
{: .output}

* Calculate the average value of the elements in the array.

~~~
print("mean(a) = ", a.mean())
~~~
{: .language-python}
~~~
mean(a) =  2.0
~~~
{: .output}


* Calculate something called `std` of the array.

~~~
print("std(a) = ", a.std()) #what is this?
~~~
{: .language-python}
~~~
std(a) =  1.4142135623730951
~~~
{: .output}

* Calculate the `sin` of each element in the array

~~~
print("np.sin(a) = ", np.sin(a))
~~~
{: .language-python}
~~~
np.sin(a) =  [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]
~~~
{: .output}


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

~~~
a= [[0 1]
    [2 3]
    [4 5]
    [6 7]
    [8 9]]
mean(a)= 4.5
mean(a,0)= [4. 5.]
mean(a,1)= [0.5 2.5 4.5 6.5 8.5]
~~~
{: .output}


## Use square brackets to access elements in the array
* Single integers in square brackets returns one element
* ranges of data can be accessed with slices


~~~
a=numpy.arange(10)
~~~
{: .language-python}

* Access the fifth element

~~~
a[5]
~~~
{: .output}
~~~
5
~~~
{: .output}

* Access elements 5 through 10

~~~
a[5:10]
~~~
{: .language-python}

~~~
array([5, 6, 7, 8, 9])
~~~
{: .output}

* Access elements from 5 to the end of the array

~~~
a[5:] #No second number means "rest of the array"
~~~
{: .language-python}

~~~
array([5, 6, 7, 8, 9])
~~~
{: .output}

* Access all elements from the start of the array to the fifth element.

~~~
a[:5] #No first number means "from the start of the array"
~~~
{: .language-python}

~~~
array([0, 1, 2, 3, 4])
~~~
{: .output}

* Access every 2nd element from the 5th to the 10th

~~~
a[5:10:2] #A third number means "every Nth element"
~~~
{: .language-python}
~~~
array([5, 7, 9])
~~~
{: .output}

* Access every -2nd element from the 5th to the 10th. (**incorrect**)

~~~
a[5:10:-2] #negative numbers mean "count backwards"
~~~
{: .language-python}

~~~
array([], dtype=int64)
~~~
{: .output}

* Access every -2nd element from the 10th to the 5th. (**correct**)

~~~
a[10:5:-2] #but you need to start and stop in the same order
~~~
{: .language-python}


~~~
array([9, 7])
~~~
{: .output}


> ## Challenge 1
> There is an `arange` function and `linspace` function, that take similar arguments. Explain the difference. For example, what does the following code do?
> 
> ~~~
> print (numpy.arange(1.,9,3))
> print (numpy.linspace(1.,9,3))
> ~~~
> {: .language-python}
> > ## Solution
> > * `arange` takes the arguments *start, stop, step*, and generates numbers from *start* to *stop* (excluding *stop*) stepping by *step* each time.
> > * `linspace` takes the arguments *start, stop, number*, and generates numbers from *start* to *stop* (including *stop*) with *number* of steps.
> >
> > ~~~
> > print (numpy.arange(1.,9,3))
> > print (numpy.linspace(1.,9,3))
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > [1. 4. 7.]
> > [1. 5. 9.]
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}


> ## Challenge 2
>
> Generate a 10 x 3 array of random numbers (using `numpy.random.rand`). From each row, find the minimum absolute value. Make use of numpy.abs and numpy.min. The result should be a one-dimensional array.
>
> > ## Solution
> > The important part of the solution is passing the `axis` keyword to the min function:
> > 
> > ~~~
> > a = numpy.random.rand(30).reshape(10,3)
> > print("a is ", a)
> > print()
> > print("min(a) along each row is ", numpy.min( numpy.abs( a ), axis=0))
> > ~~~
> >{: .language-python}
> {: .solution}
{: .challenge}

## Use the `scipy` library for common scientific and numerical methods
* `scipy` contains functions to generate random numbers, calculate Fourier transforms, integrate
* Check the `scipy` website for more help: https://docs.scipy.org/doc/scipy/reference/

## Example : integrate y=x^2 from 0 to 10


~~~
x = numpy.arange(11)
y = x**2
import scipy.integrate
#by default, trapz assumes the independent variable is a list of integers from 0..N
print("integral of x^2 from 0 to 10", scipy.integrate.trapz(y) )#This value should be 10**3/3 = 333
~~~
{: .language-python}

~~~
integral of x^2 from 0 to 10 335.0
~~~
{: .output}

* Numerical integration can be inprecise with a coarse grid. (this time, incorrectly!)

~~~
x = numpy.linspace(0,10,1000) # finer grid
y=x**2
print("integral of x^2 from 0 to 10", scipy.integrate.trapz(y) )#This value should be 10**3/3 = 333.333
~~~
{: .language-python}

~~~
integral of x^2 from 0 to 10 33300.01668335002
~~~
{: .output}

* Passing the `x` values to `trapz` allows it to integrate correctly

~~~
print("integral of x^2 from 0 to 10", scipy.integrate.trapz(y,x) )#This value should be 10**3/3 = 333.333
~~~
{: .language-python}

~~~
integral of x^2 from 0 to 10 333.333500333834
~~~
{: .output}

We'll come back to `scipy.optimize` later.
