---
title: "Running and Quitting"
teaching: 10
exercises: 0
questions:
- "How can I run Python programs?"
objectives:
- "Launch the Jupyter Notebook, create new notebooks, and exit the Notebook."
- "Create Markdown cells in a notebook."
- "Create and run Python cells in a notebook."
keypoints:
- "Python programs are plain text files."
- "Use the Jupyter Notebook for editing and running Python."
- "The Notebook has Command and Edit modes."
- "Use the keyboard and mouse to select and edit cells."
- "The Notebook will turn Markdown into pretty-printed documentation."
- "Markdown does most of what HTML does."
---
## Python programs are plain text files.

*   They have the `.py` extension to let everyone (including the operating system) 
    know it is a Python program.
    *   This is convention, not a requirement.
*   It's common to write them using a text editor but we are going to use
    the Jupyter Notebook to present the tutorials.
*   The bit of extra setup is well worth it because the Notebook provides code completion 
    and other helpful features.
*   Notebook files have the extension `.ipynb` to distinguish them from plain-text Python programs.
    *   Can export as "pure Python" to run from the command line.

## Use the Jupyter Notebook for editing and running Python.

*   The Anaconda package manager is an automated way to install the Jupyter notebook.
    *   See [the setup instructions]({{ page.root }}/setup/) for Anaconda installation instructions.
*   It also installs all the extra libraries it needs to run.
*   Once you have installed Python and the Jupyter Notebook requirements, open a shell and type:

    ~~~
    $ jupyter notebook
    ~~~

*   This will start a Jupyter Notebook server and open your default web browser. 
*   The server runs locally on your machine only and does not use an internet connection.
*   The server sends messages to your browser.
*   The server does the work and the web browser renders the notebook.
*   You can type code into the browser and see the result when the web page talks to the server.
*   This has several advantages:
    *   You can easily type, edit, and copy and paste blocks of code.
    *   Tab complete allows you to easily access the names of things you are using
        and learn more about them.
    *   It allows you to annotate your code with links, different sized text, bullets, etc.
        to make it more accessible to you and your collaborators.
    *   It allows you to display figures next to the code that produces them
        to tell a complete story of the analysis.

## Spyder
You can also use a Python Integrated Development Environment
![Example Spyder](../fig/spyder.png)  

## PyCharm
You can also use a Python Integrated Development Environment
![PyCharm](../fig/pycharm.png)  

## Jupyter notebook
![Example Jupyter Notebook](../fig/jupyter.png)  


## Math with numbers
* Addition

~~~
2+3
~~~
{: .language-python}
~~~
5
~~~
{: .output}

* Multiplication

~~~
2*2
~~~
{: .language-python}
~~~
4
~~~
{: .output}

* More complex

~~~
9.81*10.2**2/2
~~~
{: .language-python}
~~~
510.3162
~~~
{: .output}

* Power

~~~
3 ** 2
~~~
{: .language-python}
~~~
9
~~~
{: .output}


## Math with strings (?)

* Concatenation

~~~
"cat " + "dog"
~~~
{: .language-python}
~~~
'cat dog'
~~~
{: .output}

* repetition

~~~
"cat "*3 + "dog"
~~~
{: .language-python}
~~~
'cat cat cat dog'
~~~
{: .output}

* subtraction

~~~
"cat " - "dog"
~~~
{: .language-python}
~~~
...
TypeError: unsupported operand type(s) for -: 'str' and 'str'
~~~
{: .error}


## Operators

* Addition

~~~
6 + 7
~~~
{: .language-python}
~~~
13
~~~
{: .output}

* Multiplication

~~~
6 * 7
~~~
{: .language-python}
~~~
42
~~~
{: .output}

* Division

~~~
6 / 7 
~~~
{: .language-python}
~~~
0.8571428571428571
~~~
{: .output}

* Power

~~~
6 ** 7 # power
~~~
{: .language-python}
~~~
279936
~~~
{: .output}

* Modulo

~~~
66 % 7  # Modulo (remainder)
~~~
{: .language-python}
~~~
3
~~~
{: .output}

## Logic

* Less than

~~~
6 < 7
~~~
{: .language-python}
~~~
True
~~~
{: .output}

* less than or equal to

~~~
6 <= 7 
~~~
{: .language-python}
~~~
True
~~~
{: .output}

* equal to

~~~
6 == 7 
~~~
{: .language-python}
~~~
False
~~~
{: .output}

* greater than or equal to

~~~
6 >= 7 
~~~
{: .language-python}
~~~
False
~~~
{: .output}

* greater than

~~~
6 > 7 
~~~
{: .language-python}
~~~
False
~~~
{: .output}

* logical **and**

~~~
True and False 
~~~
{: .language-python}
~~~
False
~~~
{: .output}


* logical **or**

~~~
True or False
~~~
{: .language-python}
~~~
True
~~~
{: .output}

* logical **not**

~~~
not False
~~~
{: .language-python}
~~~
True
~~~
{: .output}
