# Setup for Windows

## Windows or WSL?

One important decision to make at the start is to whether or not make Windows your development environment. Generally, python works fine on Windows, so it is perfectly viable for python alone. However, there are a number of python packages for astornomy that are not compatible with Windows. For Code/Astro, all of the packages we will work with work with Windows, but this may not be true for other packages you might encounter for your research.

The suggested alternative is to use Windows Subsystem for Linux (WSL), which is a full Linux operating system running inside of Windows. This is supported by default now on Windows 10 and it is fairly simple to setup. The additional complexity introduced by WSL is that there usually is 1-2 more steps that need to be done to hook up your programming setup to use the python installed under WSL for your development. This is generally not a large barrier, but it involves doing a few extra steps. 

For Code/Astro, we will present instructions on how to set things up for WSL and native Windows. Generally, we will recommend you using WSL for the purpose of software programming for astronomy.

## Common Applications

For either WSL or native Windows setup, we will use Visual Studio Code as our code editor. You can download it here: https://code.visualstudio.com/. Install the Windows version either way. We will provide further details on how to use this editor.

## Windows Subsystem for Linux (WSL)

WSL allows you to run a virtual Linux operating system in Windows. This is officially supported by Microsoft and lets you do anything a Linux user would do. 

### Install WSL

See the WSL installation instructions here: https://docs.microsoft.com/en-us/windows/wsl/install-win10. When you get to the step of choosing a Linux distrbution from the Microsoft store, we suggest you install Ubuntu, as it is probably the easiest to work with. If it is installed successfully, you should be open Ubuntu and have a black terminal screen appear. Anything you do inside this terminal screen will be done through Ubuntu. But as we will see, this is not the only way to run things in Linux.

### Install xming

Normally, WSL is just a command prompt, so it does not have a GUI interface. If you try to display matplotlib plots through the command line, it will not work, because WSL does not directly talk with your Windows desktop normally. However, you can make this communication happen with xming, which can be installed from here: https://sourceforge.net/projects/xming/.

After you download and install xming, click on it to run. It runs passively in the backgorund, so you should not expect anything to happen. You should just see the xming icon appear in the Windows taskbar. This means the connection is active. 

### Setup Python in Linux

Follow the Linux setup guide to install and configure python for your WSL setup.



