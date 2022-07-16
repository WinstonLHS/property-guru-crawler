# Property Guru Crawler

A python app that extracts useful information from a property guru link.

## Extracted Information

The following class represents the extracted information on each property listing visited.

```python
class Property:
    address : str
    link : str
    price : float
    floor : str
    sqft : float
    years_Left : float
    year_built : int
    lease_length : int
```

1. address - the local address of the property.
2. link - the full length property guru listing url
3. price - listing price in dollars
4. floor - high, medium, low floors
5. sqft - the property's floor size in squarefeet
6. years_left - number of years left on the lease to the property
7. year_built - Gregarian calendar year that this property was built
8. lease_length - length (in years) of the lease on this property

## Setup

To install this project's depedencies, run the following command at the root of this repository:

Linux/MacOS
> python -m pip install -r requirements.txt

Windows
> py -m pip install -r requirements.txt
OR
> pip install -r requirements.txt

## Usage

run the cli with the command:

Linux/MacOS
> python main.py

Windows
> py main.py
