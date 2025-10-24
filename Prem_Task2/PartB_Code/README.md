# Mini DHCP + DNS Simulator

This Python program simulates **DHCP (Dynamic Host Configuration Protocol)** and **DNS (Domain Name System)**. It allows simulated nodes to request IP addresses from a DHCP server, register themselves in a DNS server, and “ping” other nodes by resolving their names to IP addresses.

---

## Components

### 1. DHCP Server

The DHCP server automatically assigns IP addresses to nodes in the network. When a node boots:

1. It broadcasts a **DHCP Discover** message asking for an IP.  
2. The DHCP server responds with a **DHCP Offer**, selecting an available IP from its pool.  
3. The node then sends a **DHCP Request** to confirm the offered IP.  
4. Finally, the DHCP server sends a **DHCP Acknowledge** confirming the IP.  

This process ensures that no two devices are assigned the same IP and that each device can communicate within the network without manual configuration. 

---

### 2. DNS Server

Once a node receives an IP from the DHCP server, it registers itself in the DNS server. The DNS server stores a mapping of **node name → IP address**. 

1. It sends a query to the DNS server asking for the IP of the target node.  
2. The DNS server resolves the name to an IP if it exists in its records.  
3. The node can then “ping” the target node using the resolved IP.  

If the target node does not exist in DNS, the query fails.

---

## Communication Flow

The following sequence shows how the simulator handles nodes joining the network and communicating, based on the Python code:

1. **Node Booting**  
   - Each node calls `boot()`:
     - Sends a **DHCP Discover** message (`discover_dhcp()`) to the DHCP server.
     - DHCP server responds with an **offered IP** (`offer_ip()`).
     - Node requests this IP (`request_dhcp()`), and DHCP acknowledges it (`acknowledge()`).
     - Node registers its name and IP in the DNS server (`dns.register()`).

2. **Example (Node1 and Node2)**  
   - `Node1.boot()`:
     ```
     Node1 sent a BROADCAST message with IP 0.0.0.0
     DHCP receives the message from Node1
     DHCP offered 192.34.45.10 to Node1
     Node1 requests DHCP for 192.34.45.10
     DHCP assigns IP 192.34.45.10 to Node1
     DNS registers Node1 → 192.34.45.10
     ```
   - `Node2.boot()`:
     ```
     Node2 sent a BROADCAST message with IP 0.0.0.0
     DHCP receives the message from Node2
     DHCP offered 192.34.45.11 to Node2
     Node2 requests DHCP for 192.34.45.11
     DHCP assigns IP 192.34.45.11 to Node2
     DNS registers Node2 → 192.34.45.11
     ```

3. **Ping Simulation**  
   - Node1 wants to communicate with Node2:
     ```
     Node1 sends a DNS query for Node2
     DNS resolves Node2 → 192.34.45.11
     Pinging successful: Node1(192.34.45.10) → Node2(192.34.45.11)
     ```
   - Node1 tries to ping a non-existent node (Node3):
     ```
     Node1 sends a DNS query for Node3
     DNS resolves Node3 → not found
     Ping failed: Node3 is not a valid domain
     ```

4. **Summary**  
   - DHCP handles **automatic IP allocation** and avoids conflicts.  
   - DNS handles **name-to-IP resolution** so nodes can refer to each other by name.  
   - Nodes interact in the network via **booting → DHCP → DNS → ping** flow.  

---

