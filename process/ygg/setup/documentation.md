# Add Ygg to .zshrc and Test Access
1. Open Terminal:
 - Press [command] + [spacebar], type Terminal, and hit Enter.

2. Navigate to Home Directory
 - cd ~
 - pwd  # Ensure output is /Users/YourMacbookUsername

3. Check for .zshrc File
 - ls -a  # Look for .zshrc, create one if missing

4. Add Ygg Access Snippet
 - Open .zshrc in a text editor and add:
   - USERNAME="`ssh -G yggdrasil.us-central1.panth.io | grep 'user ' | awk -F' ' '{ print $2 }' | xargs`"
   - alias yggme="ssh $USERNAME@`dig +short yggdrasil.us-central1.panth.io | tail -1`"

5. Save and close.
6. Test Ygg Access
 - yggme
 - If prompted, confirm the connection by typing yes.
 - Successful access confirms setup.