from duckduckgo_search import DDGS
import unicodedata
import time

def remove_diacritics(text):
    """
    Strips diacritics from a string.
    Example: 'Țiriac' becomes 'Tiriac', 'Băsescu' becomes 'Basescu'.
    """

    # Normalize translates special characters into their base character + a combining mark
    normalized = unicodedata.normalize('NFD', text)
    # We keep only the base characters (ignoring the 'Mn' = Mark, Nonspacing category)
    return ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')

def person_radar(target_name):
    # Automatically generates the version without diacritics
    target_clean = remove_diacritics(target_name)

    # We create a list of targets. We use a 'set' to remove duplicates
    # (in case the user entered a name that didn't have diacritics to begin with)
    targets_to_scan = list(set([target_name, target_clean]))

    print("-" * 80)
    print(f"[*] Deploying OSINT Radar for target: {target_name}")
    print("-" * 80)
    
    # Open a session with the search engine
    with DDGS() as ddgs:
        # Loop through both the original name and the cleaned one
        for current_target in targets_to_scan:
            print(f"\n[>>>] SCANNING VARIATION: {current_target}")
            
            # The Dorks are now generated for whichever variation is currently looping
            queries = [
                f'"{current_target}"',
                f'"{current_target}" (news OR stiri OR press OR articol OR media)',
                f'"{current_target}" (court OR instanta Or dosar OR politia OR arestat)'
            ]
            
            for query in queries:
                print(f"  [*] Executing Dork: {query}")
                try:
                    # Fetch the top 5 results for each tactical query
                    results = list(ddgs.text(query, max_results=10))
                    
                    if not results:
                        print("    [-] No immediate results found for this dork.\n")
                        continue
                        
                    for idx, result in enumerate(results, 1):
                        title = result.get('title', 'No Title')
                        link = result.get('href', 'No Link')
                        
                        print(f"      [{idx}] TITLE: {title}")
                        print(f"          LINK  : {link}\n")
                    
                except Exception as e:
                    print(f"    [!] Radar jammed or rate-limited: {e}")
            
            # Polite delay between different search queries to avoid IP ban
            time.sleep(2)
            
    print("-" * 80)
    print("[*] Radar sweep completed.")

if __name__ == "__main__":
    print("=== TARGET RADAR (NEWS & WEB SCRAPER) ===")
    target = input("Enter the full name of the target (with or without diacritics; e.g., Ion Popescu): ")
    person_radar(target)
