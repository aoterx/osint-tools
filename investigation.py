import requests
import time

def cauta_username(username):
    print(f"[*] Începem investigația pentru ținta: {username}")
    print("-" * 40)

    platforme = {
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Pinterest": "https://ro.pinterest.com/{}/",
        "Steam": "https://steamcommunity.com/id/{}",
	"Instagram" : "https://instagram.com/{}"
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for nume_site, url_baza in platforme.items():
        url_tinta = url_baza.format(username)
        try:
            raspuns = requests.get(url_tinta, headers=header, timeout=5)
            if raspuns.status_code == 200:
                print(f"[+] GĂSIT pe {nume_site}: {url_tinta}")
            elif raspuns.status_code == 404:
                print(f"[-] Nu există pe {nume_site}")
            else:
                print(f"[?] Răspuns incert pe {nume_site} (Cod HTTP: {raspuns.status_code})")
        except requests.exceptions.RequestException:
            print(f"[!] Eroare de conectare la {nume_site}")
        time.sleep(1)

    print("-" * 40)
    print("[*] Investigație finalizată.")

nume_de_cautat = input("Introdu username-ul suspectului: ")
cauta_username(nume_de_cautat)

