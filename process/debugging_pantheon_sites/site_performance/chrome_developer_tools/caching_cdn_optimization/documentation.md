#  Chrome Dev tools: Caching and CDN optimization
Using Chrome DevTools to Analyze Caching and CDN optimization. Improve response times by optimizing caching and Pantheon’s Global CDN.

- Open Chrome DevTools → Network tab.
- Check response headers:
    - x-cache: HIT → Cached (good).
    - x-cache: MISS → Not cached (need to fix).

###### Pantheon-Specific Caching Fixes
- Enable Pantheon Global CDN.
- Use Pantheon Edge Cache for HTML caching.
- Optimize Redis Object Cache for database-heavy operations.