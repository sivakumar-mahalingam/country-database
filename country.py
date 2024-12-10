from .utils import load_country_data

class CountryDatabase:
    def __init__(self):
        self.countries = load_country_data()

    def search_by_name(self, name):
        """
        Search for countries by name (partial match).
        :param name: Partial or full name of the country.
        :return: List of matching countries.
        """
        return [country for country in self.countries if name.lower() in country["CountryName"].lower()]

    def get_by_alpha2_code(self, alpha2):
        """
        Get country details using the Alpha-2 code.
        :param alpha2: The Alpha-2 code of the country.
        :return: Dictionary of country details or None if not found.
        """
        return next((country for country in self.countries if country["Alpha2Code"] == alpha2.upper()), None)

    def get_by_alpha3_code(self, alpha3):
        """
        Get country details using the Alpha-3 code.
        :param alpha3: The Alpha-3 code of the country.
        :return: Dictionary of country details or None if not found.
        """
        return next((country for country in self.countries if country["Alpha3Code"] == alpha3.upper()), None)

    def get_by_continent(self, continent):
        """
        List all countries in a given continent.
        :param continent: Name of the continent.
        :return: List of countries in the continent.
        """
        return [country for country in self.countries if country["Continent"].lower() == continent.lower()]

    def list_all_countries(self):
        """
        List all countries in the database.
        :return: List of all countries.
        """
        return self.countries
