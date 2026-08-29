import sys
import pywikibot

# Enable UTF-8 encoding for Windows terminal output
sys.stdout.reconfigure(encoding='utf-8')

print("Connecting to Wikidata...")
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

print(f"Logged in user: {site.user()}")

# Load Wikidata Sandbox Item Q4115189
item_id = 'Q4115189'
item = pywikibot.ItemPage(repo, item_id)
item.get()

print(f"Loaded Sandbox Item ({item_id}) label: {item.labels.get('en', 'None')}")

labels = {'hi': 'विकिडाटा सैंडबॉक्स'}
descriptions = {'en': 'Sandbox item for Pywikibot testing'}

print("Updating Wikidata Sandbox item...")
item.editLabels(labels, summary="Automated edit test via Pywikibot")
item.editDescriptions(descriptions, summary="Automated edit test via Pywikibot")

print(f"SUCCESS: View Wikidata Sandbox live at: https://www.wikidata.org/wiki/{item_id}")
