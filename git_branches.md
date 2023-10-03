# Small helper on managing branches on git

showing all branches: ___git branch [-v]___

creating a new branch based on the one that is currently checked out: ___git branch <branch-name>___

creating a new branch based on a specific revision: ___git branch <branch-name> <revision-name>___

switch to other branch: ___git checkout <branch-name>___
another way: ___git switch <branch-name>___

renaming the current HEAD branch: ___git branch -m <new-name>___
renaming any branch: ___git branch -m <old-name> <new-name>___

renaming a remote branch:
   first, delete the old one: ___git push origin --delete <old-name>___
   then, push the new one: ___git push -u origin <new-name>___

publishing a branch: ___git push -u origin <local-branch-name>___

tracking a remote branch: ___git checkout --track origin/<remote-name>___
this allows us to easily use __git pull__ and __git push__

deleting a branch: ___git branch -d <branch-name>___
deleting a remote branch: ___git push origin --delete <branch-name>___

merging branches:
   choose the branch that should receive the changes: ___git switch main___
   make merge: ___git merge <branch-name>___
   or: ___git rebase <branch-name>___

comparing branches: ___git log <branch-name1> <branch-name2>___

