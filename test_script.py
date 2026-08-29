import pywikibot

print("Connecting to Wikidata...")
site = pywikibot.Site('wikidata', 'wikidata')

# Fetch Wikidata Sandbox Item Q4115189
item = pywikibot.ItemPage(site.data_repository(), 'Q4115189')
item.get()

print(f"Successfully loaded item: {item.labels.get('en', 'No English label')}")
print("Pywikibot is working perfectly!")
