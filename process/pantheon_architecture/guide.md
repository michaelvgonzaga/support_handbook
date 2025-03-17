# Pantheon architecture - User Request Workflow (Fastly + Pantheon)
1️⃣ User Request
↓ 
A visitor enters a URL in their browser, and the request is sent to the website.
2️⃣ Fastly POP (Nearest Edge Server - First Caching Layer)
↓ 
The request first reaches the closest Fastly Point of Presence (POP).
✅ Cache hit → The response is served instantly from Fastly.
❌ Cache miss → The request is sent to Origin Shield.
3️⃣ Origin Shield (Fastly Mid-Tier Cache - Second Caching Layer)
↓ 
Acts as a central cache layer to reduce traffic to Pantheon’s infrastructure.
✅ Cache hit → Content is served from Origin Shield.
❌ Cache miss → The request moves to Pantheon’s Global CDN (Varnish).
4️⃣ Pantheon Global CDN (Varnish - Third Caching Layer)
↓ 
✅ Cache hit → Content is served directly.
❌ Cache miss → The request is forwarded to Styx HTTP Router.
5️⃣ Styx HTTP Router (Traffic Director)
↓ 
Routes the request to the correct nginx web server in Pantheon’s infrastructure.
6️⃣ nginx (Web Server - Decision Point)
↓ 
If the request is for static content (images, CSS, JS, etc.) → Served from Valhalla fileserver.
If the request is dynamic (needs PHP processing) → Sent to PHP-FPM.
7️⃣ PHP-FPM (Executes Code - Application Layer)
↓ 
Runs PHP scripts and processes dynamic requests.
If database queries are needed, PHP communicates with MySQL.
8️⃣ MySQL Database (Stores and Retrieves Data)
↓ 
Queries data requested by PHP (e.g., user info, blog posts, products).
Data is returned to PHP-FPM for final processing.
9️⃣ Response Travels Back to the User
↓ 
Processed content goes back through the same caching layers:
🔄 nginx → Styx → Varnish → Origin Shield → Fastly POP → User.
Content is cached at multiple levels to optimize future requests.

Summary of Key Optimizations
✅ POP (Point of Presence) → First layer of caching closest to the user.
✅ Origin Shield → Reduces unnecessary hits to Pantheon’s origin.
✅ Pantheon Global CDN (Varnish) → Reduces origin server load.
✅ Efficient Routing (Styx) → Sends requests to the right server.
✅ nginx → Serves static files quickly; PHP-FPM handles dynamic content.
✅ Database Queries (MySQL) → Ensures dynamic content is served efficiently.
✅ Multiple Caching Layers → Faster page loads & better performance.