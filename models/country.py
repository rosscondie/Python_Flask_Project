class Country:
    def __init__(self, country_name, country_continent, country_population, country_language, id = None):
        self.country_name = country_name
        self.country_continent = country_continent
        self.country_population = country_population
        self.country_language = country_language
        self.id = id

    
    # def get_population(self, population):
    #     return f"{float(population)}"