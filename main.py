from property import Property
from webscraper import extract_property_from_link
from property_csv_writer import PropertiesCsvWriter

file = open('sample_links')
writer = PropertiesCsvWriter()
for link in file:
    property: Property = extract_property_from_link(link.strip())
    writer.write(property)
