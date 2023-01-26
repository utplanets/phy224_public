---
title: "Reading Tabular Data into arrays"
teaching: 20
exercises: 0
questions:
- "How can I read tabular data?"
- "How can I save tabular data?"
objectives:
- "Import the numpy library."
- "Use numpy to load a simple CSV data set."
- "Get some basic information about a numpy array."
keypoints:
- "Use numpy.loadtxt library to load tabular data."
- "Use numpy.savetxt library to save tabular data."
- "Use delimiters to make your text file cleaner."
- "Use comments in your file to describe the contents."
---

## Use the Numpy package to load data using the `loadtxt` command

* Numpy provides the function loadtxt to read and parse numeric data from a text file.
* The file can be delimited with commas (a 'comma separated file'), tabs, or other common delimiters
* Numerical data can be converted to floating point data or integers
* Headers and comments can be ignored during the reading of the file.

~~~
import numpy
data = numpy.loadtxt('data/galileo_flat.empty')
print(data)
~~~
{: .language-python}
~~~
[[1500. 1000.]
 [1340.  828.]
 [1328.  800.]
 [1172.  600.]
 [ 800.  300.]]
~~~
{: .output}


## Read a comma separated file of data with headers
* If you have a delimiter in your file (a comma, tab, vertical line), specify that with the `delimiter` keyword.
* If you use a comment character consistently, using the `comments` keyword.
* If you have a header you want to skip, use `skiprows`

~~~
data = numpy.loadtxt('data/galileo_flat.csv', comments="#", skiprows=2, delimiter=',')
print(data)
~~~
{: .language-python}
~~~
[[1500. 1000.]
 [1340.  828.]
 [1328.  800.]
 [1172.  600.]
 [ 800.  300.]]
~~~
{: .output}


## Remember your data has the shape `ROWS X COLUMNS`
* Your data will be shaped with the rows **first**.
* You can change the order with `transpose`

~~~
print("data shape is ",data.shape)
~~~
{: .language-python}
~~~
data shape is  (5, 2)
~~~
{: .output}


## Split the data into variables using `unpack`
* You can split data using the `unpack` keyword

~~~
D,H = numpy.loadtxt('data/galileo_flat.csv', comments="#", skiprows=2, delimiter=',',unpack=True)
print(D,H)
print("D shape is ",D.shape)
print("H shape is ",H.shape)
~~~
{: .language-python}
~~~
[1500. 1340. 1328. 1172.  800.] [1000.  828.  800.  600.  300.]
D shape is  (5,)
H shape is  (5,)
~~~
{: .output}

* You can split data after loading too

~~~
data = numpy.loadtxt('data/galileo_flat.csv', comments="#", skiprows=2, delimiter=',')
D,H = data.T
print(D,H)
print("D shape is ",D.shape)
print("H shape is ",H.shape)
~~~
{: .language-python}
~~~
[1500. 1340. 1328. 1172.  800.] [1000.  828.  800.  600.  300.]
D shape is  (5,)
H shape is  (5,)
~~~
{: .output}

## Save data with `numpy.savetxt`

Saving text data is made possible with the `savetxt` command. It mirrors the `loadtxt` command

~~~
numpy.savetxt("data/mydata.txt", data, delimiter=',')
~~~
{: .language-python}

    1.500000000000000000e+03,1.000000000000000000e+03
    1.340000000000000000e+03,8.280000000000000000e+02
    1.328000000000000000e+03,8.000000000000000000e+02
    1.172000000000000000e+03,6.000000000000000000e+02
    8.000000000000000000e+02,3.000000000000000000e+02


## Control the data format with the `fmt` keyword
* The default format for the data is floating point data with 16 digits
* You can change the format with the `fmt` keyword

~~~
numpy.savetxt("data/mydata2.txt", data, delimiter=',', fmt='%.6g')
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
header="Distance (D), Header(H)"
newdata = numpy.vstack([D,H]).T
numpy.savetxt("data/mydata3.txt", newdata, delimiter=', ', header=header, fmt='%.6g')
~~~
{: .language-python}

    # Distance (D), Header(H)
    1500, 1000
    1340, 828
    1328, 800
    1172, 600
    800, 300


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

~~~
data shape is  (5,)
Distance data is  [1500. 1340. 1328. 1172.  800.]
~~~
{:. output}
