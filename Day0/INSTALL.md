# Installation

If you are using a Windows machine, first check out the setup instructions 
[here](https://github.com/semaphoreP/codeastro/blob/main/Day0/INSTALL_WINDOWS.md). If you are using a Mac, first check out the instructions at the bottom of this page. Once you've
followed those instructions, come back and continue here.

At the end of the Python installation section, you will run a series of tests that will give you a secret code that indicates Python has been installed successfully! 

### Git ###
If you don't have `git` installed, [install git](https://git-scm.com/downloads). (Windows users can use the `git` installed from WSL)

Then, clone this repository to your machine. It will create a folder called codeastro. 

    git clone https://github.com/semaphoreP/codeastro.git

### Python ###
We recommend you use an Anaconda Python installation. If you don't have such an installation already, use miniconda to install Python and necessary packages. You can download and install
miniconda [here](https://docs.conda.io/en/latest/miniconda.html).

For all Python users, we strongly recommend that you use conda environments to manage multiple Python versions for multiple projects, especially if you already have python installed for other projects. This prevents projects having conflicting dependencies as each project can have its own Python. Let's create an environment for Code/Astro that uses Python 3.

    conda create -n codeastro python=3

Then, any time you want to use this version of Python from the command line, run the following line of code to set Python to point to this version:

    conda activate codeastro

 To verify your installation, run the following line, which will list the path to your python installation. The path should include miniconda/anaconda and codeastro:

    which python

Now that we have a Python environment for this workshop, let's install packages that we need. First we want to install `numpy` through conda so that it is compiled with MKL/BLAS so that we can parallelize linear algebra operations. We'll also install `jupyter` notebooks this way if they are not already installed.

    conda install numpy jupyter

We can install the rest of the Python packages listed in our 
[requirements.txt](https://github.com/semaphoreP/codeastro/blob/main/requirements.txt) file through the regular `pip` package manager.
Assuming you followed the instructions above to clone this repository, `cd` into the codeastro folder and run the command:

    pip install -r requirements.txt

You can also install the packages one-by-one by typing, for example:

    pip install matplotlib

Once you've installed all of the requirements, clone the `orbitize!` repository to your machine and run the test suite to make sure everything is working properly. You can use the command sequence below to do this:

    git clone https://github.com/sblunt/orbitize.git
    cd orbitize
    pytest --mode codeastro

You may get some warnings, but you should see 0 errors and a secret code at the end of the output. We will ask you for the secret code to check your python installation is all working. 

If you run into any issues, [contact us](mailto:sblunt@caltech.edu). We will hold a "virtual office hours" session for 
technical setup questions.


## Visual Studio Code

In this workshop, we are recommending you use Visual Studio Code (VS Code) to develop and test your code. 
As part of the workshop, we will cover skills such as debugging and demonstrate how to do them using VS Code, so it will be easiest to also use it and follow along.
You can download VS Code for free from its official webpage: https://code.visualstudio.com/.

There are a few plugins to install and setup to utilize its features for Python development. The instructions we give below are adapted from the official [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial). That guide is long, and not everything will be needed, so feel free to peruse the documentation, but do not worry if you do not understand certain parts of it (it can get quite advanced!). 

> For Windows users using WSL, install the `Remote - WSL` extension from the Marketplace so you can connect VS Code with WSL. Check the [Windows install guide](https://github.com/semaphoreP/codeastro/blob/main/Day0/INSTALL_WINDOWS.md) again for a few more details then come back here. If you cannot find where the Marketplace is to install this extension, check out the paragraph below on installing the Python installation, and adapt it for `Remote - WSL`. 

First, install the Python extension from the Marketplace. The Marketplace is the place to install all VS Code addons, and can be accessed by clicking the icon with the 4 square blocks on the lefthand bar of the application (it is the icon highlighted in white below). Then type Python in the search bar, and install the `Python` add-on that is published by Microsoft. It should be the top result, and it should look like the screenshot below, except that you should have a big green install button instead. 
![alt text](../imgs/vscode-python-install.png)

We also recommend you install the `Remote - SSH` plugin so that you can develop on machines you have connected to over ssh. Note that when you connect to a remote machine (this could be either SSH or WSL or Docker containers), it will use the remote machine's VS Code setup. Likely, you will need to install your extensions there again.

The VS Code Python add on is simply just hooks that connect your system Python installation. Next, we will configure VS Code so that it is connected with your system Python installation. This means you should have installed python already (see instructions above). Follow the instructions in the [Select a Python Interpreter](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter) section of the official VS code tutorial. Select your preferred python installation (likely the codeastro environment of the miniconda you just installed). For WSL users, do this in a VS Code running in WSL. Note that VS Code allows you to set the python version on a per user and per workspace basis, which makes it easy to develop for multiple projects that have different python versioning requirements by having a different conda environment for each project. 

When you are done setting up a python interpreter, feel free to run the [Hello World tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-python-hello-world-source-code-file) to test that everything works and get a feel for VS Code development in Python. If you choose to do this, stop before "Configure and run the debugger" which we will cover later.

# Apple-specific Instructions

If you are using a Mac you will need to install Xcode and the associated command line utilities in order to compile code. Some Python packages include portions of C or fortran code and must be compiled to run optimally. 

First, install the Xcode application using the App Store. 

Once Xcode is finished installing open a terminal and type:
    
    xcode-select --install

Accept the user agreement and follow the onscreen prompts. 
