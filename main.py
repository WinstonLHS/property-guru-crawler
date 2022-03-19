from common import TEMP_HTML, TEMP_PROPERTIES_CSV
from extractor import extract_property_from_text
from property import Property
from property_csv_writer import write_csv

file = open(TEMP_HTML, 'r')
text = file.read()
p = extract_property_from_text(text)
properties = [p, p]
write_csv(properties)
