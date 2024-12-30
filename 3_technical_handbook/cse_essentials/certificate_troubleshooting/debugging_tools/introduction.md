# Debugging Tools

## Purpose
Learn to diagnose SSL/TLS certificate issues using various tools.

### Recommended Tools
1. **Browser DevTools**:
   - Inspect the certificate details in the browser (e.g., Chrome Security tab).
2. **OpenSSL**:
   - Verify certificates:
     ```bash
     openssl x509 -in cert.pem -text -noout
     ```
   - Test connections:
     ```bash
     openssl s_client -connect example.com:443
     ```
3. **SSL Labs**:
   - Use the SSL Labs test to analyze certificate configurations.
4. **cURL**:
   - Check certificates during HTTP requests:
     ```bash
     curl -v https://example.com
     ```
5. **Online Certificate Checkers**:
   - Use tools like \"whynopadlock.com\" or \"digicert.com/help\".

