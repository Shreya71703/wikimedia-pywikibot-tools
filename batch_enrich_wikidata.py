import time
import sys
import pywikibot

# Enable UTF-8 encoding for Windows terminal output
sys.stdout.reconfigure(encoding='utf-8')

# Connect to Wikidata repository
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

print("==================================================")
print("  AUTOMATED WIKIDATA BATCH ENRICHMENT PIPELINE    ")
print("==================================================")
print("Connected to Wikidata repository as Shreyapedia@PywikibotTest\n")

# Batch dataset of Q-items needing multilingual label/description enrichment
batch_items = {
    # Wikidata Sandbox
    'Q4115189': {
        'labels': {'hi': 'विकिडाटा सैंडबॉक्स', 'en': 'Wikidata Sandbox'},
        'descriptions': {
            'hi': 'स्वचालित पायविकिबॉट स्क्रिप्ट परीक्षण के लिए सैंडबॉक्स आइटम',
            'en': 'Sandbox item for Pywikibot testing'
        }
    },
    # Taj Mahal
    'Q9141': {
        'labels': {'hi': 'ताज महल', 'en': 'Taj Mahal'},
        'descriptions': {'hi': 'आगरा, भारत में स्थित ऐतिहासिक सफेद संगमरमर का मकबरा'}
    },
    # Samosa
    'Q180424': {
        'labels': {'hi': 'समोसा', 'en': 'Samosa'},
        'descriptions': {'hi': 'दक्षिण एशियाई तला हुआ मसालेदार व्यंजन'}
    },
    # Kurta
    'Q80989': {
        'labels': {'hi': 'कुर्ता', 'en': 'Kurta'},
        'descriptions': {'hi': 'पारंपरिक दक्षिण एशियाई परिधान'}
    }
}

print(f"Loaded {len(batch_items)} item(s) for processing.\n")

success_count = 0

for qid, data in batch_items.items():
    try:
        print(f"--------------------------------------------------")
        print(f"Processing Item: {qid}...")
        item = pywikibot.ItemPage(repo, qid)
        item.get()

        current_en = item.labels.get('en', 'None')
        current_hi = item.labels.get('hi', 'None')
        print(f"  Current English Label: {current_en}")
        print(f"  Current Hindi Label:   {current_hi}")

        # Update Labels
        if 'labels' in data:
            item.editLabels(data['labels'], summary="Added/updated multilingual labels via Pywikibot automation")
            print("  [+] Labels updated successfully.")

        # Update Descriptions
        if 'descriptions' in data:
            item.editDescriptions(data['descriptions'], summary="Added/updated multilingual descriptions via Pywikibot automation")
            print("  [+] Descriptions updated successfully.")

        success_count += 1
        print(f"SUCCESS: Item {qid} successfully enriched!")

        # API throttling pause
        print("  Sleeping 3s for API throttle hygiene...")
        time.sleep(3)

    except Exception as e:
        print(f"  NOTICE for {qid}: {e}")

print("==================================================")
print(f"BATCH PROCESS COMPLETE: {success_count}/{len(batch_items)} items processed.")
print("==================================================")
