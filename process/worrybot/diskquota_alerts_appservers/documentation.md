# Diskquota alert
btool disable-quota -b ${BINDING_ID} --hours 0.01
btool restart -b ${BINDING_ID} --hours 0.01
btool purge_binlogs -b ${BINDING_ID} --hours 0.01
btool converge -b ${BINDING_ID} --hours 0.01
###### super user:
btool su

###### find top 10 largest files in directory:
 find . -type f \( -name "mysql-bin.*" -o -print \) -exec du -h {} + | sort -rh 2>/dev/null | head -n 10

###### remove file 
rm -rf file_name