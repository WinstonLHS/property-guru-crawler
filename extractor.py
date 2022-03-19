from property import Property
from bs4 import BeautifulSoup

# from webcrawler import TEMP_FILE

TEMP_FILE = 'saved_pages/page.html'

def extract_property_from_text(text : str):
    doc = BeautifulSoup(text, 'html.parser')
    return extract_property(doc)

def extract_property(doc : BeautifulSoup):
    p = Property()
    p.set_address(find_address(doc))
    p.set_year_built(find_year_built(doc))
    return p

def find_address(doc : BeautifulSoup) -> str:
    matches = doc.find_all(attrs={"itemprop" : "streetAddress"})
    match = matches.pop()
    return match.text

def find_year_built(doc: BeautifulSoup) -> int:
    column_tag_attrs={
        "class":"property-attr completion-year"
    }
    value_attrs = {
        "class":"value-block",
        "itemprop":"value"
    }
    matches = doc.find_all(name='tr', attrs=column_tag_attrs)
    if len(matches) < 1:
        raise Exception("found zero matches")

    match = matches.pop()
    value_matches = match.find_all(name='td', attrs=value_attrs)
    if len(value_matches) != 1:
        raise Exception('found no match')
    value_text = value_matches[0].text

    return int(value_text)


file = open(TEMP_FILE)
text = file.read()


p = extract_property_from_text(text)
print(p.year_built)