# Small helper on managing branches on git

showing all branches: ___git branch [-v]___

creating a new branch based on the one that is currently checked out: ___git branch (branch-name)___

creating a new branch based on a specific revision: ___git branch (branch-name) (revision-name)___

switch to other branch: ___git checkout (branch-name)___  
another way: ___git switch (branch-name)___

renaming the current HEAD branch: ___git branch -m (new-name)___  
renaming any branch: ___git branch -m (old-name) (new-name)___

renaming a remote branch:  
   first, delete the old one: ___git push origin --delete (old-name)___  
   then, push the new one: ___git push -u origin (new-name)___

publishing a branch: ___git push -u origin (local-branch-name)___  
this creates a new remote branch based on a local branch.  


tracking a remote branch: ___git checkout --track origin/(remote-name)___  
this allows us to easily use __git pull__ and __git push__

deleting a branch: ___git branch -d (branch-name)___  
deleting a remote branch: ___git push origin --delete (branch-name)___

merging branches:  
   choose the branch that should receive the changes: ___git switch main___  
   make merge: ___git merge (branch-name)___  
   or: ___git rebase (branch-name)___

comparing branches: ___git log (branch-name1) (branch-name2)___

# Freature branch workflow
The core idea behind the Feature Branch Workflow is that all feature development should take place in a dedicated branch instead of the main branch. This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase. It also means the main branch will never contain broken code, which is a huge advantage for continuous integration environments.  

### Usually it consists of these steps:  
1. git checkout -b new-feature
2. git add <some-file>
3. git commit -m "message"
4. git push -u origin new-feature











