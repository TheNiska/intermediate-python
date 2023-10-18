# Git Commands

- __git restore --stage filename.txt__ -- a command to unstage added to commit files. After this command, _filename.txt_ will be untracked as if command _add_ never was used.  
- __git pull__ -- updates our local content. It's a good practice to do _git pull_ before pushing. Usually, it's used in such order:
    1. Creating a new branch locally.
    2. Switching to this branch and making some changes.
    3. Commiting and pushing this branch to origin.
    4. Making a pull request.
    5. If our request is accepted, we can checkout the main branch and pull changes with _git pull_.  

- __git remote -v__ -- shows origins of this repository.  
- __git remote add origin 'remore-repo-address'__ -- adding origin. Usually for a new repo created locally.  
- 

# Git workflow
1. Modified
2. Staged
3. Commited

