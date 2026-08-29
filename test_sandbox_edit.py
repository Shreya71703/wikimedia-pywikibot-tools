import sys
import pywikibot

sys.stdout.reconfigure(encoding='utf-8')

print("Connecting to English Wikipedia...")
site = pywikibot.Site('en', 'wikipedia')

page = pywikibot.Page(site, 'User:Shreyapedia/sandbox')

print(f"Current sandbox text:\n{page.text}\n")

# Update sandbox text
page.text = "Hello! Automated Pywikibot edit successful! Registered bot contribution by Shreyapedia."

print("Saving edit to User:Shreyapedia/sandbox...")
page.save(summary="Automated edit test via Pywikibot script")

print("SUCCESS: View edit live at: https://en.wikipedia.org/wiki/User:Shreyapedia/sandbox")
