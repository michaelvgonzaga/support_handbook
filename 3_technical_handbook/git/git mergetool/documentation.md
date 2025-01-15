# Git Merge tool
source: https://git-scm.com/docs/git-mergetool

## TLDR:
git mergetool helps you resolve merge conflicts using visual tools. After merging branches, if Git can't automatically combine changes, this command lets you open a conflict in a user-friendly editor to manually fix it.

Basic Usage:

git mergetool: Opens a tool to resolve all current merge conflicts.
git mergetool <file>: Opens the tool for a specific file with conflicts.
Common Options:

--tool=<tool>: Choose a tool (e.g., meld, vimdiff, kdiff3).
-y or --no-prompt: Runs the tool without asking for confirmation.
-g or --gui: Uses a graphical tool if configured.
--tool-help: Lists available tools.
How It Works:
It shows three versions of the file:

LOCAL: Your branch’s version.
REMOTE: The version from the branch you're merging.
BASE: The common ancestor of both versions.
MERGED: The file where you'll fix conflicts.
Important Notes:

Changes might take 15 minutes to appear due to caching.
Use the correct tool scope (like "web") for the tool to work properly.
Backups of the original conflicted files are saved as .orig files unless disabled.

In short, git mergetool makes it easier to manually solve code conflicts by opening them in a visual tool.