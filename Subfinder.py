
import requests
import os
import threading

print("                  -----SUBHUNTER------                    ")
print("----------------------------------------------------------")

domain = input("Enter the domain you want to scan for subdomain: ")
    

f = open('subdomain.txt','r')
content = f.read()
subdomains = content.splitlines()

#t1 = threading.Thread(target= requests.get(url1))
#t2 = threading.Thread(target= requests.get(url2))
#t1.start()
#t2.start()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(f"Result Subdomain: {url1}")
        requests.get(url2)
        print(f"Result Subdomain :{url2}")
        
        
    except requests.ConnectionError:
        pass
    
