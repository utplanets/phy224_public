---
layout: episode
title: Reading Tabular Data into arrays
permalink: /07_Loading-data
exercises: 0
keypoints: ['Use numpy.loadtxt library to load tabular data.', 'Use numpy.savetxt library to save tabular data.', 'Use delimiters to make your text file cleaner.', 'Use comments in your file to describe the contents.']
objectives: ['Import the numpy library.', 'Use numpy to load a simple CSV data set.', 'Get some basic information about a numpy array.']
questions: ['How can I read tabular data?', 'How can I save tabular data?']
teaching: 20
---


~~~
import numpy
~~~
{: .language-python}

## Read a text file of data using `numpy.loadtxt`
* Numpy provides the function loadtxt to read and parse numeric data from a text file.
* The file can be delimited with commas (a 'comma separated file'), tabs, or other common delimiters
* Numerical data can be converted to floating point data or integers
* Headers and comments can be ignored during the reading of the file.


~~~
#print out the data - only works on some computers
def display_file(filename):
    """I'm just here to print the file contents"""
    print("".join(open(filename,'r').readlines()))
~~~
{: .language-python}


~~~
display_file("data/galileo_flat.txt")
~~~
{: .language-python}

    1500 1000
    1340 828
    1328. 800   
    1172 600
    800 300


~~~
data = numpy.loadtxt('data/galileo_flat.txt')
print("data is ", data)
print("data shape is ", data.shape)
~~~
{: .language-python}

    data is  [[1500. 1000.]
     [1340.  828.]
     [1328.  800.]
     [1172.  600.]
     [ 800.  300.]]
    data shape is  (5, 2)

## Read a comma separated file of data with headers using keywords
* If you have a delimiter in your file (a comma, tab, vertical line), specify that with the `delimiter` keyword.
* If you use a comment character consistently, using the `comments` keyword.
* If you have a header you want to skip, use `skiprows`



~~~
display_file("data/galileo_flat.csv")
~~~
{: .language-python}

    # Horizontal Distance Traveled (D), Release Height Above Table (H)
    #D,H
    1500, 1000
    1340, 828
    1328., 800   
    1172, 600
    800, 300


~~~
data = numpy.loadtxt('data/galileo_flat.csv', comments="#", skiprows=2, delimiter=',')
print(data)
~~~
{: .language-python}

    [[1500. 1000.]
     [1340.  828.]
     [1328.  800.]
     [1172.  600.]
     [ 800.  300.]]

* Because the header lines are commented, I don't need `skiprows`.
* Because I used the pound sign for a comment, I don't need the `comments` keyword.


~~~
data = numpy.loadtxt('data/galileo_flat.csv', delimiter=',')
print(data)
~~~
{: .language-python}

    [[1500. 1000.]
     [1340.  828.]
     [1328.  800.]
     [1172.  600.]
     [ 800.  300.]]

## Remember your data has the shape `ROWS X COLUMNS`
*   Your data will be shaped with the rows first.
*   You can change the order with transpose



~~~
print("data shape is ",data.shape)
~~~
{: .language-python}

    data shape is  (5, 2)

## Split the data into variables using the `unpack` keyword


~~~
D,H = numpy.loadtxt('data/galileo_flat.csv', delimiter=',',unpack=True)
print(D,H)
print("D shape is ",D.shape)
print("H shape is ",H.shape)
~~~
{: .language-python}

    [1500. 1340. 1328. 1172.  800.] [1000.  828.  800.  600.  300.]
    D shape is  (5,)
    H shape is  (5,)


~~~
#equivalent code
data = numpy.loadtxt('data/galileo_flat.csv', delimiter=',')
#transpose the array to columns x rows
D,H = data.T
print(D,H)
print("D shape is ",D.shape)
print("H shape is ",H.shape)
~~~
{: .language-python}

    [1500. 1340. 1328. 1172.  800.] [1000.  828.  800.  600.  300.]
    D shape is  (5,)
    H shape is  (5,)

## Save data with `numpy.savetxt`


~~~
numpy.savetxt("data/mydata.txt", data, delimiter=',')
~~~
{: .language-python}


~~~
display_file("data/mydata.txt")
~~~
{: .language-python}

    1.500000000000000000e+03,1.000000000000000000e+03
    1.340000000000000000e+03,8.280000000000000000e+02
    1.328000000000000000e+03,8.000000000000000000e+02
    1.172000000000000000e+03,6.000000000000000000e+02
    8.000000000000000000e+02,3.000000000000000000e+02


## Control the data format with the `fmt` keyword
* The default format for the data is floating point data with many digits
* You can change the format with the `fmt` keyword


~~~
numpy.savetxt("data/mydata2.txt", data,delimiter=',', fmt='%.6g')
~~~
{: .language-python}


~~~
display_file("data/mydata2.txt")
~~~
{: .language-python}

    1500,1000
    1340,828
    1328,800
    1172,600
    800,300


## Add a header string with `header`
* Add header text to the file with the `header` keyword.
* Include column titles in the `header` keyword.


~~~
header="""Distance (D), Header(H)
header lines are automatically commented out"""

newdata = numpy.vstack([D,H]).T
numpy.savetxt("data/mydata3.txt", newdata, delimiter=',', header=header, fmt='%.6g')
!cat data/mydata3.txt
~~~
{: .language-python}

    # Distance (D), Header(H)
    # header lines are automatically commented out
    1500,1000
    1340,828
    1328,800
    1172,600
    800,300

## More complex loadtxt commands can make your data more flexible
* Using the `dtype` keyword allows fine control over the types of data you read.
* Using `dtype` allows you to 'name' your data columns and reference them with the name.


~~~
data = numpy.loadtxt('data/galileo_flat.csv', comments="#", skiprows=2, delimiter=',',\
                    dtype={'names':("Distance","Height"), 'formats':('f4','f4')})
print("data shape is ", data.shape)
print("Distance data is ", data["Distance"])
~~~
{: .language-python}

    data shape is  (5,)
    Distance data is  [1500. 1340. 1328. 1172.  800.]

* If you're going to use this level of complexity from loadtxt. There are better data oriented packages like `pandas` for working with data.
