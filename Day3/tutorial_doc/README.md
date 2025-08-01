![Astronomy Documentation](https://pbs.twimg.com/media/EUJmsaXUcAEfmTT?format=jpg&name=medium)

# Documentation
Documentation for code comes in many forms. Some includ
 * In-line comments in the code (`# makes comments in python`)
 * Docstrings: chunks of comments when a function or class is defined
 * README files: text files that come with the code
 * Documentation pages: webpages of documentation


## Jason's hot takes on documentation
 * Perfect is the enemy of good.
 * The three most important aspects of your code to document (if you document nothing else): 
    1. how to setup/install your code
        * Optimal: a series of commands I can briendly follow with copy/paste
    2. how to run the code for the most standard use case
        * Optimal: a series of commands I can briendly follow with copy/paste
        * Optimal: document expected output with units
    3. how to cite your code
 * The third most important aspect is to document your code's API (application programming interface). An API species what are the inputs to your code and what are the outputs.      
    * Docstrings are one way to document your API
 * In-line comments are the least important, but they have their place (e.g., explaining confusing parts of the code)

  

# Python Docstrings
A docstring is a string that appears in the first line of a function
or class that provides an overview of its purpose, a description of
the input variables it expects, and an explanation of the outputs
produced. There are several common styles of python
docstrings (see examples
[here](https://betterprogramming.pub/3-different-docstring-formats-for-python-d27be81e0d68)),
but today we will focus on the Google Docstring. 

Here is an example of a Google-stype docstring for a function called `cross_corr`:


<p align="center">
  <img width="800" height="211" src="./figs/docstring_f.png">
</p>


This example shows a docstring for a typical function. Docstrings for
specific cases (e.g., optional input variables, classes,
exceptions, etc) have some slight modifications to this general structure.
Example docstrings for these cases (and more!) can be found [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

In addition to providing crucial information, docstrings provide a standardized way to
document code that can be easily parsed by automated
documentation tools, like
[sphinx](https://www.sphinx-doc.org/en/master/). 

### Python Type Hinting

By default in Python, you can pass any kind of object into any argument. There is no syntax prohibiting it (although your code might crash!). However, we frequently actually know exactly what is the type of a given input or output. A small formatting technique to make your functions more easy to understand and also assist IDE/dsebugging tools is to add "Type Hinting" to your functions. The `cross_corr()` function can be type hinted when defining the function signature:

```
import numpy as np

def cross_corr(a: np.array, b: np.array) -> np.array:
```

Note that this does not change the behavior of the function. The function will not check that `a` and `b` are actually arrays that get passed in, and it will not guarantee the output will return an array (you still have to do those type checks yourself). However, it will make it easier for IDEs and debuggers to identify bugs in your code before you run it and provide hints. 

# Sphinx website quickstart guide

1. In this example, we will create a documentation website for our example package `correlate`, which is located at `Day3/tutorial_doc/` in
the codeastro repository. The correlate package as a single module (`correlate.py`) with a few functions. This demo is meant to be similar to how you would set up the doc for your project. Start by using `cd` to move into the
`tutorial_doc` directory.

2. Now we are ready to initialize the documentation. Start by making a
`docs` directory in your repo. Then run `sphinx-quickstart` within `docs`:
```
mkdir docs
cd docs
sphinx-quickstart
```
Answer the questions when prompted on the terminal. Answer `n` to the question: `Separate source and build directories?`.

This should create several files and directories in your `docs`
directory, as shown below.
```
$ ls
Makefile   _build     _static    _templates conf.py    index.rst  make.bat
```

3. Open `conf.py` in VScode or another editor. This is the configuration
file for the Sphinx documentation builder, which controls how Sphinx
processes your code.

First, we'll need to tell Sphinx where to find your python files by
defining the path. You can think of this as being
similar to the PYTHONPATH environment variable that python uses to run the
python files you create.

If your `conf.py` file has a ``Path setup'' section, then uncomment
the following lines:

```
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```

Otherwise, copy and paste these lines to the top of `conf.py` and
uncomment them. 

4. Change the argument of `os.path.abspath('.')` to point to directory where `correlate.py` and `__ini__.py` live. In this example that would be `../correlate/` (
one level up in the directory struture from `conf.py` and in a folder called `correlate`).
```
import os
import sys
sys.path.insert(0, os.path.abspath('../correlate/'))
```
This command places the code directory you wish to
document at the front of your existing path, to ensure that sphinx
searches for the python files there first. **Building the documentation is finicky and small syntax errors can lead to docs breaking. Getting the right path is one of the most finicky things.** 

5. Make several additional changes to the conf.py file:
* Add the line `root_doc = 'index'` below your author name. This
  defines the main page of your documentation to be 'index.rst" (which
  was automatically generated by `sphinx-quickstart` in step 4). The
  root page contains the
  table of contents for your package (more on that later)
* Also add "sphinx.ext.autodoc" and "sphinx.ext.napoleon" to the `extensions`
   list in `conf.py`. "spinx.ext.autodoc" gives sphinx the power to
   read your python files and automatically extract the
   docstrings. "sphinx.ext.napoleon" allows sphinx to understand
   google-style docstrings.
* Finally, change the `html_theme` variable to
  "sphinx_rtd_theme". This defines the style of the documentation
  webpages. Here, we use the ReadtheDocs format. But, many others are
  availabe (see examples [here](https://www.sphinx-doc.org/en/master/usage/theming.html))


<p align="center">
  <img width="800" height="884" src="./figs/conf_edits2.png">
</p>

6. Now we are ready to build the documentation pages! Do this from the `docs` directory.
```
make html
```

This will create a basic set of documentation pages in `_build/html`. Open up the `index.html` with your favorite browser.


7. This page doesn't have any of the documentation yet. You can write anything you want in `.rst` (reStructured text) pages to document your code. Right now, we are just goint to show one feature: automatic API documentation with sphinx. We're going to make an API page for `correlate.py`. We'll make a new `.rst` page for the API doc. In the `docs`
directory, create a new `.rst` file called `correlate.rst`. The contents of this file should look like this:
```
.. _correlation:

Correlation Functions
=====================

Function to perform correlations.

.. automodule:: correlate
   :members:
```
This will tell Sphinx automatically parse `correlate.py` and read
your docstrings in order to turn them into a nicely-formatted web
page. Here is a breakdown of what the different parts of this
   file mean:

<p align="center">
  <img width="800" height="156" src="./figs/correlate_f3.png">
</p>

8. Link the correlate page to the index page by adding ``correlate.rst``
to ``index.rst`` under the "toctree" command. This puts
``correlate.rst`` in the table-of-contents that appears in the main
page of your documentation. Remember to match indentation levels!

<p align="center">
  <img width="800" height="356" src="./figs/index_f.png">
</p>


9. Run `make html` again to update the docs.

10. View your documentation by opening the file at
`_build/html/index.html`. You should now see a link to the Correlation
Functions page, which has the documentation for `correlate.py`.

# Tips and Tricks

* Docstring / rst file formatting:
  * Remember to check out these
  [additional docstring examples](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
  to see how to handle specific cases such as optional input variables, classes, exceptions, etc.

  * .rst files offer many more text formatting options than what is
  shown in this example. Here is a nice
  [cheatsheet](https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html)
  with more options.

  * Docstrings and .rst files can be very finicky regarding syntax!
      How sphinx compiles your documentation can be sensitive to indents, skipped lines, type of punctuation used, etc.

* More details regarding some of the Sphinx commands we used:

  * `:maxdepth:`: Under the `.. toctree::` command in `index.rst`, you'll
  notice the command `:maxdepth:`. This defines the number of nested headings to
  include as links in your table-of-contents on the front page of your
  documentation. For example, `:maxdepth: = 1` means
  that only the titles of each .rst file will be included (those
  underlinded with '==='). `:maxdepth: = 2` will include these titles as well as
  the first level of subsections (those underlined with '---'). In
 the above example, we only had one title in `correlate.rst`
  ("Correlation Functions"), and so that is all that appeared. But,
  try adding a sub-section to `correlate.rst` and see what happens!

  * `:caption:`: Under the `.. toctree::` command in `index.rst`, you'll
  also notice the command `:caption: Contents:`. The `:caption:`
  command is a way you can set the title for that particular section
  in that compiled documentation. In the example above,
  we assign the title `Contents:` `.. toctree::` section. This
  command is optional and does not need to be used.

  * `.. automodule::`: In `correlate.rst`, we use the command
  `.. automodule::` followed by `:members:`to tell sphinx to document
  all functions, classes, etc (i.e. the "members") of our python
  module that have defined docstrings. However,
  you can tweak this command in many ways: for example, you can
  document a specific class, rather than an entire module
  (`.. autoclass::`), you can document
  only specific members within a given module (`:members: func1,
  func2`), include entries for
  functions that don't have docstrings (`:undoc-members:`), and more. Check out the
  [autodoc documentation](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
  for ways to can control these commands.

  * In the example above, let's say we wanted to insert a link to the
  correlation function page somwhere (say, under the "Indicies and
  tables" sections of the index page). Now that the `correlate.rst` file has been added
  under the toctree, we can refer to its label using `:ref:` command:
```
Indices and tables
==================
We can make a link to the correlation page by referring to its label
  like this :ref:`correlation`.
  
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

 ```

# Activity: Building Sphinx Documentation For Your Repository
1. Document at least one function in your package with a docstring. 
2. Set up sphinx documentation for your project repo and build the doc
page for your function(s). Make sure it builds correctly!
    * Hint: to begin, make a `docs` directory in your repo, just like
      step 2 in the example above. 


# Activity Wrap-Up: Moving Forward with Code Documentation
We've focused on the basics of how to document your code using
docstrings and how to automatically compile those docstrings into
webpages via Sphinx. This is crucial to help other users
(and yourself!) use your code in the future. As you work
on your python packages, keep in mind that it is
useful to include other information in your documentation as
well, such as:

* Installation instructions 
* Quick-start guides, tutorials, and code examples
* How users might cite/give credit to your code, as
well as a list of folks who have contributed to your code
* A change-log: how your code has evolved with different versions/releases
* How users might contribute to your code and/or report issues

If there is a software package that you often use in your own work,
take a look at its documentation. What info is included, and what do
you find most useful? Is the documentation easy to understand and
navigate? By looking at other documentation, you can get a
sense of what works and doesn't work for you as you document your own
package. For additional examples of code documentation, check out the
pages for [orbitize](https://orbitize.readthedocs.io/en/latest/index.html),
[RadVel](https://radvel.readthedocs.io/en/latest/), and
[SPISEA](https://spisea.readthedocs.io/en/latest/). 

## Bonus Activity: Linking your Sphinx Documentation with ReadTheDocs
In most cases, we want to host our sphinx documentation online so that
other users can access it easily. If your code is in a GitHub repo, is
public, 
and has sphinx documentation set up as above,
then you can host your documentation via
[ReadTheDocs](https://readthedocs.org/). One very nice aspect of
ReadTheDocs is that you can have it automatically recompile
the documentation each time a change is pushed to your code
repository. Just like that, you have documentation that updates
itself!

ReadtheDocs provides a nice
[tutorial](https://docs.readthedocs.io/en/stable/tutorial/) on how to
set it up. You will need to:

1. Make a free ReadTheDocs account and authorize it to access your
GitHub account ("Sign Up for Read the Docs")

2. Import your repository as a new ReadTheDocs project ("Import the
   Project for Read the Docs")

3. Build your documentation; make sure it runs to completion and that
the output webpage looks the way you expect it to ("Checking the First Build")

4. Set it up so that the docs are automatically recompiled if a push
is made to the github repo. In the ReadtheDocs project page,
click on the `Advanced Settings` link on the left under the `Admin`
menu, check the “Build pull requests for this project” checkbox,
and click the Save button at the bottom of the page. (From "Trigger a
Build from a pull request"). 



