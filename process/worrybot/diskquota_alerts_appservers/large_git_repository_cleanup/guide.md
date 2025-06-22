Overview:
git reset failed due to .git/index.lock → caused by a stuck git add.
Killing the process and deleting the lock allowed cleanup to proceed.

What to Do (Commands):
- Go to Git repo: 
cd /code
- Check Git health: 
git fsck
- Expire old reflogs: 
git reflog expire --expire=now --all
- Reset Git index:
git reset

- If error: index.lock exists, find & kill stuck process:
ps aux | grep git
kill -9 <PID>     # replace <PID> with actual process ID
rm -f .git/index.lock

- Run Git cleanup:
git gc --aggressive --prune=now

- Check Git size:
du -sh .git


- Clean Up Large Backups:
    - Go to backup folders:
      cd /code/wp-content

- Delete large backup files:
    - rm ai1wm-backups/*.wpress
    - rm updraft/*.zip

- Verify free space:
    - btool show-quota

