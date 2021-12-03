---
layout: episode
title: Libraries
permalink: /05_Libraries
exercises: 10
keypoints: ['Most of the power of a programming language is in its libraries.', 'A program must import a library module in order to use it.', 'Use `help` to learn about the contents of a library module.', 'Import specific items from a library to shorten programs.', 'Create an alias for a library when importing it to shorten programs.']
objectives: ['Explain what software libraries are and why programmers create and use them.', "Write programs that import and use libraries from Python's standard library.", 'Find and read documentation for standard libraries interactively (in the interpreter) and online.']
questions: ['How can I use software that other people have written?', 'How can I find out what that software does?']
teaching: 10
---

## Most of the power of a programming language is in its libraries.
A library is a collection of files that contains functions for use by other programs. Like a textbook is a collection of chapters with equations for use by other physicists.

## A program must import a library module before using it.
*   Use `import` to load a library module into a program's memory.
*   Then refer to things from the module as `module_name.thing_name`.
    *   Python uses `.` to mean "part of".
*   Using `math`, one of the modules in the standard library:




~~~
import math

print("pi is", math.pi)
print("cos(pi) is ", math.cos(math.pi)) #radians!
~~~
{: .language-python}

    pi is 3.141592653589793
    cos(pi) is  -1.0

## Use help to learn about the contents of a library module.


~~~
help(math)
~~~
{: .language-python}

    Help on module math:
    
    NAME
        math
    
    MODULE REFERENCE
        https://docs.python.org/3.8/library/math
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    DESCRIPTION
        This module provides access to the mathematical functions
        defined by the C standard.
    
    FUNCTIONS
        acos(x, /)
            Return the arc cosine (measured in radians) of x.
        
        acosh(x, /)
            Return the inverse hyperbolic cosine of x.
        
        asin(x, /)
            Return the arc sine (measured in radians) of x.
        
        asinh(x, /)
            Return the inverse hyperbolic sine of x.
        
        atan(x, /)
            Return the arc tangent (measured in radians) of x.
        
        atan2(y, x, /)
            Return the arc tangent (measured in radians) of y/x.
            
            Unlike atan(y/x), the signs of both x and y are considered.
        
        atanh(x, /)
            Return the inverse hyperbolic tangent of x.
        
        ceil(x, /)
            Return the ceiling of x as an Integral.
            
            This is the smallest integer >= x.
        
        comb(n, k, /)
            Number of ways to choose k items from n items without repetition and without order.
            
            Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
            to zero when k > n.
            
            Also called the binomial coefficient because it is equivalent
            to the coefficient of k-th term in polynomial expansion of the
            expression (1 + x)**n.
            
            Raises TypeError if either of the arguments are not integers.
            Raises ValueError if either of the arguments are negative.
        
        copysign(x, y, /)
            Return a float with the magnitude (absolute value) of x but the sign of y.
            
            On platforms that support signed zeros, copysign(1.0, -0.0)
            returns -1.0.
        
        cos(x, /)
            Return the cosine of x (measured in radians).
        
        cosh(x, /)
            Return the hyperbolic cosine of x.
        
        degrees(x, /)
            Convert angle x from radians to degrees.
        
        dist(p, q, /)
            Return the Euclidean distance between two points p and q.
            
            The points should be specified as sequences (or iterables) of
            coordinates.  Both inputs must have the same dimension.
            
            Roughly equivalent to:
                sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
        
        erf(x, /)
            Error function at x.
        
        erfc(x, /)
            Complementary error function at x.
        
        exp(x, /)
            Return e raised to the power of x.
        
        expm1(x, /)
            Return exp(x)-1.
            
            This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
        
        fabs(x, /)
            Return the absolute value of the float x.
        
        factorial(x, /)
            Find x!.
            
            Raise a ValueError if x is negative or non-integral.
        
        floor(x, /)
            Return the floor of x as an Integral.
            
            This is the largest integer <= x.
        
        fmod(x, y, /)
            Return fmod(x, y), according to platform C.
            
            x % y may differ.
        
        frexp(x, /)
            Return the mantissa and exponent of x, as pair (m, e).
            
            m is a float and e is an int, such that x = m * 2.**e.
            If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
        
        fsum(seq, /)
            Return an accurate floating point sum of values in the iterable seq.
            
            Assumes IEEE-754 floating point arithmetic.
        
        gamma(x, /)
            Gamma function at x.
        
        gcd(x, y, /)
            greatest common divisor of x and y
        
        hypot(...)
            hypot(*coordinates) -> value
            
            Multidimensional Euclidean distance from the origin to a point.
            
            Roughly equivalent to:
                sqrt(sum(x**2 for x in coordinates))
            
            For a two dimensional point (x, y), gives the hypotenuse
            using the Pythagorean theorem:  sqrt(x*x + y*y).
            
            For example, the hypotenuse of a 3/4/5 right triangle is:
            
                >>> hypot(3.0, 4.0)
                5.0
        
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
            Determine whether two floating point numbers are close in value.
            
              rel_tol
                maximum difference for being considered "close", relative to the
                magnitude of the input values
              abs_tol
                maximum difference for being considered "close", regardless of the
                magnitude of the input values
            
            Return True if a is close in value to b, and False otherwise.
            
            For the values to be considered close, the difference between them
            must be smaller than at least one of the tolerances.
            
            -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
            is, NaN is not close to anything, even itself.  inf and -inf are
            only close to themselves.
        
        isfinite(x, /)
            Return True if x is neither an infinity nor a NaN, and False otherwise.
        
        isinf(x, /)
            Return True if x is a positive or negative infinity, and False otherwise.
        
        isnan(x, /)
            Return True if x is a NaN (not a number), and False otherwise.
        
        isqrt(n, /)
            Return the integer part of the square root of the input.
        
        ldexp(x, i, /)
            Return x * (2**i).
            
            This is essentially the inverse of frexp().
        
        lgamma(x, /)
            Natural logarithm of absolute value of Gamma function at x.
        
        log(...)
            log(x, [base=math.e])
            Return the logarithm of x to the given base.
            
            If the base not specified, returns the natural logarithm (base e) of x.
        
        log10(x, /)
            Return the base 10 logarithm of x.
        
        log1p(x, /)
            Return the natural logarithm of 1+x (base e).
            
            The result is computed in a way which is accurate for x near zero.
        
        log2(x, /)
            Return the base 2 logarithm of x.
        
        modf(x, /)
            Return the fractional and integer parts of x.
            
            Both results carry the sign of x and are floats.
        
        perm(n, k=None, /)
            Number of ways to choose k items from n items without repetition and with order.
            
            Evaluates to n! / (n - k)! when k <= n and evaluates
            to zero when k > n.
            
            If k is not specified or is None, then k defaults to n
            and the function returns n!.
            
            Raises TypeError if either of the arguments are not integers.
            Raises ValueError if either of the arguments are negative.
        
        pow(x, y, /)
            Return x**y (x to the power of y).
        
        prod(iterable, /, *, start=1)
            Calculate the product of all the elements in the input iterable.
            
            The default start value for the product is 1.
            
            When the iterable is empty, return the start value.  This function is
            intended specifically for use with numeric values and may reject
            non-numeric types.
        
        radians(x, /)
            Convert angle x from degrees to radians.
        
        remainder(x, y, /)
            Difference between x and the closest integer multiple of y.
            
            Return x - n*y where n*y is the closest integer multiple of y.
            In the case where x is exactly halfway between two multiples of
            y, the nearest even value of n is used. The result is always exact.
        
        sin(x, /)
            Return the sine of x (measured in radians).
        
        sinh(x, /)
            Return the hyperbolic sine of x.
        
        sqrt(x, /)
            Return the square root of x.
        
        tan(x, /)
            Return the tangent of x (measured in radians).
        
        tanh(x, /)
            Return the hyperbolic tangent of x.
        
        trunc(x, /)
            Truncates the Real x to the nearest Integral toward 0.
            
            Uses the __trunc__ magic method.
    
    DATA
        e = 2.718281828459045
        inf = inf
        nan = nan
        pi = 3.141592653589793
        tau = 6.283185307179586
    
    FILE
        /Users/lee/anaconda3/lib/python3.8/lib-dynload/math.cpython-38-darwin.so
    


## Import specific items from a library module to shorten programs.
*   Use `from ... import ...` to load only specific items from a library module.
*   Then refer to them directly without library name as prefix.


~~~
from math import cos, pi
print("cos(pi) is ", cos(pi))
~~~
{: .language-python}

    cos(pi) is  -1.0

## Create an alias for a library module when importing it to shorten programs.
*   Use `import ... as ...` to give a library a short *alias* while importing it.
*   Then refer to items in the library using that shortened name.


~~~
import math as m
print("cos(pi) is ", m.cos(m.pi))
~~~
{: .language-python}

    cos(pi) is  -1.0

## Exercise 1

  1. What function from the `math` module can you use to calculate a square root without using `sqrt`?
  2. Since the library contains this function, why does `sqrt` exist?


## There are many libraries installed as `standard` with Python

https://docs.python.org/3/library/
    
    `math` - Mathematical functions
    `decimal` - Decimal fixed and floating point arithmetic
    `random` - random number generator
    `os` - operating system functions
    `string` - Common string library (used to make 'str' types)
    `io` - Core input/ouput functions
    `email` - Email handling package
    `html` - HTML support (including a web server)
    ...


## Exercise 2
Match the following print statements with the appropriate library calls.

Print commands:

  1. print("sin(pi/2) =",sin(pi/2))
  2. print("sin(pi/2) =",m.sin(m.pi/2))
  3. print("sin(pi/2) =",math.sin(math.pi/2))

Library calls:

  1. from math import sin,pi
  2. import math
  3. import math as m
  4. from math import *

## Exercise 3
Read the code below and try to identify what the errors are without running it. Run the code, and read the error message. What type of error is it?

    from math import log
    log(0)


~~~
from math import log
log(0)
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-d72e1d780bab> in <module>
          1 from math import log
    ----> 2 log(0)
    

    ValueError: math domain error
