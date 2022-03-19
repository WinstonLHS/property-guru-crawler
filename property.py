from datetime import date


class Property:
    address : str
    sqft : int
    years_Left : float
    year_built : int
    lease_length : int

    def set_lease_length(self, lease_length : int):
        if lease_length < 1:
            raise Exception('expected lease length to be positive.')
        self.lease_length = lease_length

    def set_year_built(self, year : int):
        if year < 1:
            raise Exception('expected year to be > 1')
        self.year_built = year

    def compute_years_left(self):
        if self.lease_length is None or self.lease_length < 1:
            raise Exception('expected lease length to be set.')
        self.years_Left = self.lease_length - (self.year_built - date.today().year)

    def set_size(self, sqft : int):
        self.sqft = sqft

    def set_address(self, address : str):
        self.address = address

