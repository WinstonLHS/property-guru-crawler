from common import TEMP_PROPERTIES_CSV, TEMP_HTML
from property import Property
from bs4 import BeautifulSoup

HTML_PARSER = 'html.parser'

def extract_property_from_text(text : str):
    doc = BeautifulSoup(text, HTML_PARSER)
    return extract_property(doc)

def extract_property(doc : BeautifulSoup):
    p = Property()
    p.set_address(find_address(doc))
    p.set_year_built(find_year_built(doc))
    p.set_size(find_sqft(doc))
    p.set_lease_length(find_lease_length(doc))
    p.compute_years_left()
    return p

def find_address(doc : BeautifulSoup) -> str:
    matches = doc.find_all(attrs={"itemprop" : "streetAddress"})
    match = matches.pop()
    return match.text

def find_year_built(doc : BeautifulSoup) -> int:
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

def find_sqft(doc : BeautifulSoup) -> float:
    COLUMN_TAG_NAME = 'tr'
    COLUMN_TAG_ATTRS = {'class':'property-attr floor-area'}
    VALUE_TAG_NAME = 'td'
    VALUE_TAG_ATTRS = {'class':'value-block', 'itemprop':'value'}
    column_tag_found = doc.find_all(name=COLUMN_TAG_NAME, attrs=COLUMN_TAG_ATTRS).pop()
    value_tag_found = column_tag_found.find_all(name=VALUE_TAG_NAME, attrs=VALUE_TAG_ATTRS).pop()
    value_text = value_tag_found.text
    if value_text.__contains__('sqft'):
        endIndex = value_text.index('sqft')
        value_text = value_text[:endIndex]
        return float(value_text)
    elif value_text.__contains__('sqm'):
        endIndex = value_text.index('sqm')
        value_text = value_text[:endIndex]
        sqm = int(value_text)
        sqft = sqm * (1 / 0.3048)**2
        return float(sqft)
    else:
        return float(value_text)

def find_lease_length(doc : BeautifulSoup) -> int:
    COLUMN_TAG_NAME = 'tr'
    COLUMN_TAG_ATTRS = {'class':'property-attr'}
    column_tags = doc.find_all(name=COLUMN_TAG_NAME, attrs=COLUMN_TAG_ATTRS)
    if len(column_tags) < 1:
        raise Exception('expected at least 1 match')

    VALUE_TAG_ATTRS = {'class':'value-block', 'itemprop':'value'}
    VALUE_TAG_NAME = 'td'
    column_tag = column_tags[0]
    tenure = column_tag.find_next(text='Tenure')
    value_tag = tenure.find_next(name=VALUE_TAG_NAME, attrs=VALUE_TAG_ATTRS)
    lease_text = value_tag.text
    if not lease_text.__contains__('Leasehold'):
        raise Exception('expected leasehold tenure')

    lease_years = lease_text[:lease_text.index('-year Leasehold')]
    return int(lease_years)
