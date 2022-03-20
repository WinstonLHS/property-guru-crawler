from webscraper import extract_property_from_link
from property_csv_writer import write_csv

file = open('sample_links')
properties = []
for link in file:
    property = extract_property_from_link(link.strip())
    properties.append(property)

write_csv(properties)
