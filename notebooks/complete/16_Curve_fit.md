## Data analysis with Python

Many physical systems can be modeled as an equation, which in Python would be represented by a function $f$. If an appropriate function $f$ can be found for an experiment we can use the equation to determine physical parameters releted to the experiment, and we can use this new model to *predict* new things about the world. Galileo used this method to calculate the trajectory of canonballs by rolling them down inclined ramps.

In experimental physics, we constrain these models by designing an experiment with two quantities. The first quantity, that we can control, is the **independent variable**. The second quantity, that we can measure, is the **dependent variable**.  The relationship between these two quantities can then be used to determine some physical parameters.

A simple example of measuring the path of moving object. We could guess that the model is moving at a constant speed and design an experiment to find that speed using the model:

$$ s = ut $$

## Scipy provides functions that can fit model functions to data.

`Scipy` provides a number of functions that, given a suitable model function, can return the *best estimate* of the unknown parameters in the model.

Consider the experiment where the time of flight of an object moving at constant speed is measured. If the experiment is correctly setup. The unknown variable we are trying to determine is the speed $u$. The remaining variables are time $t$ and height $s$. We can design two different experiments, one where we control *time* (measuring at a fixed interval) and measure *distance*, or one where we control *distance* and measure *time*.

In Python the model function might be written as:


```python
def distance(time, speed):
    """Calculate the distance travelled at a constant speed for a known time."""
    return speed * time

def model_function(independent_data, parameter1, parameter2):
    """A template for the model function."""
    dependent_data = parameter1 * independent_data + parameter2
    return dependent_data
```


```python
#control time, measure distance
import numpy
# derr is my estimate of errors measuring distance, my ruler is bad.
derr = 5 # metres
measured_times =numpy.arange(10,100,10) #time in seconds
measured_distances = numpy.array([ 108.2,  220.4,  360.2,  482.8,
        630.6,  793.9,  947.5, 1125.0, 1314.9]) # distance in metres
distance_errors = numpy.ones_like(measured_distances)*derr
```

For such a simple model, the average speed can be calculated from the data quite easily.


```python
speeds = measured_distances / measured_times
average_speed = numpy.average(speeds)
print("Average speed is {:.04g} m/s".format(average_speed))
mean_times_error = numpy.std(speeds, ddof=1)/numpy.sqrt(speeds.size)
mean_times_std = numpy.sqrt( numpy.mean( derr**2 * numpy.ones(speeds.size)) )

#error propagation, sum in quadrature
speed_error = numpy.sqrt( numpy.mean( (distance_errors / measured_distances)**2) )* average_speed
print("Standard error in average speed is {:.03g} m/s".format(mean_times_error))
print("Error in average speed is {:.03g} m/s".format(speed_error))
```

    Average speed is 12.66 m/s
    Standard error in average speed is 0.436 m/s
    Error in average speed is 0.236 m/s



```python
# Copied here to make it easier to find!
def distance(time, speed):
    """Calculate the distance travelled at a constant speed for a known time."""
    return speed * time
```

* You can also use `scipy.optimize.curve_fit` to perform this calculation.


```python
from scipy.optimize import curve_fit

popt, pcov = curve_fit(distance, measured_times, measured_distances)

print("Speed is %4g m/s" % popt[0])

pvar = numpy.diag(pcov)
print("Error in fitted speed is {:.03g} m/s".format(numpy.sqrt(pvar[0])))
```

    Speed is 13.6645 m/s
    Error in fitted speed is 0.31 m/s


## What is `popt`, `pvar`?

* `popt` is a one dimensional array of the best estimates for the parameter values, each entry matches the order in the function definition
* `pcov` is the covariance matrix showing the uncertainty and interdependence of each parameter in `popt`. We take the diagonal elements as `pvar` for the variance of each parameter in `popt`.

* The above error didn't consider the errors in the individual data points correctly.
* Give `curve_fit` the error values using the `sigma` keyword, and always use `absolute_sigma=True`

## Exercise 1
Predict the value of distance at after 10 seconds and 100s.

## Calculate predictions using the model function
* `curve_fit` needs a model function to make predictions.
* Any calculations using that model should also use the function to avoid errors
* e.g. when plotting the predictions you should call the model_function, *and not rewrite the equation*


```python
# Always predict with the model function!
d10 = distance(10, popt[0])
d100 = distance(100, popt[0])
print("After 10 seconds, predicted distance = {:.4g}m".format(d10))
print("After 100 seconds, predicted distance = {:.4g}m".format(d100))

#dont_do_this
rewrite10 = popt[0] * 10
print("After 10 seconds, predicted distance = {:.4g}m".format(rewrite10))

#or this
hardcoded10 = 13.64 * 10
print("After 10 seconds, predicted distance = {:.4g}m".format(hardcoded10))
```

    After 10 seconds, predicted distance = 136.6m
    After 100 seconds, predicted distance = 1366m
    After 10 seconds, predicted distance = 136.6m
    After 10 seconds, predicted distance = 136.4m



```python
popt, pcov = curve_fit(distance, measured_times, measured_distances,
                       absolute_sigma=True, sigma = distance_errors)
pvar = numpy.diag(pcov)

print("Average speed is {:.04g} m/s".format(popt[0]))
print("Error in fitted speed is {:.03g} m/s".format(numpy.sqrt(pvar[0])))
```

    Average speed is 13.66 m/s
    Error in fitted speed is 0.0296 m/s


* With the correct error estimates, the model is more certain about the speed, but the eastimate of the average speed didn't change.

## The model function needs to follow the `curve_fit` rules
* The function must take and array of **independent data** as its first argument
* The function can take any number of additional parameters that will be found using `curve_fit`
* The function must return a single prediction of the **dependent data** for each value in the independent data.


```python
def good_model_function(xdata, parameter_1, parameter_2, parameter_3):
    # code_that_calculates_a_model
    return prediction
```

## `curve_fit` works with multiple parameters

Extending the above experiment, what if the object was actually accelerating? The model function is now

$$ s = ut + \frac{1}{2} at^2$$

where $a$ is the acceleration. We can change the model function and run the `curve_fit` code again


```python
def distance_with_acceleration(time, speed, acceleration):
    """Calculate the distance travelled with at a constant speed for a known time
    and constant acceleration."""
    return speed * time + 0.5 * acceleration * time**2

from scipy.optimize import curve_fit
popt2, pcov2 = curve_fit(distance_with_acceleration, measured_times, measured_distances,
                       absolute_sigma=True, sigma = distance_errors)
print("Initial speed is {:.04g} m/s".format(popt2[0]))
print("Error in fitted initial speed is {:.03g} m/s".format(numpy.sqrt(pcov2[0,0])))

print("Acceleration is {:.04g} m/s2".format(popt2[1]))
print("Error in fitted acceleration is {:.03g} m/s2".format(numpy.sqrt(pcov2[1,1])))
```

    Initial speed is 10.26 m/s
    Error in fitted initial speed is 0.119 m/s
    Acceleration is 0.09589 m/s2
    Error in fitted acceleration is 0.00325 m/s2


The data use here is fake, generated with an initial speed of 10.86 m/s and an acceleration of 0.1$m/s^2$. The model with constant speed predicted a higher speed to compensate for the acceleration!

## Exercise 1
How could we have quickly checked whether our model was good?

A **plot** would have quickly showed the linear model is not correct, or printing each value predicted might tell us something too for small amounts of data.




```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(8,6))
plt.errorbar(measured_times, measured_distances,yerr=distance_errors, marker='o', linestyle='none', label="measured data")
plt.plot(measured_times, distance(measured_times, numpy.mean(speeds)),label='simple average')
plt.plot(measured_times, distance(measured_times, popt[0]),label='$s=ut$')
plt.plot(measured_times, distance_with_acceleration(measured_times, popt2[0],popt2[1]),label=r'$s=ut+\frac{1}{2}at^2$')
plt.legend(fontsize=14)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)");
```

![png](../fig/16_Curve_fit_files/16_Curve_fit_24_1.png)



**Always plot your data and model fits.**

## Plotting residuals

Once you have a model prediction, you can check for problems in the model using a residual plot. Plot the difference between the model prediction and the measured data.



```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(8,6))
plt.plot(measured_times, distance(measured_times, numpy.mean(speeds))-measured_distances,label='simple average',marker='o',ls='')
plt.plot(measured_times, distance(measured_times, popt[0])-measured_distances,label='$s=ut$',marker='s',ls='')
plt.plot(measured_times, distance_with_acceleration(measured_times, popt2[0],popt2[1])-measured_distances,label=r'$s=ut+\frac{1}{2}at^2$',marker='<',ls='')
plt.legend(fontsize=14)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)");
```

![png](../fig/16_Curve_fit_files/16_Curve_fit_27_1.png)



In this example you can see that the linear model (`simple average` or `s=ut`) deviates from the data in a way that depends on the `independent variable` (time). If the model fit is good we expect to see differences betwee model and data that are random in magnitude and location (as in the quadratic fit).

## `curve_fit` find the *best estimate* of the parameters using by minimizing **chi squared**.
* Curve fit works by finding the combination of parameters that gives the lowest value of a parameter $\chi^2$, defined as

$$\chi^2 = \sum\frac{(y_i - f(x_i))^2}{\sigma_{y_i}^2}$$

* The lower the value of $\chi^2$, the closer the model is **on average** to each measured data point.
* This metric penalizes outliers disproportionally because of the square factor
* The metric weights the penalty of each point by the inverse of the standard deviation, penalizing (genuinely) noisier outliers less than less noisy outliers.

## **Reduced chi squared** is easier to understand and compare between data sets.
* The value of $\chi^2$ for a good model depends on the number of data points and model parameters.
* A related variable $$\chi_r^2 = \frac{\chi^2}{\mathrm{dof}}$$ is defined such that a the ideal value is 1.0.  
* To get the metric we need the number of **degrees of freedom** (dof) defined as the number of data points (N) minus the number of unknown parameters (m) $$\mathrm{dof} = N - m$$.

* High values of $\chi_r^2$ are bad and suggest the model does a poor job of fitting the data.
* Low values (<<1) are also bad, suggesting the model fits the data **too well**.
* A low value suggests the model is fitting data better than the average error in the data should allow.


```python
def chi2(y_measure,y_predict,errors):
    """Calculate the chi squared value given a measurement with errors and prediction"""
    return numpy.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    """Calculate the reduced chi squared value given a measurement with errors and prediction,
    and knowing the number of parameters in the model."""
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)
```


```python
print("Constant velocity model chi2r=",chi2reduced(measured_distances,
                                        distance(measured_times,popt[0]),
                                        distance_errors,
                                        1))

print("Constant acceleration model chi2r=",chi2reduced(measured_distances,
                                        distance_with_acceleration(measured_times,popt2[0],popt2[1]),
                                        distance_errors,
                                        2))
```

    Constant velocity model chi2r= 109.63987561403505
    Constant acceleration model chi2r= 1.1810606671759618


**Chi square values should be rounded to a small number of digits, keeping only 1 or 2 significant figures.**


```python
print("Constant velocity model chi2r=",round(chi2reduced(measured_distances,
                                        distance(measured_times,popt[0]),
                                        distance_errors,
                                        1),-1))

print("Constant acceleration model chi2r=",round(chi2reduced(measured_distances,
                                        distance_with_acceleration(measured_times,popt2[0],popt2[1]),
                                        distance_errors,
                                        2),1))
```

    Constant velocity model chi2r= 110.0
    Constant acceleration model chi2r= 1.2


## Exercise 2
Put a print statement inside the model function `distance_with_acceleration` to print out the parameter values. What is happening to the parameter values?


```python
def distance_with_acceleration_print(time, speed, acceleration):
    """Calculate the distance travelled with at a constant speed for a known time
    and constant acceleration."""

    print ("speed=",speed, "acceleration=",acceleration)
    return speed * time + 0.5 * acceleration * time**2

popt2, pcov2 = curve_fit(distance_with_acceleration_print, measured_times, measured_distances,
                       absolute_sigma=True, sigma = distance_errors)

```

    speed= 1.0 acceleration= 1.0
    speed= 1.0 acceleration= 1.0
    speed= 1.0 acceleration= 1.0
    speed= 1.0000000149011612 acceleration= 1.0
    speed= 1.0 acceleration= 1.0000000149011612
    speed= 10.257717023193093 acceleration= 0.0958943850247661
    speed= 10.257717176044988 acceleration= 0.0958943850247661
    speed= 10.257717023193093 acceleration= 0.0958943864537038
    speed= 10.257717023531002 acceleration= 0.09589438501373611


## Non-linear regression
* Mathematically, `curve_fit` is using *least squared error regression* to find the best parameter estimate.
* `curve_fit` works with non linear model (e.g. $y=at^{(b-1)}+c$) and the error estimates are usually correct.

## When fitting non-linear functions, use the `p0` keyword to start `curve_fit` with a good estimate
* `p0` is used to provide a first guess of the parameters you are trying to find
* If you have some idea of a parameter value, use `p0` to give `curve_fit` a better chance of finding the global minimum error for non-linear functions
* Don't be too precise so as not to bias the fitting process.


```python
iteration=0

def nonlinear_function(t, a, b, c,verbose=True):
    global iteration
    if verbose:
        print (iteration, "a=",a, "b=",b, "c=",c)
    iteration = iteration+1
    return a*t**(b-1) + c

#generated "good" data
t=numpy.arange(10)
y=numpy.array([-0.173, 2.12, 9.42, 19.69, 37.16, 59.40, 96.59, 119.448, 158.0,201.9])
sigmaNL = numpy.ones(10)*0.5
```

First, try fitting the non-linear function with no initial guess


```python
iteration=0
poptNL1, pcovNL1 = curve_fit(nonlinear_function, t, y,
                       absolute_sigma=True, sigma = sigmaNL)
```

    0 a= 1.0 b= 1.0 c= 1.0
    1 a= 1.0 b= 1.0 c= 1.0
    2 a= 1.0 b= 1.0 c= 1.0
    3 a= 1.0000000149011612 b= 1.0 c= 1.0
    4 a= 1.0 b= 1.0000000149011612 c= 1.0
    5 a= 1.0 b= 1.0 c= 1.0000000149011612
    6 a= 77.19199892187382 b= 1.000001167729559 c= 1.0
    7 a= 77.19200007212423 b= 1.000001167729559 c= 1.0
    8 a= 77.19199892187382 b= 1.0000011826307376 c= 1.0
    9 a= 77.19199892187382 b= 1.000001167729559 c= 1.0000000149011612
    10 a= 78.36447902457489 b= 1.0000087185633595 c= -0.17339350031973977
    11 a= 78.36448019229663 b= 1.0000087185633595 c= -0.17339350031973977
    12 a= 78.36447902457489 b= 1.0000087334646506 c= -0.17339350031973977
    13 a= 78.36447902457489 b= 1.0000087185633595 c= -0.17339349773597526
    14 a= 78.36575304520085 b= 1.000023821040081 c= -0.1760675336783647
    15 a= 78.36575421294157 b= 1.000023821040081 c= -0.1760675336783647
    16 a= 78.36575304520085 b= 1.0000238359415972 c= -0.1760675336783647
    17 a= 78.36575304520085 b= 1.000023821040081 c= -0.176067531054754
    18 a= 78.36829338606314 b= 1.000054025993526 c= -0.18138432562329934
    19 a= 78.36829455384172 b= 1.000054025993526 c= -0.18138432562329934
    20 a= 78.36829338606314 b= 1.0000540408954923 c= -0.18138432562329934
    21 a= 78.36829338606314 b= 1.000054025993526 c= -0.18138432292046228
    22 a= 78.37336537641278 b= 1.000114435900421 c= -0.19201089205528044
    23 a= 78.37336654426693 b= 1.000114435900421 c= -0.19201089205528044
    24 a= 78.37336537641278 b= 1.0001144508032875 c= -0.19201089205528044
    25 a= 78.37336537641278 b= 1.000114435900421 c= -0.19201088919409517
    26 a= 78.38350855879007 b= 1.0002352557142202 c= -0.2132664884449126
    27 a= 78.38350972679537 b= 1.0002352557142202 c= -0.2132664884449126
    28 a= 78.38350855879007 b= 1.000235270618887 c= -0.2132664884449126
    29 a= 78.38350855879007 b= 1.0002352557142202 c= -0.2132664852669943
    30 a= 78.40375805726882 b= 1.000476895341837 c= -0.2557573412755463
    31 a= 78.40375922557585 b= 1.000476895341837 c= -0.2557573412755463
    32 a= 78.40375805726882 b= 1.0004769102501045 c= -0.2557573412755463
    33 a= 78.40375805726882 b= 1.000476895341837 c= -0.2557573374644649
    34 a= 78.44414069436054 b= 1.000960174597108 c= -0.34068544025678876
    35 a= 78.44414186326932 b= 1.000960174597108 c= -0.34068544025678876
    36 a= 78.44414069436054 b= 1.0009601895125768 c= -0.34068544025678876
    37 a= 78.44414069436054 b= 1.000960174597108 c= -0.3406854351801801
    38 a= 78.52440809519321 b= 1.001926733107724 c= -0.5102975962995859
    39 a= 78.52440926529808 b= 1.001926733107724 c= -0.5102975962995859
    40 a= 78.52440809519321 b= 1.0019267480375957 c= -0.5102975962995859
    41 a= 78.52440809519321 b= 1.001926733107724 c= -0.5102975886955592
    42 a= 78.68295365023071 b= 1.003859850129104 c= -0.8485450008432245
    43 a= 78.6829548226981 b= 1.003859850129104 c= -0.8485450008432245
    44 a= 78.68295365023071 b= 1.0038598650877815 c= -0.8485450008432245
    45 a= 78.68295365023071 b= 1.003859850129104 c= -0.8485449881989187
    46 a= 78.99212226862176 b= 1.0077260841721594 c= -1.5211266928787794
    47 a= 78.99212344569611 b= 1.0077260841721594 c= -1.5211266928787794
    48 a= 78.99212226862176 b= 1.0077260991884482 c= -1.5211266928787794
    49 a= 78.99212226862176 b= 1.0077260841721594 c= -1.5211266702122255
    50 a= 79.57868943929664 b= 1.0154585522588568 c= -2.8503134467953046
    51 a= 79.57869062511152 b= 1.0154585522588568 c= -2.8503134467953046
    52 a= 79.57868943929664 b= 1.0154585673903684 c= -2.8503134467953046
    53 a= 79.57868943929664 b= 1.0154585522588568 c= -2.8503134043223244
    54 a= 80.62467437532132 b= 1.030923488433409 c= -5.442612199580205
    55 a= 80.6246755767226 b= 1.030923488433409 c= -5.442612199580205
    56 a= 80.62467437532132 b= 1.0309235037953661 c= -5.442612199580205
    57 a= 80.62467437532132 b= 1.030923488433409 c= -5.442612118478964
    58 a= 82.2158698174953 b= 1.0617996243516288 c= -10.346968085161677
    59 a= 82.21587104260723 b= 1.0617996243516288 c= -10.346968085161677
    60 a= 82.2158698174953 b= 1.0617996401736762 c= -10.346968085161677
    61 a= 82.2158698174953 b= 1.0617996243516288 c= -10.346967930979838
    62 a= 83.56036137648809 b= 1.1224174405023146 c= -18.939483341565204
    63 a= 83.5603626216345 b= 1.1224174405023146 c= -18.939483341565204
    64 a= 83.56036137648809 b= 1.1224174572276377 c= -18.939483341565204
    65 a= 83.56036137648809 b= 1.1224174405023146 c= -18.93948305934491
    66 a= 80.5850336122205 b= 1.234017487351611 c= -31.058503871201538
    67 a= 80.58503481303107 b= 1.234017487351611 c= -31.058503871201538
    68 a= 80.5850336122205 b= 1.2340175057399045 c= -31.058503871201538
    69 a= 80.5850336122205 b= 1.234017487351611 c= -31.058503408393765
    70 a= 56.751362765850736 b= 1.4572175810494246 c= -36.55974194846282
    71 a= 56.75136361151194 b= 1.4572175810494246 c= -36.55974194846282
    72 a= 56.751362765850736 b= 1.4572176027636585 c= -36.55974194846282
    73 a= 56.751362765850736 b= 1.4572175810494246 c= -36.55974140368021
    74 a= 9.412848751161384 b= 1.903617768434505 c= -19.878029688803014
    75 a= 61.483657606423286 b= 1.524144259376958 c= -51.41844279867909
    76 a= 61.48365852260118 b= 1.524144259376958 c= -51.41844279867909
    77 a= 61.483657606423286 b= 1.5241442820884774 c= -51.41844279867909
    78 a= 61.483657606423286 b= 1.524144259376958 c= -51.418442032484585
    79 a= 44.06479582132333 b= 1.6458995337301787 c= -42.57579487686705
    80 a= 44.06479647793996 b= 1.6458995337301787 c= -42.57579487686705
    81 a= 44.06479582132333 b= 1.645899558255993 c= -42.57579487686705
    82 a= 44.06479582132333 b= 1.6458995337301787 c= -42.57579424243827
    83 a= 22.7416696308516 b= 1.8894100824492441 c= -29.274728397158896
    84 a= 22.741669969728886 b= 1.8894100824492441 c= -29.274728397158896
    85 a= 22.7416696308516 b= 1.8894101106036483 c= -29.274728397158896
    86 a= 22.7416696308516 b= 1.8894100824492441 c= -29.27472796093145
    87 a= 22.2141582032497 b= 2.0111653568227528 c= -29.856751452833294
    88 a= 22.214158534266453 b= 2.0111653568227528 c= -29.856751452833294
    89 a= 22.2141582032497 b= 2.011165386791452 c= -29.856751452833294
    90 a= 22.2141582032497 b= 2.0111653568227528 c= -29.856751007933028
    91 a= 9.497781313321376 b= 2.2546759055471783 c= -16.906666709857994
    92 a= 20.05615668776253 b= 2.048325511608447 c= -28.351196482361924
    93 a= 20.056156986622554 b= 2.048325511608447 c= -28.351196482361924
    94 a= 20.05615668776253 b= 2.0483255421308755 c= -28.351196482361924
    95 a= 20.05615668776253 b= 2.048325511608447 c= -28.351196059896175
    96 a= 16.815249036138148 b= 2.1226458211826924 c= -24.948997071547023
    97 a= 16.815249286704884 b= 2.1226458211826924 c= -24.948997071547023
    98 a= 16.815249036138148 b= 2.12264585281258 c= -24.948997071547023
    99 a= 16.815249036138148 b= 2.1226458211826924 c= -24.948996699777997
    100 a= 11.48695742632615 b= 2.2712864403323305 c= -18.789672870111083
    101 a= 11.486957597495154 b= 2.2712864403323305 c= -18.789672870111083
    102 a= 11.48695742632615 b= 2.2712864741771357 c= -18.789672870111083
    103 a= 11.48695742632615 b= 2.2712864403323305 c= -18.78967259012314
    104 a= 8.544378433515524 b= 2.4199270594868105 c= -14.65085975375216
    105 a= 8.544378560836684 b= 2.4199270594868105 c= -14.65085975375216
    106 a= 8.544378433515524 b= 2.4199270955465337 c= -14.65085975375216
    107 a= 8.544378433515524 b= 2.4199270594868105 c= -14.650859535437338
    108 a= 3.2609266364710763 b= 2.7172082977909886 c= -5.60823942271983
    109 a= 8.373210355989729 b= 2.449655183319498 c= -14.33534836306235
    110 a= 8.373210480760285 b= 2.449655183319498 c= -14.33534836306235
    111 a= 8.373210355989729 b= 2.449655219822205 c= -14.33534836306235
    112 a= 8.373210355989729 b= 2.449655183319498 c= -14.335348149449013
    113 a= 7.364773878272835 b= 2.5037365105888902 c= -12.612719725376273
    114 a= 7.364773988016518 b= 2.5037365105888902 c= -12.612719725376273
    115 a= 7.364773878272835 b= 2.5037365478974714 c= -12.612719725376273
    116 a= 7.364773878272835 b= 2.5037365105888902 c= -12.612719537432103
    117 a= 5.663437146924743 b= 2.6118991651285066 c= -9.462143335426791
    118 a= 5.663437231316532 b= 2.6118991651285066 c= -9.462143335426791
    119 a= 5.663437146924743 b= 2.611899204048837 c= -9.462143335426791
    120 a= 5.663437146924743 b= 2.6118991651285066 c= -9.462143194429869
    121 a= 4.506763928272086 b= 2.720061819669977 c= -6.903364231974335
    122 a= 4.506763995428102 b= 2.720061819669977 c= -6.903364231974335
    123 a= 4.506763928272086 b= 2.7200618602020565 c= -6.903364231974335
    124 a= 4.506763928272086 b= 2.720061819669977 c= -6.903364129106191
    125 a= 2.471220994398413 b= 2.936387128751198 c= -1.7556672756894924
    126 a= 4.410104786995485 b= 2.7416943505792655 c= -6.570524445207402
    127 a= 4.410104852711168 b= 2.7416943505792655 c= -6.570524445207402
    128 a= 4.410104786995485 b= 2.741694391433695 c= -6.570524445207402
    129 a= 4.410104786995485 b= 2.7416943505792655 c= -6.570524347298958
    130 a= 3.9896715213673186 b= 2.7849594123958665 c= -5.508665220597615
    131 a= 3.989671580818057 b= 2.7849594123958665 c= -5.508665220597615
    132 a= 3.9896715213673186 b= 2.7849594538949956 c= -5.508665220597615
    133 a= 3.9896715213673186 b= 2.7849594123958665 c= -5.508665138512107
    134 a= 3.249950064605349 b= 2.8714895360294554 c= -3.5091399585715157
    135 a= 3.2499501130333788 b= 2.8714895360294554 c= -3.5091399585715157
    136 a= 3.249950064605349 b= 2.8714895788179837 c= -3.5091399585715157
    137 a= 3.249950064605349 b= 2.8714895360294554 c= -3.5091399062812556
    138 a= 2.6985635134653867 b= 2.9580196596640085 c= -1.7482374733457104
    139 a= 2.6985635536771166 b= 2.9580196596640085 c= -1.7482374733457104
    140 a= 2.6985635134653867 b= 2.9580197037419365 c= -1.7482374733457104
    141 a= 2.6985635134653867 b= 2.9580196596640085 c= -1.748237447294942
    142 a= 2.493069937790426 b= 3.000282949362353 c= -0.945206652576314
    143 a= 2.493069974940063 b= 3.000282949362353 c= -0.945206652576314
    144 a= 2.493069937790426 b= 3.000282994070053 c= -0.945206652576314
    145 a= 2.493069937790426 b= 3.000282949362353 c= -0.9452066384916373
    146 a= 2.5075729202849915 b= 2.9989977790641706 c= -0.9740440872521959
    147 a= 2.5075729576507397 b= 2.9989977790641706 c= -0.9740440872521959
    148 a= 2.5075729202849915 b= 2.99899782375272 c= -0.9740440872521959
    149 a= 2.5075729202849915 b= 2.9989977790641706 c= -0.974044072737808
    150 a= 2.5074171106029874 b= 2.9990317544021594 c= -0.9734594072738433
    151 a= 2.507417147966414 b= 2.9990317544021594 c= -0.9734594072738433
    152 a= 2.5074171106029874 b= 2.999031799091215 c= -0.9734594072738433
    153 a= 2.5074171106029874 b= 2.9990317544021594 c= -0.9734593927681677
    154 a= 2.5074210685973637 b= 2.999031031902325 c= -0.9734725519528605


Try a good guess for the parameters


```python
iteration = 0
poptNL2, pcovNL2 = curve_fit(nonlinear_function, t, y,
                       absolute_sigma=True, sigma = sigmaNL, p0=(2.5,3,0))
#I think it's 2.5*t^2 with no offset
```

    0 a= 2.5 b= 3.0 c= 0.0
    1 a= 2.5 b= 3.0 c= 0.0
    2 a= 2.5 b= 3.0 c= 0.0
    3 a= 2.500000037252903 b= 3.0 c= 0.0
    4 a= 2.5 b= 3.0000000447034836 c= 0.0
    5 a= 2.5 b= 3.0 c= 1.4901161193880158e-08
    6 a= 2.507540116653946 b= 2.9990074809599334 c= -0.973917163330992
    7 a= 2.5075401540192055 b= 2.9990074809599334 c= -0.973917163330992
    8 a= 2.507540116653946 b= 2.9990075256486275 c= -0.973917163330992
    9 a= 2.507540116653946 b= 2.9990074809599334 c= -0.9739171488184953
    10 a= 2.5074184226341583 b= 2.9990315172382234 c= -0.9734643979860024
    11 a= 2.5074184599976044 b= 2.9990315172382234 c= -0.9734643979860024
    12 a= 2.5074184226341583 b= 2.9990315619272754 c= -0.9734643979860024
    13 a= 2.5074184226341583 b= 2.9990315172382234 c= -0.9734643834802524
    14 a= 2.5074209783416057 b= 2.9990310475838156 c= -0.9734720313746336


Now try an unreasonable guess for the `b` parameter


```python
iteration = 0
poptNL3, pcovNL3 = curve_fit(nonlinear_function, t, y,
                       absolute_sigma=True, sigma = sigmaNL, p0=(3,-2,0.1))
#I think it's 3/t^3 +0.1
```

    0 a= 3.0 b= -2.0 c= 0.1
    1 a= 3.0 b= -2.0 c= 0.1
    2 a= 3.0 b= -2.0 c= 0.1
    3 a= 3.0000000447034836 b= -2.0 c= 0.1
    4 a= 3.0 b= -1.9999999701976776 c= 0.1
    5 a= 3.0 b= -2.0 c= 0.10000000149011612


    <ipython-input-16-1520d182c2d1>:7: RuntimeWarning: divide by zero encountered in power
      return a*t**(b-1) + c
    /Users/lee/anaconda3/lib/python3.8/site-packages/scipy/optimize/minpack.py:828: OptimizeWarning: Covariance of the parameters could not be estimated
      warnings.warn('Covariance of the parameters could not be estimated',


It's always important to **check the fit**


```python
plt.figure(figsize=(8,6))
plt.errorbar(t,
             y,
             yerr=sigmaNL, marker='o',ls='none',label="Data")

def plot_and_print(popt,ls,label):
    plt.plot(t, nonlinear_function(t,popt[0],popt[1],popt[2]),label=label,ls=ls,lw=3)
plot_and_print(poptNL1,"-","No guess")
plot_and_print(poptNL2,"--","good guess")
plot_and_print(poptNL3,":","Bad guess")

plt.legend()
plt.xlabel("Time")
plt.ylabel("Value")
plt.figure(figsize=(8,6))



def plot_residual(data, popt,marker,label):
    plt.plot(t, nonlinear_function(t,popt[0],popt[1],popt[2],verbose=False)-data,label=label,marker=marker,ls='',lw=3)
plot_residual(y,poptNL1,"o","No guess")
plot_residual(y,poptNL2,"s","good guess")
plot_residual(y,poptNL3,"<","Bad guess")

plt.legend()
plt.setp(plt.gca(),ylabel="Residual",xlabel="Time (s)")

```

    18 a= 2.5074210685973637 b= 2.999031031902325 c= -0.9734725519528605
    19 a= 2.5074209783416057 b= 2.9990310475838156 c= -0.9734720313746336
    20 a= 3.0 b= -2.0 c= 0.1



![png](../fig/16_Curve_fit_files/16_Curve_fit_46_3.png)





![png](../fig/16_Curve_fit_files/16_Curve_fit_46_4.png)




## Keypoints
* `scipy` provides tools and functions to fit models to data.
* Use `curve_fit` to fit linear and non-linear models to experimental data
* Use appropriate errors in the `sigma` keyword to get a better estimate of parameter errors.
* **Check the fit** using a plot if possible
* Check the $\chi_r^2$ value to compare the fit against the errors in the measurements.
* Non linear models can be fitted, but may need an initial esimate of the parameters.
