import re
from cloudscraper import create_scraper
from django.core.validators import URLValidator
from django.forms import ValidationError

ADDRESS_REGEX = re.compile('<span itemprop="streetAddress">(.+)</.*span')
TEMP_FILE = 'saved_pages/page.html'

def prompt_for_url():
    link = input('please enter the property guru link:')
    return link

def extract_page(link: str):
    if not is_valid_url(link):
        return
    html = fetch_html(link)
    save_to_file(html)
    address = find('address')
    property = Property()
    property.set('address', address)

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

def find(attribute_name: str, file_name = TEMP_FILE):
    with open(file_name, 'r') as file:
        for line in file:
            if (line.__contains__('<span itemprop="streetAddress">')):
                matches = ADDRESS_REGEX.findall(line)
                if (len(matches) != 1):
                    print('found more than 1 match for street address.')
                else:
                    return matches[0]
