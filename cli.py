from django.core.validators import URLValidator
from django.forms import ValidationError

class Cli:
    url : str
    def prompt_user(self):
        perhaps_a_link = input('please enter the property guru link:')
        Cli.check_url(perhaps_a_link)

    @staticmethod
    def check_url(url: str):
        validate = URLValidator()
        try:
            validate(url)
            print("Entered a valid URL.")
        except ValidationError as e:
            print("Entered an invalid URL")