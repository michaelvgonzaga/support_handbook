# Worrybot
As of 2025 do not pause alerts for elite site down.

# Handling down sites

###### Confluence guide
- https://getpantheon.atlassian.net/wiki/spaces/CS/pages/387973121/Tracking+Appserver+and+Monitoring+Changes
- https://getpantheon.atlassian.net/wiki/spaces/CS/pages/413041007/worrybot+Handling+downtime+alerts#Troubleshooting-downtime

###### Steps:

1. Check Logs:
- Look for PHP/FPM errors. If you see “pm.max_children,” the site is hitting server limits.

2. Elite Plan? Add App Servers:
Formula:
Max RPM ÷ 100 = App Servers Needed (rough estimate)
(Example: 400 RPM ÷ 100 = 4 app servers)

3. Use btool appserver-scale [env] --add [#]

4. Try a Converge:
Restarts services (skip if site has multiple domains).

5. Check New Relic:

6. Migrate slow or stuck app servers.

7. If MySQL is spiking, use btool kill-queries.

8. If Drupal:
Run btool drush ws to check recent site errors.

9. Many Sites Down?
Run @hubot servers me in Slack. Ping OCE if 10+ sites alert.

10. Under Attack? (AGCDN sites only):
Check traffic patterns, block abusive IPs using AGCDN tools.

11/ Still Down?
If converge/migration doesn’t fix it and it alerts again, send a proactive ticket to the customer.