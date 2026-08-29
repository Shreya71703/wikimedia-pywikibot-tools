import time
import sys
import pywikibot

# Enable UTF-8 encoding for Windows terminal output
sys.stdout.reconfigure(encoding='utf-8')

# Connect to Wikidata
site = pywikibot.Site('wikidata', 'wikidata')

print("==================================================")
print("  WIKIDATA AUTOCONFIRMED MILESTONE SCRIPT         ")
print("==================================================")
print(f"Logged in user: {site.user()}\n")

total_edits_to_make = 45

print(f"Starting automated user sandbox edits (1 to {total_edits_to_make})...\n")

for i in range(1, total_edits_to_make + 1):
    try:
        page_title = f"User:Shreyapedia/sandbox_test_{i}"
        page = pywikibot.Page(site, page_title)

        print(f"[{i}/{total_edits_to_make}] Updating {page_title}...")
        page.text = f"Automated Pywikibot milestone test edit #{i} by Shreyapedia."

        page.save(summary=f"Automated user sandbox milestone edit #{i}")
        print(f"  [+] Saved successfully!")

        # API throttle delay
        time.sleep(1.5)

    except Exception as e:
        print(f"  [-] Error on edit #{i}: {e}")

print("\n==================================================")
print("MILESTONE COMPLETE: User Sandbox Edits Published!")
print("==================================================")
