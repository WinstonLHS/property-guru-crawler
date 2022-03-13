from property import Property
from bs4 import BeautifulSoup

# from webcrawler import TEMP_FILE

TEMP_FILE = 'saved_pages/page.html'

def extract_property(html : str):
    doc = BeautifulSoup(text, 'html.parser')
    p = Property()
    p.set_address(find_address(doc))
    return p

def find_address(doc: BeautifulSoup) -> str:
    matches = doc.find_all(attrs={"itemprop" : "streetAddress"})
    match = matches.pop()
    return match.text

file = open(TEMP_FILE)
text = file.read()


p = extract_property(text)
print(p.address)