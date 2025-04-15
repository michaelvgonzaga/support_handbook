# Steps 
1. Close all Chrome/Brave tabs (optional, just to start clean).

2. Open Terminal, run:

###### For Google
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
Or use this for Brave:

###### For Brave
/Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser --remote-debugging-port=9222
Install tab helper:

###### Install jq
brew install jq
Paste this to terminal to close duplicate Zendesk tabs:

###### save close-zendesk.sh file
TAB_LIST=$(curl -s http://localhost:9222/json)
ZENDESK_TABS=$(echo "$TAB_LIST" | jq -r '.[] | select(.url | contains("zendesk.com")) | .id')
COUNT=0
for ID in $ZENDESK_TABS; do
  if [[ $COUNT -gt 0 ]]; then
    curl -s "http://localhost:9222/json/close/$ID"
  fi
  COUNT=$((COUNT+1))
done

###### run in terminal
./close-zendesk.sh
