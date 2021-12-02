---
title: "Looping Over Data Sets"
teaching: 5
exercises: 0
questions:
- "How can I process many data sets with a single command?"
objectives:
- "Be able to read and write globbing expressions that match sets of files."
- "Use glob to create lists of files."
- "Write for loops to perform operations on files given their names in a list."
keypoints:
- "Use a `for` loop to process files given a list of their names."
- "Use `glob.glob` to find sets of files whose names match a pattern."
- "Use `glob` and `for` to process batches of files."
---

## Use a `for` loop to process files given a list of their names.
* A filename is just a character string.
* And lists can contain character strings.



~~~
import numpy
for filename in ["data/galileo_flat.csv","data/galileo_ramp.csv"]:
    distance, height = numpy.loadtxt(filename, skiprows=2,\
                                     comments="#", delimiter=',', unpack=True)
    print(filename, distance.min(), height.max())
~~~
{: .language-python}

~~~
    data/galileo_flat.csv 800.0 1000.0
    data/galileo_ramp.csv 253.0 1000.0
~~~
{: .output}

## Use `glob.glob` to find sets of files whose names match a pattern.
*   In Unix, the term "globbing" means "matching a set of files with a pattern".
*   The most common patterns are:
    *   `*` meaning "match zero or more characters"
    *   `?` meaning "match exactly one character"
*   Python contains the `glob` library to provide pattern matching functionality
*   The `glob` library contains a function also called `glob` to match file patterns
*   E.g., `glob.glob('*.txt')` matches all files in the current directory
    whose names end with `.txt`.
*   Result is a (possibly empty) list of character strings.



~~~
import glob
print("all csv files in data/random directory:", glob.glob("data/random/*.csv"))
~~~
{: .language-python}
~~~
    all csv files in data/random directory: ['data/random/data.029.csv', 'data/random/data.015.csv', 'data/random/data.001.csv', 'data/random/data.000.csv', 'data/random/data.014.csv', 'data/random/data.028.csv', 'data/random/data.002.csv', '...','data/random/data.035.csv', 'data/random/data.009.csv', 'data/random/data.023.csv', 'data/random/data.037.csv', 'data/random/data.036.csv', 'data/random/data.022.csv', 'data/random/data.026.csv', 'data/random/data.032.csv', 'data/random/data.033.csv', 'data/random/data.027.csv', 'data/random/data.031.csv', 'data/random/data.025.csv', 'data/random/data.019.csv', 'data/random/data.018.csv', 'data/random/data.024.csv', 'data/random/data.030.csv']
~~~
{: .output}

~~~
print("all txt files in data/random directory:", glob.glob("data/random/*.txt"))
~~~
{: .language-python}

~~~
    all txt files in data/random directory: []
~~~
{:. output}

## Use `glob` and `for` to process batches of files.
Helps a lot if the files are named and stored systematically and consistently so that simple patterns will find the right data.



~~~
for filename in sorted(glob.glob('data/random/*.csv')):
    distance, height = numpy.loadtxt(filename, delimiter=',', unpack=True)
    print(filename, distance.mean(), height.std())
~~~
{: .language-python}

~~~
    data/random/data.000.csv 0.973455156 14.253108991004671
    data/random/data.001.csv -4.4384872 18.271604877007015
    data/random/data.002.csv -2.28566216 13.972753882460598
    ...
    data/random/data.096.csv 0.724618214 16.429186710317516
    data/random/data.097.csv 0.48894924 15.292681284065516
    data/random/data.098.csv 1.84267224 11.33741881916356
    data/random/data.099.csv -3.772237556 14.155571992376832
~~~
{: .output}
> ## Determining Matches
>
> Which of these files is *not* matched by the expression `glob.glob('data/*as*.csv')`?
>
> 1. `data/gapminder_gdp_africa.csv`
> 2. `data/gapminder_gdp_americas.csv`
> 3. `data/gapminder_gdp_asia.csv`
>
> > ## Solution
> >
> > 1 is not matched by the glob.
> {: .solution}
{: .challenge}

> ## Averaging over datasets
>
> Write a program that calculate the average value from all of the data in the files, instead of individual files
> > ## Solution
> > ~~~
> > import glob
> > import numpy as np
> > data = []
> > for filename in sorted(glob.glob('data/random/*.csv')):
> >     distance, height = numpy.loadtxt(filename, delimiter=',', unpack=True)
> >     data.append(distance)
> > print(np.mean(data))
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
