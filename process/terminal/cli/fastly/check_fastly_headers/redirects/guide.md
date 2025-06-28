markdown````
curl -s -L -o /dev/null -w '%{url_effective}\n' -D - https://ucrotp.ucr.edu | grep -Ei '^(HTTP|location:|x-cache|x-served-by|x-fastly-request-id)'
````
