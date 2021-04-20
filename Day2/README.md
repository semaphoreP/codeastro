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
  * Mechanics of Git: [.PDF](https://drive.google.com/file/d/14S8w6b26JXjcFGa1aAFquq3Fh5iAa3-b/view?usp=sharing), [.PPTX](https://drive.google.com/file/d/1WE0eB4c1qb7N_aerenr4bboiNjvY7QT2/view?usp=sharing)
    * 1 person should be the facilitator: keep track of time, stay on track, and keep track of progress
    * 1 person should be the recorder: writes down the solution (suggestion: use powerpoint, keynote, or google slides to draw out the git commit tree)
  * Fix this orbitize! bug: https://github.com/sblunt/orbitize/issues/230

## Debug orbitize!

The issue you are tasked with investigating is this one: https://github.com/sblunt/orbitize/issues/230. To do so, download a development version of orbitize! for the debugging activity. 

    git clone https://github.com/sblunt/orbitize.git

Next, we'll want to override your system's default orbitize installation with this one. Install orbitize from source by `cd`-ing into this repo you just cloned (there should be a requirements.txt file) and running:

    pip install -r requirements.txt -e .

That command just ran pip to install the package in the current directory, and to automatically update when you make changes to the code (useful for developing on packages).

### Goal

  * Identify which of the nine inputs is causing the function to return NaN
  * (Optional) Modify the code to prevent this from happening in the future

## Debugging Principles

There is no one recipe for debugging. However, here are some general tips for debugging that you might find useful

  * If you have no idea what is broken, establish what is working and try to use process of elimination.
  * A good process of elimination method is binary search: see if it is the first half of the code that is breaking things, or the second half. If it's the first half, then check the first quarter vs the second quarter. Keep repeating and isolating the error this way.
  * Google error messages, especially if they are specific, to see if anyone else has hints or leads. However, do think about what commands they are suggesting you type, and don't blindly type them!
  * Learn to use interactive debuggers like the one in VS Code, which allows you to step through code line by line and stop at places of intereset. It is really useful when you have a lot of lines of code to sift through.  
  * Write tests for your function as you are writing the function so you can use them to debug your code (this is called test-driven development). It will also help clarify to yourself what exactly each function should do. 
  * Keep at it! You will develop an intuition for debugging as you do more of it. 
