# Introduction to Git: Demo
This demo will go through how to make a git repository via github,
including how to add and edit files to the repo and resolve conflicts.

For this demo, you will need 3 applications running: a web-browser
with the Github webpage (where you have logged into your account), 
a terminal window, and then your favorite text editor. 

## Make a Git Repo via Github and Clone it to Your Machine

1. After logging into github, click the `Repositories` tab at the top
   of the page and then click the `New` green button to the upper right.

2. Assign your new repo anything you wish, and then configure
   some of the basic settings. For this demo, we'll set the code to be
   public (the default selection) and then click the box to `Add a
   README file`. When complete, click the green `Create Repository`
   button to the bottom right of the page.
   
   This process creates the repo on github and assigns it a web address.
   
3. Now that the github repo is created, we need to copy a version of
   it to our local machine. This process is called "cloning". To clone
   the repo, click the green `Code` button, and copy the HTTPS address
   for the repo. 
   
   Then, in your terminal window, navigate to whereever
   you'd like the repo to live on your local machine and type:
   
```
git clone <HTTPS_address_for_repo>
```

This will create a new directory on your local machine with the same
name as the repo. 

4. To make sure everything worked properly, `cd` into the newly
   created directory on your machine and type:
   
```
git status
```
   
This should tell us that (1) we are in a git repository on the `main`
branch and (2) our branch is up-to-date with `main` (more on that
later):


## Adding and Editing Files in Your Repo 

4. Now, let's make a new text file to add to the repo directory on
   your machine. For this demo, we'll make a file called `hello.txt`
   and add some text to it. The next step is to tell git that this new
   file should be added to the git repo, which is done by:

```
git add hello.txt
```

Note that at this point, this file only exists on your local machine,
and doesn't yet exist in the github repo page. Next we need to
"commit" the change, and add a short message as to what the change we
are making is:

```
git commit hello.txt -m 'First commit of file'
```

5. Next we are ready to "push" this change to the github repo. This is
   done by:
   
```
git push origin main
```

In this command, `origin` is shorthand for the URL for the remote
repository (the one on Github), while `main` is the name of the branch
we want to push the changes to. In the future, there may be cases
where you want to push the changes to a different branch other than
`main`, in which case we would change this command, but we'll talk
about that in a future demo.

Now, go to your refresh the github webpage for your repo. You should
see that `hello.txt` now appears. 

