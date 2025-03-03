# NGINX error log
Purpose: Identify server errors, misconfigurations, and failed requests.
grep -i "error" nginx-error.log | tail -50

###### Key metrics to look for
- 502 Bad Gateway (PHP-FPM crash).
- 504 Gateway Timeout (slow backend responses).
- 403 Forbidden (permissions issue).
- 429 Too Many Requests (rate-limiting triggered).