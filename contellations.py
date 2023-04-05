class Constellation:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        self.show_labels = True
    
    def add_star(self, star):
        self.stars.append(star)
    
    def remove_star(self, star):
        if star in self.stars:
            self.stars.remove(star)
    
    def get_star_count(self):
        return len(self.stars)
    
    def get_stars(self):
        return self.stars
    
    def toggle_labels(self):
        self.show_labels = not self.show_labels
    
    def draw_constellation(self):
        # Method to draw the constellation by connecting stars with lines
        # This is a placeholder, actual implementation will depend on the specific graphical library or framework used
        
        if self.show_labels:
            print(f"Constellation: {self.name}")
        else:
            print("Constellation: Hidden")
        
        # Draw lines between stars
        for i in range(len(self.stars)-1):
            print(f"Draw line from {self.stars[i]} to {self.stars[i+1]}")
        
    def __str__(self):
        return f"Constellation: {self.name}, Stars: {', '.join(self.stars)}, Show Labels: {self.show_labels}"
