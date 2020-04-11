### Create a new issue

Make suggestions, request features and report bugs at https://github.com/tompc35/ooidata/issues

### Make a pull request

To contribute code, follow the [fork-and-branch Git workflow](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/). The steps are outlined below. The [setup](#setup) steps (1-4) only have to be done once. The steps for [making changes](#making-changes) (5-10) should be done for each new feature or enhancement that you add to the project.

#### Setup

##### 1. Fork the repository

Fork the repository by clicking this button on the upper right hand corner:

<img src="https://upload.wikimedia.org/wikipedia/commons/3/38/GitHub_Fork_Button.png"
       alt="fork_button"
       style="float: left; width:100px" />
</br>

##### 2. Make a local clone

On the command line, clone the repository. To find the correct link, go to your cloned repository and click this button in the upper right hand corner:

<img src="https://www.vexwiki.org/_media/programming/version_control/gitclone.png"
       alt="clone_button"
       style="float: left; width:140px" />
</br>

Use `git clone` on the command line, using the link to your forked repository. For example:

```
git clone https://github.com/your-username/ooidata.git
```

##### 3. Install the package

Use pip to install the package. The `-e` option installs in developer mode so that you do not have to reinstall every time you want to make a change to the package (although you do still have to restart the kernel).

```
cd ooidata
pip install -e .
```

##### 4. Add a remote

Add a new git remote pointing back to the original repository (not your forked repository).

```
git remote add upstream https://github.com/tompc35/ooidata.git
```

Now you have two remotes:
* `origin` points to your forked repository
* `upstream` points to the original repository

#### Making changes

##### 5. Keeping your fork in sync

Before making new changes, it is a good idea to make sure that your fork is in sync with the original repository:

```
git pull upstream master
git push origin master
```

##### 6. Create a new branch

Create a new branch to make your changes. Limit each branch to one new feature or enhancement. This will simplify the review and merge process later.

```
git checkout -b new-branch-name
```

Replace `new-branch-name` with a name that describes the new feature or enhancement that you are working on in the branch.

##### 7. Make your changes

As you make changes to the project, use `git add` to add changes to the staging area and use `git commit` to commit your changes. This process only tracks the changes on your local machine.

As an example, to add all new and edited files in the project to the staging area and commit the changes:
```
git add .
git commit -m "add commit message here"
```

Replace the message in quotes with a descriptive message about the changes that have been made. Repeat the edit-add-commit process as necessary.

Avoid adding unnecessary files to the repository. The `.gitignore` file contains a list of files and extensions that are ignored by Git in this project.

##### 8. Push your changes to Github

Push the changes that you have made locally to your forked Github repository:

```
git push origin new-branch-name
```

Replace `new-branch-name` with the name of your branch that you created in step 6.

##### 9. Open a pull request

Visit the page for your forked repository on Github. You will be prompted to [create a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).

The code will be reviewed and you may be asked to make some changes before the pull request is merged.

##### 10. Clean up after merged pull request

Once your changes have been reviewed and merged, you can update the master branch of your local repository:

```
git pull upstream master
```

Now you can delete the new branch where you made the edits (replace `new-branch-name` with the branch name you created in step 6):

```
git branch -d new-branch-name
```
Update the master branch of your forked repository:
```
git push origin master
```

Deletion of the new branch on your forked GitHub repository (replace `new-branch-name` with the branch name you created in step 6):
```
git push --delete origin new-branch-name
```
