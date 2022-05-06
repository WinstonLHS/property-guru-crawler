from property import Property
from webscraper import extract_property_from_link
from property_csv_writer import PropertiesCsvWriter

file = open('sample_links')
writer = PropertiesCsvWriter()
for link in file:
    try:
        property: Property = extract_property_from_link(link.strip())
    except Exception as e:
        print(f"property couldn't be fetched: {e}")
        continue
    writer.write(property)
