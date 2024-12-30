# General Caching Overview

## Purpose
Caching improves website performance by storing copies of data to reduce latency and load on backend systems.

### Key Concepts
1. **Cache Layers**:
   - Client-Side: Browser-based caching.
   - Server-Side: Application and database caches.
   - CDN: Distributed network caching.

2. **Cache Invalidation**:
   - Strategies to refresh cached content (e.g., Time-to-Live (TTL), manual invalidation).

3. **Common Headers for Caching**:
   - `Cache-Control`: Directives for caching.
   - `Expires`: Sets an expiration date/time for the resource.
   - `ETag`: Validation token for cache freshness.

