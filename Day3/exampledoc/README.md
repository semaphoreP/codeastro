# Sphinx quickstart guide

1. Make sure that sphinx is installed.
```
$ pip install sphinx
```

1. Since we will be using the Napolean style of docstrings we need to install the `sphinx-napolean` package as well (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/). Lets also install the ReadTheDocs theme so that our documentation page looks nice when created.
```
$ pip install sphinxcontrib-napolean sphinx-rtd-theme
```

1. Now we are ready to initialize the documentation. Start by making a `docs` directory in your repo. Then run `sphinx-quickstart`
```
$ mkdir docs
$ sphinx-quickstart
```
Answer the questions when prompted on the terminal. You can answer `n` to the question: `Separate source and build directories?`.

This should create several files and directories in your current working directory, including `conf.py`.
```
$ ls
Makefile   _build     _static    _templates conf.py    index.rst  make.bat
```

1. Open `conf.py` in VScode or other editor. We'll need to uncomment the following lines in the "Path setup" section.
```
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
```

1. Change the `os.path.abspath('.')` part to point to the top level of your repo. In this example that would be `..`.
```
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
```



