#!/bin/bash
while IFS= read -r line; do
    echo "$line" | tr ' ' '\n' | awk '!seen[$0]++' | tr '\n' ' '
    echo
done < "$1"
