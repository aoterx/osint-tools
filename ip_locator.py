import requests

def trace_ip(ip_address):
    print(f"[*] Initiating trace on IP: {ip_address}")
    print("-" * 45)

    # We use a public API for IP geolocation
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url, timeout=5)
        # Convert the raw JSON response into a Python dictionary
        data = response.json()

        # Check if the API successfully found the IP
        if data.get("status") == "success":
            print("[+] Target Located Successfully!")
            print(f"    > IP Address  : {data.get('query')}")
            print(f"    > Country     : {data.get('country')}")
            print(f"    > Region/City : {data.get('regionName')} / {data.get('city')}")
            print(f"    > Coordinates : {data.get('lat')} / {data.get('lon')}")
            
            print("-" * 45)
            # Generate a clickable map link for physical team deployment
            map_link = f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
            print(f"[*] Google Maps Link: {map_link}")
            
        else:
            print(f"[-] Trace failed. Reason: {data.get('message', 'Unknown error')}")
            
    except requests.exceptions.RequestException:
        print("[!] Critical error: Could not connect to geolocation server.")
        
    print("-" * 45)
    
print("=== BASIC IP TRACKER ===")
target_ip = input("Enter target IP address (leave blank to trace your own IP): ")
trace_ip(target_ip)
