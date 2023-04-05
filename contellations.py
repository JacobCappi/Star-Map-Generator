class Star:
    def __init__(self, star_id, name, coordinates):
        self.star_id = star_id
        self.name = name
        self.coordinates = coordinates
    
    def __str__(self):
        return f"Star ID: {self.star_id}, Name: {self.name}, Coordinates: {self.coordinates}"


class Constellation:
    def __init__(self, name):
        self.name = name
        self.stars = []
    
    def add_star(self, star):
        self.stars.append(star)
    
    def remove_star(self, star_id):
        for star in self.stars:
            if star.star_id == star_id:
                self.stars.remove(star)
    
    def get_star_count(self):
        return len(self.stars)
    
    def get_stars(self):
        return self.stars
    
    def __str__(self):
        return f"Constellation: {self.name}, Star Count: {len(self.stars)}"


# Example usage:

# Create Star objects
star1 = Star(1, "Alpha", (10, 20))
star2 = Star(2, "Beta", (30, 40))
star3 = Star(3, "Gamma", (50, 60))

# Create Constellation object
constellation = Constellation("Orion")

# Add stars to the constellation
constellation.add_star(star1)
constellation.add_star(star2)
constellation.add_star(star3)

# Get the star count and list of stars in the constellation
print(constellation)
print(constellation.get_stars())

# Remove a star from the constellation
constellation.remove_star(2)

# Get the updated star count and list of stars in the constellation
print(constellation)
print(constellation.get_stars())
