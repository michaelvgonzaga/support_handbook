
## purge binlogs
```markdown
btool purge_binlogs -b ${BINDING_ID} --hours 0.01
```

## btool su - super user
```markdown
btool su
```

## find top 10 largest files in directory
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10