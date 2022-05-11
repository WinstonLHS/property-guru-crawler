from io import TextIOWrapper
from common import TEMP_PROPERTIES_CSV
from property import Property

LINE_DELIMITER = '\n'
COLUMN_DELIMITER = '|'
HEADERS: list = COLUMN_DELIMITER.join([
    'address',
    'link',
    'price',
    'floor',
    'years_left',
    'sqft',
])

class PropertiesCsvWriter:
    file_path: str = TEMP_PROPERTIES_CSV
    csv_file: TextIOWrapper

    def __init__(self) -> None:
        self.csv_file = open(self.file_path, 'w', newline=LINE_DELIMITER)
        self.csv_file.close()

    def write(self, property: Property):
        self.csv_file = open(self.file_path, 'a', newline=LINE_DELIMITER)
        if self.csv_file.tell() == 0:
            self.write_headers()
        line = self.property_to_csv_row(property)
        self.csv_file.write(line)
        self.csv_file.write(LINE_DELIMITER)
        self.csv_file.close()

    def write_headers(self):
        self.csv_file.write(HEADERS)
        self.csv_file.write(LINE_DELIMITER)
        self.csv_file.flush()

    def property_to_csv_row(self, property: Property) -> str:
        columns = [
            str(property.address),
            str(property.link),
            str(property.price),
            str(property.floor),
            str(property.years_Left),
            str(property.sqft),
        ]
        return COLUMN_DELIMITER.join(columns)

