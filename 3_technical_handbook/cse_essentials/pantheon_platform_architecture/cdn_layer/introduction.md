# CDN Layer

## Overview
Pantheon.io uses a Global CDN layer to deliver content to users with low latency and high performance.

### Key Features
1. **Content Distribution**:
   - Distributes static content (e.g., images, CSS, JS) across edge locations.
2. **Caching**:
   - Implements caching for anonymous user requests.
   - Default TTL is set to optimize performance while respecting cache-control headers.
3. **SSL/TLS Support**:
   - Provides HTTPS for all sites with Let’s Encrypt certificates or custom certificates.

### Benefits
- Accelerates content delivery.
- Reduces load on the origin servers.
- Enhances security with encrypted connections.

