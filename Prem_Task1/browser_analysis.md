# Part A: Browser DevTools Analysis

---

## 1. HTTP vs HTTPS Comparison

---

### Comparison of Request Headers

#### **HTTP (neverssl.com)**
- Request URL starts with `http://`
- Protocol: http/1.1
- All header information (Host, User-Agent, etc.) is sent in plain, readable text across the network.

#### **HTTPS (github.com and youtube.com)**
- Request URL starts with `https://`
- Protocol: h2 (HTTP/2) — a faster and more secure modern protocol.
- Headers are visible in DevTools for debugging, but are encrypted in actual transit.

---

### Data Visibility in Requests

 **HTTP** : ✅ Yes - All request and response data (headers, form fields, HTML) are visible as plain text. Anyone intercepting traffic can read or alter it. 
 **HTTPS** : ❌ No - The browser decrypts data locally for you, but on the network it appears as **encrypted bytes** — unreadable to outsiders. 

---

### Why HTTPS is More Secure

**HTTPS (Hypertext Transfer Protocol Secure)** adds a layer of encryption using **TLS**, providing three essential protections that HTTP lacks:

1. 🔒 **Encryption** – Data between browser and server is encrypted, ensuring confidentiality and preventing eavesdropping.
2. ✅ **Authentication** – SSL certificates verify that you are communicating with the legitimate website (e.g., `youtube.com`) and not an imposter.
3. 🧩 **Integrity** – Ensures that data is not modified in transit, guaranteeing the response you receive is authentic.

---

## 2. Request Analysis

### Total Number of Requests

| **neverssl.com**  2-requests 
| **github.com**  161-requests 
| **youtube.com**  154-requests

---

### Types of Resources Loaded


 **neverssl.com** : HTML, favicon - Simple static page, no JS or CSS. 
| **github.com** : HTML, CSS, JS, Images, Fonts, Fetch/XHR - Dynamic web application loading repositories, user data, and UI scripts. 
| **youtube.com** : HTML, CSS, JS, Images, Video, XHR - Heavily dynamic with video streams, ads, analytics, and user interactions. 

---

### Which Website Made the Most Requests and Why?

Both GitHub and YouTube are complex dynamic web applications that load dynamic content using API calls

In contrast, neverssl.com is a simple, static HTML page with no dynamic content, resulting in just two requests.

---

## 3. Performance Insights

**neverssl.com** : 3.85sec Load Time
**github.com** : 1.23sec Load Time
**youtube.com** : 2.92sec Load Time

---

### Longest Requests

**neverssl.com** - `/online/` : 3.83sec - Main document load — More delay due to network issues 
**github.com** - `my_top_repositories` : 491msec - Fetches user data via API 
**youtube.com** - `log_event` : 1.87sec 

---

### Explanation of Timing Phases

**From Screenshot**: `dns_query.png`
| **DNS Lookup** : Resolves domain name to IP address. Search fot IP in the cache.
| **Connection Time** : Establishes TCP connection.
| **Waiting (TTFB)** : “Time To First Byte” — waiting for the server’s first response. 
| **Content Download** : Time to receive the remaining response data. 
