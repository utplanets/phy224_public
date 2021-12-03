---
layout: episode
title: Running and Quitting
permalink: /01_Running_and_Quitting
exercises: 0
keypoints: ['Python programs are plain text files.', 'Use the Jupyter Notebook for editing and running Python.', 'The Notebook has Command and Edit modes.', 'Use the keyboard and mouse to select and edit cells.', 'The Notebook will turn Markdown into pretty-printed documentation.', 'Markdown does most of what HTML does.']
objectives: ['Launch the Jupyter Notebook, create new notebooks, and exit the Notebook.', 'Create Markdown cells in a notebook.', 'Create and run Python cells in a notebook.']
questions: ['How can I run Python programs?']
teaching: 10
---

## Python programs are plain text files
* They have .py extension by convention, but they are plain text.
* It's common to write them in a text editor or Python "Integrated Development Environment"

## Spyder
![Spyder](../fig/spyder.png)

## PyCharm
![PyCharm](../fig/pycharm.png)

## Jupyter notebook
![Jupyter](../fig/jupyter.png)

For the tutorial's we'll use the Jupyter notebook to make presentation easier. Notebook files have the `.ipynb` but can be exported as `.py` files and printed as `.pdf` files.

## Math with numbers

Addition


~~~
2+3
~~~
{: .language-python}




~~~
5
~~~
{: .output}



Multiplication


~~~
2*2
~~~
{: .language-python}




~~~
4
~~~
{: .output}



combined


~~~
9.81*10.2**2/2
~~~
{: .language-python}




~~~
510.3162
~~~
{: .output}



power


~~~
3 ** 2
~~~
{: .language-python}




~~~
9
~~~
{: .output}



## Math with strings (?)

concatentation


~~~
"cat " + "dog"
~~~
{: .language-python}




~~~
'cat dog'
~~~
{: .output}



repetition


~~~
"cat "*3 + "dog"
~~~
{: .language-python}




~~~
'cat cat cat dog'
~~~
{: .output}



subtraction


~~~
"cat " - "dog"
~~~
{: .language-python}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-0ba50ec5c4d5> in <module>
    ----> 1 "cat " - "dog"
    

    TypeError: unsupported operand type(s) for -: 'str' and 'str'


## Operators

Addition


~~~
6 + 7
~~~
{: .language-python}




~~~
13
~~~
{: .output}



Multiplication


~~~
6 * 7 
~~~
{: .language-python}




~~~
42
~~~
{: .output}



Division


~~~
6 / 7
~~~
{: .language-python}




~~~
0.8571428571428571
~~~
{: .output}



Power


~~~
6 ** 7
~~~
{: .language-python}




~~~
279936
~~~
{: .output}



Modulo


~~~
66 % 7
~~~
{: .language-python}




~~~
3
~~~
{: .output}



## Logic

Less than


~~~
6 < 7
~~~
{: .language-python}




~~~
True
~~~
{: .output}



Less than or equal to


~~~
6 <= 7
~~~
{: .language-python}




~~~
True
~~~
{: .output}



Equal to


~~~
6 == 7
~~~
{: .language-python}




~~~
False
~~~
{: .output}



Greater than or equal to


~~~
6 >= 7
~~~
{: .language-python}




~~~
False
~~~
{: .output}



Greater than


~~~
6 > 7
~~~
{: .language-python}




~~~
False
~~~
{: .output}



logical **and**


~~~
True and False
~~~
{: .language-python}




~~~
False
~~~
{: .output}



logical **or**


~~~
True or False
~~~
{: .language-python}




~~~
True
~~~
{: .output}



logical **not**


~~~
not False # logical not
~~~
{: .language-python}




~~~
True
~~~
{: .output}


