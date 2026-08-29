import sys
import pywikibot

# Enable UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

print("Connecting to Wikidata User namespace...")
site = pywikibot.Site('wikidata', 'wikidata')

page = pywikibot.Page(site, 'User:Shreyapedia/sandbox')

print(f"Current Wikidata Sandbox user page text:\n{page.text}\n")

page.text = "Hello! Automated Pywikibot edit test on Wikidata user sandbox!"

print("Saving edit to Wikidata user sandbox...")
page.save(summary="Automated edit test via Pywikibot script")

print("SUCCESS: View edit live at: https://www.wikidata.org/wiki/User:Shreyapedia/sandbox")
