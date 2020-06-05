# Installation

If you are using a Windows machine, first check out the setup instructions 
[here](https://github.com/semaphoreP/codeastro/blob/master/Day0/INSTALL_WINDOWS.md). If you are using a Mac, first check out the instructions at the bottom of this page. Once you've
followed those instructions, come back and continue here.

We'll use miniconda to install Python and necessary packages. You can download and install
miniconda [here](https://docs.conda.io/en/latest/miniconda.html).

You'll likely need to restart your terminal window for the new miniconda Python installation to become your defualt one. To verify your installation, run the following line, which will list the path to your python installation, and check it is pointing to your miniconda install:

    which python

Once you've installed miniconda, install the Python packages listed in our 
[requirements.txt](https://github.com/semaphoreP/codeastro/blob/master/requirements.txt) file.
If you clone this repository onto your local machine, you can do this using the command:

    pip install -r requirements.txt

You can also install the packages one-by-one by typing, for example:

    pip install numpy

Once you've installed all of the requirements, clone the `orbitize!` repository to your machine and run the test suite to make sure everything is working properly. You can use the command sequence below to do this:

    git clone https://github.com/sblunt/orbitize.git
    cd orbitize
    py.test

You may get some warnings, but you should see 0 errors if your setup is working.

If you run into any issues, [contact us](mailto:sblunt@caltech.edu). We will hold a "virtual office hours" session for 
technical setup questions.


## Visual Studio Code

In this workshop, we are recommending you use Visual Studio Code (VS Code) to develop and test your code. 
As part of the workshop, we will cover skills such as debugging and demonstrate how to do them using VS Code, so it will be easiest to also use it and follow along.
You can download VS Code for free from its official webpage: https://code.visualstudio.com/.

There are a few plugins to install and setup to utilize its features for Python development. The instructions we give below are adapted from the official [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial). That guide is long, and not everyhting will be needed, so feel free to peruse the documentation, but do not worry if you do not understand certain parts of it (it can get quite advanced!). 

> For Windows users using WSL, install the `Remote - WSL` extension from the Marketplace so you can connect VS Code with WSL. Check the [Windows install guide](https://github.com/semaphoreP/codeastro/blob/master/Day0/INSTALL_WINDOWS.md) again for a few more details then come back here. If you cannot find where the Marketplace is to install this extension, check out the paragraph below on installing the Python installation, and adapt it for `Remote - WSL`. 

First, install the Python extension from the Marketplace. The Marketplace is the place to install all VS Code addons, and can be accessed by clicking the icon with the 4 square blocks on the lefthand bar of the application (it is the icon highlighted in white below). Then type Python in the search bar, and install the `Python` add-on that is published by Microsoft. It should be the top result, and it should look like the screenshot below, except that you should have a big green install button instead. 
![alt text](../imgs/vscode-python-install.png)

We also recommend you install the `Remote - SSH` plugin so that you can develop on machines you have connected to over ssh. Note that when you connect to a remote machine (this could be either SSH or WSL or Docker containers), it will use the remote machine's VS Code setup. Likely, you will need to install your extensions there again.

The VS Code Python add on is simply just hooks that connect your system Python installation. Next, we will configure VS Code so that it is connected with your system Python installation. This means you should have installed python already (see instructions above). Follow the instructions in the [Select a Python Interpreter](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter) section of the official VS code tutorial. Select your preferred python installation (likely the miniconda you just installed). For WSL users, do this in a VS Code running in WSL. Note that VS Code allows you to set the python version on a per user and per workspace basis, which makes it easy to develop for multiple projects that have different python versioning requirements. 

When you are done setting up a python interpreter, feel free to run the [Hello World tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-python-hello-world-source-code-file) to test that everything works and get a feel for VS Code development in Python. If you choose to do this, stop before "Configure and run the debugger" which we will cover later.

# Apple-specific Instructions

If you are using a Mac you will need to install Xcode and the associated command line utilities in order to compile code. Some Python packages include portions of C or fortran code and must be compiled to run optimally. 

First, install the Xcode application using the App Store. 

Once Xcode is finished installing open a terminal and type:
    
    xcode-select --install

Accept the user agreement and follow the onscreen prompts. 
