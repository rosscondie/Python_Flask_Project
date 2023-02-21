class Country:
    def __init__(self, country_name, country_continent, country_population, country_language, id = None):
        self.country_name = country_name
        self.country_continent = country_continent
        self.country_population = country_population
        self.country_language = country_language
        self.id = id

    def mark_as_visited(self):
        self.visited = True

    def get_population(self):
        short_form_population = self.country_population / 1000000 
        if short_form_population.is_integer():
            short_form_population = int(short_form_population)
        return f"{short_form_population} Million"