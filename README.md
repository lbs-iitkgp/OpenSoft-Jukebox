# OpenSoft-Jukebox

## Repository for practice sessions with LBS OpenSoft team

## Steps to follow:
### 1. Fork it :fork_and_knife:

You can get your own fork/copy of [OpenSoft-Jukebox](https://github.com/lbs-iitkgp/OpenSoft-Jukebox) by using the <a href=""><kbd><b>Fork</b></kbd></a> button in the top right corner.

 [![Fork Button](https://help.github.com/assets/images/help/repository/fork_button.jpg)](https://github.com/lbs-iitkgp/OpenSoft-Jukebox)

### 2. Clone it :busts_in_silhouette:

You need to clone (download) it to local machine using

```sh
$ git clone https://github.com/Your_Username/OpenSoft-Jukebox.git
```

> This makes a local copy of repository in your machine.

Once you have cloned the `OpenSoft-Jukebox` repository in Github, move to that folder first using change directory command on linux and Mac.

```sh
# This will change directory to a folder OpenSoft-Jukebox
$ cd OpenSoft-Jukebox
```

Move to this folder for all other commands.

### 3. Set it up :arrow_up:

Run the following commands to see that *your local copy* has a reference to *your forked remote repository* in Github :octocat:

```sh
$ git remote -v
origin  https://github.com/Your_Username/OpenSoft-Jukebox.git (fetch)
origin  https://github.com/Your_Username/OpenSoft-Jukebox.git (push)
```

Now, lets add a reference to the original [OpenSoft-Jukebox](https://github.com/lbs-iitkgp/OpenSoft-Jukebox) repository using

```sh
$ git remote add upstream https://github.com/lbs-iitkgp/OpenSoft-Jukebox.git
```

> This adds a new remote named ***upstream***.

See the changes using

```sh
$ git remote -v
origin    https://github.com/Your_Username/OpenSoft-Jukebox.git (fetch)
origin    https://github.com/Your_Username/OpenSoft-Jukebox.git (push)
upstream  https://github.com/lbs-iitkgp/OpenSoft-Jukebox.git (fetch)
upstream  https://github.com/lbs-iitkgp/OpenSoft-Jukebox.git (push)
```

### 4. Sync it :recycle:

Always keep your local copy of repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `master` branch
$ git checkout master

# Reset local `master` branch to match `upstream` repository's `master` branch
$ git reset --hard upstream/master

# Push changes to your forked `OpenSoft_Jukebox` repo
$ git push origin master
```

### 5. Ready Steady Go... :turtle: :rabbit2:

Once you have completed these steps, you are ready to start contributing by adding your work or by checking the repo's `Help Wanted` Issues, and creating [pull requests](https://github.com/lbs-iitkgp/OpenSoft-Jukebox/pulls).

### 6. Create a new branch :bangbang:

Whenever you are going to make contribution. Please create seperate branch using command and keep your `master` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name-Your_Username
$ git checkout -b Folder_Name-Your_Username
```

Create a seperate branch for contibution and try to use same name of branch as of folder concatenated with an underscore and your username.

In each of these folders (ie. tasks), add your contribution by creating a new folder with your 'username' as the title, and add your work there.

Try to keep a separate branch for each of your tasks. (Reasons will be obvious when you start adding commits)


To switch to desired branch

```sh
# To switch from one folder to other
$ git checkout Folder_Name-Your_Username
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name-Your_Username
$ git add .
```

Type in a message relevant for the code reveiwer using

```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

If you'd like to add a more detailed commit message, skip the `-m` and when you press enter, a text editor will open where you can add your commit message. Follow [this tutorial](https://github.com/erlang/otp/wiki/Writing-good-commit-messages) for some guidance on writing good commit messages.

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin Folder_Name-Your_Username
```

Finally, go to your repository in browser and click on `compare and pull requests`.
Then add a title and description to your pull request that explains your precious effort.

## Need help?
Feel free to ping us anytime!
###on [Facebook](https://www.facebook.com/naresh.ramesh) or on [Slack](https://metakgp.slack.com/) (Username: ghostwriternr).

**Naresh**

| [Facebook](https://www.facebook.com/naresh.ramesh) | [Slack (@ghostwriternr)](https://metakgp.slack.com/)
| --- | --- |

**Athitya Kumar**

| [Facebook](https://www.facebook.com/athitya.kumar) | [Slack (@athityakumar)](https://metakgp.slack.com/)
| --- | --- |

Cheers!! :smile: