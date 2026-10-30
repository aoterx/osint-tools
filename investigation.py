import requests
import time

def search_username(username):
    print(f"[*] Starting OSINT investigation for target: {username}")
    print("-" * 40)

    # Dictionary of platforms and their base URLs
    platforms = {
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Pinterest": "https://ro.pinterest.com/{}/",
        "Steam": "https://steamcommunity.com/id/{}",
	"Instagram" : "https://instagram.com/{}"
    }

    # Spoofing the User-Agent to bypass basic bot protection
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for site_name, base_url in platforms.items():
	target_url = base_url.format(username)
	try:
	   response = requests.get(target_url, headers=headers, timeout=5)

	   # Extracting the raw HTML text from the response
	   page_content = response.text.lower()

	   if raspuns.status_code == 200:
		# Checking for common false positive strings in the HTML
		false_positive_strings = ["this page isn't available", "page not found", "does not exist", "error 404"]

		# If any false positive string is found in the page text, the account doesn't exist
		if any(fp_string in page_content for fp_string in false_positive_strings):
		   print(f"[-] False Positive (Page exists, but account doesn't) on {site_name}")
		else:
		   print(f"[+] FOUND (Confirmed) on {site_name}: {target_url}")

	   elif response.status_code == 404:
		print(f"[-] Not found (404) on {site_name}")
	   else:
		print(f"[?] Unknown status on {site_name} (HTTP Code: {response.status_code})")

	except requests.exceptions.RequestException:
	   print(f"[!] Connection error to {site_name}")

	# Polite delay to prevent IP blocking
	time.sleep(1)

    print("-" * 40)
    print("[*] Investigation complete.")

target_username = input("Enter target username: ")
search_username(target_username)
