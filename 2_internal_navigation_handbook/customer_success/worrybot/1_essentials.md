# WORRYBOT ESSENTIALS
last reviewed 01-05-2024

## Elite Site Down (Handling Alert)
- Click Health link to see if platform URL is OK
  - Double check NR and logs if platform URL is OK but multiple alerts. Provide findings to customer. 
  - Create proactive ticket as needed.
  - For Emergencies:
    - Create OCE Bug card, this will prompt primary and secondary OCE in #oncall-handoff channel. Respond and monitor emergency as needed.
    - source: https://getpantheon.atlassian.net/wiki/spaces/VULCAN/pages/1076889616/OCE+Guide+to+Escalation#Emergencies



  ##  Binding Quota 85 - 97% (Disk Quota Help)
  - SSH into affected binding. Determine if alert is dbserver or appserver. 
    - follow either DISK QUOTA ALERT APPSERVER or # DISK QUOTA ALERT DBSERVER guides