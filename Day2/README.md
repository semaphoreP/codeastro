# Day 2

## Project Goals

  * Set up a Github repository for your project. Start creating modules and classes that you need. 
  * Write at least 1 or 2 functions for tomorrow (we'll need it for an activity).
  * The next two days will have a lot of scaffolding work for your code packages. Today is a good time to make progress on code functionality!

## Learning Objectives

  * Be able to use git and follow the git flow process to contribute version-controlled code
  * Interactively debug code using breakpoints, and not rely on print statements

## Useful Links

  * [Day 2 Slides](https://docs.google.com/presentation/d/1HTWKeYw1iwI9AGh52uDatMo6T1wWUGbTmkhaJ_tyT5U/edit?usp=sharing)
  * [Mechanics of Git (.pptx)](https://drive.google.com/file/d/1WE0eB4c1qb7N_aerenr4bboiNjvY7QT2/view?usp=sharing)
  * Fix this orbitize! bug: https://github.com/sblunt/orbitize/issues/171

## Debug orbitize!

Download a development version of orbitize! to fix the above issue. Since you do not have direct write access to the orbitize! Github repo, fork the repo, make your changes there, and submit a pull request to fix the issue. To fork the repo, click on the Fork button on the [orbitize! repo page](https://github.com/sblunt/orbitize).

![alt text](imgs/fork.png)

This will fork orbitize to a Github repo owned by you (Github will remember it is a forked repo). Clone this forked repository (replace `username` with your Github username):

    git clone https://github.com/username/orbitize.git

Next, we'll want to override your system's default orbitize installation with this one. Install orbitize from source by `cd`-ing into this repo you just cloned (there should be a requirements.txt file) and running:

    pip install -r requirements.txt -e .

That command just ran pip to install the package in the current directory, and to automatically update when you make changes to the code (useful for developing on packages). 

Next, check out the `broken_orbitize` branch and fix the bug! To help you get started, we are providing the bug reproduction script from [the issue](https://github.com/sblunt/orbitize/issues/171) in this folder. If you run `broken_orbitize.py`, the code should crash.

After you fix and push the bug fix to your forked orbitize!, go back to the original [orbitize! repo page](https://github.com/sblunt/orbitize) and submit a pull request. The pull request should be requesting to pull your forked repo's `broken_orbitize` branch to the original `broken_orbitize` branch. And you've fixed the bug, and submitted a PR to incorporate your fixes into a public python repository. 
