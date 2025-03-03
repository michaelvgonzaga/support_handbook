# Identify specific PHP scripts taking too long.
Reduce database query execution times. Optimize loops and large array processing:
cat /var/log/mysql-slow.log | tail -50


###### Common issues:
- SELECT * FROM large_table WHERE column=... (add indexes).
- ORDER BY RAND() (replace with indexed sorting).
- JOIN queries taking >1s (optimize indexes).