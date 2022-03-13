from webcrawler import fetch_html
from webcrawler import save_to_file
from webcrawler import find
from webcrawler import prompt_for_url
from webcrawler import extract_property

class Cli:
    url : str

    def start(self):
        link = prompt_for_url()
        extract_property(link)
