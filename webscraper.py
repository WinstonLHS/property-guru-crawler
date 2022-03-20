from cloudscraper import create_scraper
from django.core.validators import URLValidator
from django.forms import ValidationError
from common import TEMP_HTML

from extractor import Property, extract_property, extract_property_from_html

def prompt_for_url():
    link = input('please enter the property guru link:')
    return link

def extract_property_from_link(link: str) -> Property:
    if not is_valid_url(link):
        raise Exception(f'entered an invalid url: {link}')
    html = fetch_html(link)
    save_to_file(html) # snapshot
    return extract_property_from_html(html)

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
        print(f"Entered a valid URL: {url}")
        return True
    except ValidationError as e:
        print(f"Entered an invalid URL: {url}")
        return False

def save_to_file(content: str, file_name = TEMP_HTML):
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(content)
