# Best Practices for Pantheon SSO

## Purpose
Implement best practices to ensure secure and efficient SSO integration in Pantheon environments.

### Recommendations
1. **Use Proper Caching Rules**:
   - Exclude SSO endpoints from caching in Pantheon’s Global CDN.
2. **Monitor Certificate Expirations**:
   - Set alerts for certificate renewal.
3. **Validate IdP Configuration**:
   - Regularly review IdP metadata and ACS URL configurations.
4. **Enable Logging**:
   - Use verbose logging in both Pantheon and IdP for detailed error tracking.
5. **Test in Staging**:
   - Validate SSO configurations in a staging environment before deploying to production.
6. **Implement MFA**:
   - Add Multi-Factor Authentication (MFA) for additional security.

