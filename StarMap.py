import tkinter as tk
from Star import Star

from PIL import Image, ImageTk
import csv
import math
class StarMap:
    def __init__(self, observer_location, date_time):
        #self.observer_location = observer_location
        #self.date_time = date_time
        self.star_catalog = self.load_star_catalog()
        #self.planets = self.get_planets_location()
        #self.moon = self.get_moon_location()
        #self.messier_objects = self.get_messier_objects_location()

    # Load the star catalog data from the Yale Star Catalog
    # Return the data as a dictionary with star names as keys and locations as values
    def load_star_catalog(self):
        allStarsfromFile = []

        with open('hyg.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip the first row
            for row in reader:
                if all(val.strip() == '' for val in row):
                    break  # exit loop if row is completely empty
                if float(row[10]) <= 6:
                    allStarsfromFile.append(Star(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12], row[13]))

        self.stars = allStarsfromFile

        print (vars(allStarsfromFile[1]))

        return self.stars

    def get_planets_location(self):
        # Calculate the location of all major planets (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune)
        # Return the location data as a dictionary with planet names as keys and locations as values
        # ...
        return self.planets
    def get_moon_location(self):
        # Calculate the location and phase of the moon
        # Return the location data as a tuple (location, phase)
        # ...
        return self.moon
    def get_messier_objects_location(self):
        # Calculate the location of all the Messier deep space objects
        # Return the location data as a dictionary with object names as keys and locations as values
        # ...
        return self.messier_objects
    def save_image(self, image, filename):
        # Generate the star map image and save it to disk in the JPEG format
        # ...
        image.save(filename, 'JPEG')
        return image

    def show_on_screen(self, star_map_image):
        window = tk.Tk()
        window.title("Star Map")

        # Open the star map image
        image = Image.open(star_map_image)
        image = image.resize((800, 600), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        # Display the image in a scrollable window
        canvas = tk.Canvas(window, width=800, height=600)
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.config(scrollregion=canvas.bbox(tk.ALL))

        # Add scrollbars to the window
        scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Show the window
        window.mainloop()

# Create a main function to run the program
def main():
    # Ask the user to enter the observer location, date and time
    observer_location = input("Enter observer location (latitude and longitude in degrees and minutes): ")
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")

    # Create an instance of the StarMap class
    star_map = StarMap(observer_location, date_time)

    # Show the star map on screen
    #star_map.show_on_screen()

    # Ask the user if they want to save the image to disk
    #save_image = input("Do you want to save the image to disk? (yes/no): ")
    #if save_image.lower() == 'yes':
        #filename = input("Enter filename: ")
        #star_map.save_image(filename)

if __name__ == '__main__':
    main()
