from webscraper import fetch_html
from webscraper import save_to_file
from webscraper import find
from webscraper import prompt_for_url
from webscraper import extract_property

class Cli:
    url : str

    def start(self):
        link = prompt_for_url()
        extract_property(link)
