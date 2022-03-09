import cloudscraper

def fetch_html(url: str):
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'android',
            'desktop': True
        })
    return scraper.get(url).text

html_content = fetch_html('https://www.propertyguru.com.sg/listing/hdb-for-sale-164-bukit-batok-street-11-23824303')

with open('page.html', 'w') as html_file:
    html_file.write(html_content)
