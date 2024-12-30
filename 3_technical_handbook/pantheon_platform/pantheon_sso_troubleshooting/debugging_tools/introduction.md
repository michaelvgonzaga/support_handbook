# Debugging Tools for Pantheon SSO

## Purpose
Use appropriate tools to diagnose and resolve SSO-related issues specific to Pantheon.

### Recommended Tools
1. **Browser DevTools**:
   - Inspect network requests and response headers.
2. **SAML Tracer**:
   - Analyze SAML messages for misconfigurations.
3. **Pantheon Dashboard Logs**:
   - Review server logs for errors related to SSO flows.
4. **OpenSSL**:
   - Validate certificates and check expiration:
     ```bash
     openssl x509 -in cert.pem -text -noout
     ```
5. **cURL**:
   - Test connectivity and SSO endpoints:
     ```bash
     curl -v https://example.com/sso-endpoint
     ```
6. **IdP Debugging Tools**:
   - Tools provided by the Identity Provider (e.g., Okta or Azure logs).

