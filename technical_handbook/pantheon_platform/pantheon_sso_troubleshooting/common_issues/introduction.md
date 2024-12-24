# Common SSO Issues on Pantheon

## Purpose
Identify frequently encountered SSO issues in Pantheon environments and their potential causes.

### Key Issues
1. **Redirect Loops**:
   - Caused by conflicting caching settings in Pantheon’s CDN or app layers.
2. **Certificate Errors**:
   - Expired or mismatched certificates between Pantheon and the IdP.
3. **Login Failures**:
   - Incorrect SAML response formatting or missing attributes.
4. **Caching Conflicts**:
   - Cached SSO responses creating inconsistencies for users.
5. **URL Endpoint Mismatches**:
   - Incorrect ACS (Assertion Consumer Service) URL or IdP metadata.
6. **Time Synchronization Issues**:
   - Skewed clocks between Pantheon servers and the IdP.

