import re
from cloudscraper import create_scraper
from django.core.validators import URLValidator
from django.forms import ValidationError

from extractor import Property, extract_property, find_address
TEMP_FILE = 'saved_pages/page.html'

def prompt_for_url():
    link = input('please enter the property guru link:')
    return link

def extract_property(link: str) -> Property:
    if not is_valid_url(link):
        return
    html = fetch_html(link)
    save_to_file(html) # snapshot
    return extract_property(html)

def fetch_html(url: str):
    scraper = create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'android',
            'desktop': True
        })
    return scraper.get(url).text

def is_valid_url(url: str):
    validate = URLValidator()
    try:
        validate(url)
        print("Entered a valid URL.")
        return True
    except ValidationError as e:
        print("Entered an invalid URL")
        return False

def save_to_file(content: str, file_name = TEMP_FILE):
    with open(file_name, 'w') as file:
        file.write(content)
