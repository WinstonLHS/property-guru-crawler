from property import Property
from common import TEMP_PROPERTIES_CSV

LINE_DELIMITER = '\n'
COLUMN_DELIMITER = '|'
HEADERS : list = COLUMN_DELIMITER.join([
    'address',
    'link',
    'price',
    'floor',
    'years_left',
    'sqft',
])


def property_to_str(p : Property) -> str:
    columns = [
        str(p.address),
        str(p.link),
        str(p.price),
        str(p.floor),
        str(p.years_Left),
        str(p.sqft),
    ]
    return COLUMN_DELIMITER.join(columns)

def write_csv(properties : list):
    csv_file = open(TEMP_PROPERTIES_CSV, 'w', newline=LINE_DELIMITER)
    csv_file.write(HEADERS)
    csv_file.write(LINE_DELIMITER)
    for p in properties:
        line = property_to_str(p)
        csv_file.write(line)
        csv_file.write(LINE_DELIMITER)
        csv_file.flush()
    csv_file.close()