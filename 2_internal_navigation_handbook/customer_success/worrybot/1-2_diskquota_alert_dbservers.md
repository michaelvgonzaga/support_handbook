# DISK QUOTA ALERT

## grant super user access
```MARKDOWN
btool su
```

## purge binlogs
```MARKDOWN
ssh dbserver-c0b21144.panth.io -p 2225  -t 'cd /srv/bindings/9e0451151c724350b57ed5620a674d79/;btool info -b 9e0451151c724350b57ed5620a674d79; bash --login'
```

## top 10 large files
```MARKDOWN
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10
```
## truncate table
```MARKDOWN
TRUNCATE TABLE table_name;
```