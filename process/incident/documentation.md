# Incident
source: https://getpantheon.atlassian.net/wiki/spaces/CS/pages/2485813249/Escalations+Bugs+Process+SLAs+Definitions

###### Escalation
Urgent issues that must be handled as soon as possible. Acknowledgment by OCE: 15 minutes. Target Resolution by OCE: 4 hours

Incidents:
 - Live sites down
 - Platform Infrastructure down
 - High Revenue impact
 - Data and Asset loss
 - Unable to deploy code
 - Unable to pay for site
 - Unable to create a site
 - Data Backup Recovery

###### OCE
Issues on this list are generally time sensitive, but not product escalations. The Severity for an OCE Task should be High.

Incidents:
 - Locked appserver/dbserver/codeserver, etc
 - Duplicate database server
 - Failing converge workflow (single customer)
 - Adding a customer to the domain protection exception list
 - Dashboard commit log not loading
   - Git-Diff Not Showing for SFTP mode
   - Codeserver Logs
   - Codeserver repository corruption
 - Deleting backups as requested by customer
 - Customer Site does not have vanity domains on site creation

Severity:

- Highest:
  - Multidev creation failing (Impacting multiple customers)
  - Solr server unavailable / site not down but functionally impaired
  - Unable to reset password or access the dashboard
  - Unable to initialize Test or Live (blocking go-live)
  - 404 unknown site after site creation (blocking go-live)

- High:
  - No workaround
  - Customer contractual Uptime SLA at risk
  - Severe performance impact

- Medium:
 - Workaround is available
 - Moderate performance impact

- Low:
 - Not blocking work on site
 - User experience bugs
 - Site performance is not impacted
