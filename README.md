# Code/Astro

[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

Course materials for the 2023 Code/Astro workshop. 

Workshop website: https://semaphorep.github.io/codeastro/

Workshop "cheatsheet" of links & information: https://github.com/semaphoreP/codeastro/blob/main/workshop_info.md

Recording of the 2022 Code/Astro workshop: https://www.youtube.com/playlist?list=PLb1880Rn0qkK7zTWcqGaXNbKZbxkpvUuH. 

## Getting Started

Before the workshop, please complete the following:

1. Follow the [installation instructions](https://github.com/semaphoreP/codeastro/blob/main/Day0/INSTALL.md) to get the necessary packages installed. 

2. Do the [diagnostic assignment](https://colab.research.google.com/drive/1ZctFSkoE0uorM13Js-Djco09ve_7LOEh?usp=sharing) to get familiarized with some Python fundamentals.


## Project Information

Throughout this week, you’ll be working with a small group of collaborators (1-4 others) on a final project, a real open-source Python package for astronomy. If you already have group partners in mind, please email us! If not, we will assign you to a group based on timezone, career level, and any personal preferences you've communicated to us. This is an opportunity to put the knowledge you’ve learned from Code/Astro intro practice. On the final day of the workshop, you’ll (optionally) have a chance to present your package to the other Code/Astro participants. 

### Project Goal: 

Develop an open-source Python package for astronomy from the ground up. Your project should:
- be maintained on GitHub
- be thoroughly documented using docstrings
- contain unit tests and end-to-end tests
- be pip installable and runnable on other computers
- be a tool with an API (i.e. not a single script or notebook). We should be able to import  your package and call it.

Each of these goals will be covered on a different day of the workshop, so it’s completely fine if you don’t know how to do each of these right now. 

### Timeline & Time Expectations:

You should aim to spend 10 hours (2.5 hours per day) working on the project. Days 1 and 2 are the main time to develop the core functionality of your package. Writing docs/tests/packaging will keep you busy on Days 3 and 4.

Here’s a more detailed suggested timeline:

**Day 1**: decide on the purpose of the package. Write one central function or class. 
Example: we’re working on a package that plots the most likely galactic orbits for a user-specified subset of the Gaia catalog. Today, me and partner 1 will write a function that uses galpy to compute and plot orbits for a list of stars, and partners 2 and 3 will write a class for constructing the list of stars using user input.

**Day 2**: get comfortable using GitHub to collaborate on your package.
 Example: today we’ll put our code on GitHub and begin using branches to make further changes. We’ll continue working on the core functionality we sketched out yesterday (perhaps today we’ll add code to query the Gaia database using our list).
 
**Day 3**: document your code and put it on pypi to make it pip installable.
Example: we’ll write docstrings for each of our classes and functions, and put the code on pypi. We’ll try pip installing it on each of our machines to work through installation problems.

**Day 4**: add tests, and get ready to present tomorrow!
Example: We’ll write unit tests that evaluate the performance of individual functions (e.g. if a user sets a degree range keyword, does the Gaia query work appropriately?), and end-to-end tests that make sure the whole package is working. We’ll also add a tutorial.

### Examples from Past Years:

https://github.com/sonithls/GaiaCurves

https://github.com/JulienNGirard/SEDition

https://github.com/Bhavesh012/TCalc

https://github.com/laldoroty/snlcpy

### Final Presentation:
During the final presentation, you will have the opportunity to give a short (5 minute) demonstration of the package your developed. Remember to talk about the motivation behind the package, any challenges or difficulties you encountered, and show off what the package does!

### Advice for Pair Programming:
To do this project, you’ll be working with others to program. This is likely a new experience for most of you. We suggest you use “pair programming” to collaborate, especially towards the beginning of the week:
* Pair programming
  * One person is the “driver” who types code
  * One person is the “navigator” who watches what gets typed and offers directions
  * The driver thinks more about having the right syntax, while the navigator thinks more big picture about how this code should work or function
  * Switch back and forth constantly (e.g., every 10 minutes or after finishing a function)
  * In three person groups, two people are navigators
  * Use Discord/Zoom/Skype to share screens if working together virtually
* Code individually when there are separate tasks to be done
  * Use git branches (which we will cover on Day 2) to prevent overriding each others’ work

### Project Topics:
Many of you came to this workshop with ideas for open-source projects that are relevant to your research. If you’re in that category, please use this project as an opportunity to make something useful for your research! 

Many of you don’t have research experience, and/or did not come to this workshop with an idea. That’s completely fine too! If you’re struggling to think of an idea for a project, here’s a list of ideas to give you some inspiration:

- write an educational visualization of a physical process (e.g. check out [Show Me the Orbit](https://github.com/sblunt/orbitize/blob/main/docs/tutorials/show-me-the-orbit.ipynb))
- write something that randomly generates a joke or song lyrics given the name of a user 
- write a quadratic equation solver that prints out the steps for solving by hand
- write a image processing tool that does one main task (e.g., make color images from astronomical data taken at different wavelengths, a tool that automatically looks for stars in an image). 

