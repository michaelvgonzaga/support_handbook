#!/bin/bash

TAB_LIST=$(curl -s http://localhost:9222/json)
ZENDESK_TABS=$(echo "$TAB_LIST" | jq -r '.[] | select(.url | contains("zendesk.com")) | .id')
COUNT=0
for ID in $ZENDESK_TABS; do
  if [[ $COUNT -gt 0 ]]; then
    curl -s "http://localhost:9222/json/close/$ID"
  fi
  COUNT=$((COUNT+1))
done