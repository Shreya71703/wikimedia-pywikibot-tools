import sys
import pywikibot

# Enable UTF-8 terminal encoding
sys.stdout.reconfigure(encoding='utf-8')

print("Connecting to Hindi Wikipedia...")
site = pywikibot.Site('hi', 'wikipedia')

page = pywikibot.Page(site, 'User:Shreyapedia/sandbox')

print(f"Current Hindi Wikipedia sandbox text:\n{page.text}\n")

page.text = "नमस्ते! यह पायविकिबॉट (Pywikibot) द्वारा स्वचालित संपादन परीक्षण है।"

print("Saving edit to Hindi Wikipedia sandbox...")
page.save(summary="Automated edit test via Pywikibot script")

print("SUCCESS: View edit live at: https://hi.wikipedia.org/wiki/User:Shreyapedia/sandbox")
