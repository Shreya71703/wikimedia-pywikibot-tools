import pywikibot

# Connect to Wikidata
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

print("Connected to Wikidata repository!")

# Example Item: Wikidata Sandbox Item (Q4115189)
item_id = 'Q4115189'
item = pywikibot.ItemPage(repo, item_id)
item.get()

print(f"Loaded Item: {item_id}")
print(f"Current English Label: {item.labels.get('en', 'None')}")
print(f"Current Hindi Label: {item.labels.get('hi', 'None')}")

# Multilingual Labels & Descriptions to update
new_labels = {
    'hi': 'विकिडाटा सैंडबॉक्स'
}

new_descriptions = {
    'en': 'Sandbox item for testing Pywikibot automated scripts',
    'hi': 'स्वचालित पायविकिबॉट स्क्रिप्ट परीक्षण के लिए सैंडबॉक्स आइटम'
}

# Apply updates safely
print("\nUpdating labels and descriptions...")
item.editLabels(new_labels, summary="Updated Hindi label via Pywikibot script")
item.editDescriptions(new_descriptions, summary="Updated English & Hindi descriptions via Pywikibot script")

print("SUCCESS: Check item live on Wikidata: https://www.wikidata.org/wiki/" + item_id)
