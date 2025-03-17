# Create ygg alias

###### Step 1 add in .zhrc profile:
USERNAME=“`ssh -G yggdrasil.us-central1.panth.io | grep ‘user ’ | awk -F’ ' ‘{ print $2 }’ | xargs`”
alias yggme=“ssh $USERNAME@`dig +short yggdrasil.us-central1.panth.io | tail -1`”

###### Step 2 refresh .zhrc:
source ~/.zshrc
