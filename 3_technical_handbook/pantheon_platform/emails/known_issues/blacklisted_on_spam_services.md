# Blacklisted on spam services


## Context
The Pantheon platform's default email servers are listed in Spamhaus due to a history of misconfigured email setups, impacting deliverability.

While properly configured SPF records can help, working with an external email service provider is strongly recommended for improved reputation and features like bounce management.

## Solution
The only known reported workaround this is to ensure your DNS setup uses A/AAAA records instead of CNAMES for subdomains helps to improve domain reputation for Spamhaus.

last reviewed: 01-05-2025
source: https://getpantheon.atlassian.net/wiki/spaces/CS/pages/556662909/Common+Security-related+Customer+Requests#What-do-I-tell-customers-who-find-they-are-blacklisted-on-spam-services%3F