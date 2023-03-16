class City:

    def __init__(self, city_name, country, visited = False, id = None):
        self.city_name = city_name
        self.country = country
        self.visited = visited
        self.id = id


# This function defines a method which takes in 
# the falsy boolean from visited and changes it to truthy.

    def mark_as_visited(self):
        self.visited = True