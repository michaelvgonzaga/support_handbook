# Pantheon Caching

## Purpose
Specific caching strategies and layers provided by Pantheon.io for optimized performance.

### Key Topics
1. **Caching Layers in Pantheon**:
   - **Edge Cache**:
     - Cached at Pantheon’s Global CDN layer.
     - Default TTL of 1 hour.
     - Configured via `Cache-Control` and `Surrogate-Control` headers.
   - **Application Cache**:
     - WordPress and Drupal page caching.
     - Plugins/modules can extend caching.

2. **How Pantheon Handles Cache Invalidation**:
   - Automatic invalidation for updates to content (e.g., new posts or pages).
   - Manual invalidation via the Pantheon dashboard.

3. **Customizing Pantheon Cache**:
   - Use headers like `Surrogate-Key` for granular cache control.

4. **Best Practices for Pantheon Caching**:
   - Leverage the Global CDN effectively.
   - Ensure compatibility of caching plugins with Pantheon architecture.

5. **Debugging Pantheon Cache**:
   - Use `curl` or browser DevTools to inspect `X-Pantheon-Cache` headers.

