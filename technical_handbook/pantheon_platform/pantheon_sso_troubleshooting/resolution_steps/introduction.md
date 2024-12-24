# Resolution Steps for Pantheon SSO Issues

## Purpose
Provide step-by-step guidance to resolve common SSO issues in Pantheon environments.

### Steps for Common Issues
1. **Redirect Loops**:
   - Clear Pantheon’s Global CDN cache.
   - Adjust caching rules to bypass SSO-related endpoints.
2. **Certificate Errors**:
   - Renew expired certificates and update them in both Pantheon and IdP configurations.
   - Verify the certificate chain using OpenSSL.
3. **Login Failures**:
   - Check SAML response attributes (e.g., NameID, roles).
   - Ensure that the ACS URL matches the configuration in the IdP.
4. **URL Endpoint Mismatches**:
   - Confirm that the IdP metadata matches Pantheon’s SSO configuration.
5. **Time Synchronization**:
   - Ensure clocks on both Pantheon servers and the IdP are synchronized using NTP.

