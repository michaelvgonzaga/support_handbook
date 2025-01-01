## top 10 large files
```MARKDOWN
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10
```