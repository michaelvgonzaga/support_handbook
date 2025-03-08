# Diskquota alert

###### super user:
btool su

###### find top 10 largest files in directory:
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10

###### remove file 
rm -rf file_name