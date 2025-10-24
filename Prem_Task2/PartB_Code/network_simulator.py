class DHCP():
    available_ips=[]
    def __init__(self):
        for i in range(10,21):
            self.available_ips.append(f'192.34.45.{i}')
    
    def offer_ip(self):
        if self.available_ips:
            ip_offered=self.available_ips.pop(0)
            return ip_offered
        else:
            return None
        
    def acknowledge(self,name,ip):
        print(f'DHCP assigns IP {ip} for {name} and also provides the DNS sserver IP nearest Gateway IP and Lease Time')


class DNS():
    registered_ips={}
    def register(self,name,ip):
        self.registered_ips[name]=ip
        print(f'DNS registers {name} IP as {ip}')
    
    def resolve(self,name):
        ip=self.registered_ips.get(name)
        if ip:
            return ip
        else:
            return None
                


class Node():
    def __init__(self,name,dhcp,dns):
        self.name=name
        self.ip='0.0.0.0'
        self.dhcp=dhcp
        self.dns=dns

    def discover_dhcp(self):
        print(f'{self.name} sent a BROAD CAST MESSAGE with IP {self.ip}')
        print(f'DHCP recieves the message sent by {self.name}')
        self.offered_ip=dhcp.offer_ip()
        if self.offered_ip:
            print(f'DHCP offered {self.offered_ip} to {self.name}')
            return not None
        else:
            print(f'No IP is available at this moment')
            return None
        
    def request_dhcp(self):
        print(f'{self.name} requests DHCP for the IP {self.offered_ip}')
        dhcp.acknowledge(self.name,self.offered_ip)
        self.ip=self.offered_ip
    
    def boot(self):
        print(f'----------------------{self.name} booting----------------------')
        if self.discover_dhcp():
            self.request_dhcp()
        else:
            return
        self.dns.register(self.name,self.offered_ip)
    
    def ping(self,target):
        print(f'{self.name} send a DNS query looking up for {target}')
        target_ip=self.dns.resolve(target)
        if target_ip:
            print(f'Pinging successful. {self.name}({self.ip}) is connected to {target}({target_ip})')
        else:
            print(f'Pinging failed.{target} is not a valid domain')

            
                      
dhcp=DHCP()
dns=DNS()
           
Node1=Node('Node1',dhcp,dns)
Node2=Node('Node2',dhcp,dns)

Node1.boot()
print('\n\n\n\n')
Node2.boot()

print('\n\n\n\n')
Node1.ping('Node2')
print("\n\n\n")
Node1.ping('Node3')