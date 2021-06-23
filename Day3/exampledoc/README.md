![Astronomy Documentation](https://pbs.twimg.com/media/EUJmsaXUcAEfmTT?format=jpg&name=medium)

# Sphinx quickstart guide

1. Make sure that sphinx is installed.
```
$ pip install sphinx
```

2. Since we will be using the Napoleon style of docstrings we need to install the `sphinx-napoleon` package as well (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/). Lets also install the ReadTheDocs theme so that our documentation page looks nice when created.
```
$ pip install sphinxcontrib-napoleon sphinx-rtd-theme
```

3. Copy the `exampledoc` directory somewhere into your repo and `cd` into it.

4. Now we are ready to initialize the documentation. Start by making a `docs` directory in your repo. Then run `sphinx-quickstart`
```
$ mkdir docs
$ cd docs
$ sphinx-quickstart
```
Answer the questions when prompted on the terminal. You can answer `n` to the question: `Separate source and build directories?`.

This should create several files and directories in your current working directory, including `conf.py`.
```
$ ls
Makefile   _build     _static    _templates conf.py    index.rst  make.bat
```

5. Open `conf.py` in VScode or other editor. We'll need to uncomment the following lines in the "Path setup" section.
```
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```

6. Change the `os.path.abspath('.')` part to point to the top level of your repo. In this example that would be `..`.
```
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
```

7. Also change the `html_theme` variable to "sphinx_rtd_theme", add the line `master_doc='index'` below your author name. Also add “sphinx.ext.autodoc” and "sphinx.ext.napoleon" to the `extensions` list in `conf.py`.

8. Now we are ready to build the documentation pages! Do this from the `docs` directory.
```
$ make html
```

This will create a basic set of documentation pages in `_build/html`. Open up the `index.html` with your favorite browser.


9. This page doesn't have any of the documentation from your docstrings yet, so lets add that. The content of these pages are controlled by the `.rst` (reStructured text) files. Create a new `.rst` file called `correlate.rst`. The contents of this file should look like this:
```
.. _correlate:

Correlate
=========

.. automodule:: correlate
   :members:
```
This will automatically parse `correlate.py` and look for your docstrings in order to turn them into a nicely-formatted web page.

10. Run `make html` again to update the docs.

11. View your documentation by opening the file at `_build/html/index.html`.


## Activity
1. Set up sphinx documentation for your project repo.
2. Document at least one function in your package and make sure it builds in the sphinx documentation.
3. (BONUS) Trade with another group and try to use one of their functions/classes/methods that they have documented using their sphinx documentation.

