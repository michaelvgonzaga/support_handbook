# Professional Services Escalation Guide
last reviewd jan 2025

## Confluence:
https://getpantheon.atlassian.net/wiki/spaces/CS/pages/2780758174/CSE+to+PS+Handoff+Process

## Guide:
Jira Ticket Creation and Handoff Process
Step 1: Create Jira Card
- Go to Jira: PS | Kanban board > Click "Create" > Select    Issue Type:
  - AGCDN Troubleshooting: Setup issues.
  - AGCDN Consulting: Features, domains, redirects, WAF, etc.
  - SSO/SAML: Dashboard SSO or SAML issues.
  - Secure Integration: SI-related issues.
  - Custom Certificates: Certificate problems.

- Fill Required Fields:
  - Priority (see next section) - This is required.
    - Category Type
    - Zendesk Ticket (Full URL)
    - Domain Name
    - ORG UUID
    - Summary



- Step 2: Attach Jira to Zendesk
  - Add Tags:
    - agcdn_to_ps, sso_to_ps, si_to_ps, cc_to_ps (based on ticket type).
  - Link Jira Card:
    - Use Jira card ID > Click “Link Issue” > Confirm linked card.
- Step 3: Handoff Zendesk Ticket
  - Notify Customer: Confirm handoff to PS team.
  - Assign Ticket: Assign to PS/Implementation for AGCDN, Certs, SSO, SI, Load Tests.
  - Add Notes: Document actions and changes.
  - Urgent Issues: Ping @implem in Slack only if critical.