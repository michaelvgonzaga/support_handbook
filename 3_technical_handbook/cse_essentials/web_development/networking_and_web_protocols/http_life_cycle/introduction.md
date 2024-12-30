# HTTP Life Cycle

## Purpose
Understand the step-by-step process of how an HTTP request is handled from client to server and back.

### Key Phases
1. **DNS Resolution**:
   - The browser resolves the domain name into an IP address using DNS.

2. **TCP Handshake**:
   - Establishes a connection between the client and server using a three-way handshake.

3. **Request Sent**:
   - The client sends an HTTP request (e.g., GET or POST) to the server, including headers and optional body.

4. **Server Processing**:
   - The server processes the request and prepares a response (e.g., fetching data from a database).

5. **Response Sent**:
   - The server sends the HTTP response back to the client, including headers, status code, and body.

6. **Rendering/Processing**:
   - The browser processes the response and renders the webpage or handles data as needed.

### Tools for Visualizing HTTP Life Cycle
- Use `curl` or Postman to inspect requests and responses.
- Browser DevTools (Network tab) to monitor requests and measure performance.


