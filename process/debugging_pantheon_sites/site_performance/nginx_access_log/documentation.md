# NGINX access logs
Purpose: Analyze request patterns, response times, and heavy resource usage:
cat nginx-access.log | awk '{print $1, $4, $5, $7, $9, $10}' | sort | uniq -c | sort -nr | head -50

###### Key Metrics to Look For:
- High request counts for specific URLs.
- High response times (e.g., 200 5.0 means a 5-second response).
- Redirect loops (check excessive 301 or 302 responses).
- Large request payloads (POST requests with high bytes).