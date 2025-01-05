# DISK QUOTA ALERT DBSERVER
last reviewed 01-05-2024

## grant super user access
```MARKDOWN
btool su
```

## purge binlogs
```MARKDOWN
btool purge_binlogs -b ${BINDING_ID} --hours 0.01
```

## top 10 large files
```MARKDOWN
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10
```
## truncate table
```MARKDOWN
TRUNCATE TABLE table_name;
```