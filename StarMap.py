import tkinter as tk
from Star import Star
from PIL import Image, ImageTk
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import pandas as pd
import math

class StarMap:
    def __init__(self, observer_location, date_time):
        #self.observer_location = observer_location
        #self.date_time = date_time
        self.stars = self.load_star_catalog()
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

        print (vars(allStarsfromFile[5]))
        #print(len(allStarsfromFile))
        return allStarsfromFile

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
        image = image.resize((800, 600))
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
    date_time = 'YYYY-MM-DD HH:MM'
    while True:

        # get user input for latitude in degrees, minutes, seconds
        lat_deg = int(input("Enter your latitude in degrees: "))
        lat_min = int(input("Enter your latitude in minutes: "))
        lat_sec = float(input("Enter your latitude in seconds: "))

        # convert latitude to decimal degrees
        lat = lat_deg + lat_min / 60 + lat_sec / 3600

        # get user input for longitude in degrees, minutes, seconds
        lon_deg = int(input("Enter your longitude in degrees: "))
        lon_min = int(input("Enter your longitude in minutes: "))
        lon_sec = float(input("Enter your longitude in seconds: "))

        # convert longitude to decimal degrees
        lon = lon_deg + lon_min / 60 + lon_sec / 3600

        #if len(input_variables) > 4:
            #print("ERROR: More than 4 inputs (Degrees, minutes, seconds, direction) recognized in input, try again.")
           # continue
        #print("degrees: " + degrees + " minutes: " + minutes + " seconds: " + seconds + " direction: " + direction)
        break
    while True:
        date_time = input("Enter date and time in the format 'YYYY-MM-DD HH:MM': ")
        input_variables2 = date_time.split()

        if len(input_variables2) > 2:
            print("ERROR: More than 2 inputs (Date, Time) recognized in input, try again.")
            continue

        date = input_variables2[0]
        time = input_variables2[1]

        try:
            # Parse the input string into a datetime object
            datetime_object = datetime.strptime(date_time, '%Y-%m-%d %H:%M')

            # Check if the datetime object is valid
            if 1900 < datetime_object.year < 2100:
                print("Date: " + date + " Time: " + time)
            else:
                print("Invalid datetime")
                continue
        except ValueError:
            print("Invalid datetime format")
            continue
        break

    # Create an instance of the StarMap class
    #star_map = StarMap(observer_location, date_time)

    # Show the star map on screen
    #star_map.show_on_screen("starmapTest.png")

    # Ask the user if they want to save the image to disk
    #save_image = input("Do you want to save the image to disk? (yes/no): ")
    #if save_image.lower() == 'yes':
        #filename = input("Enter filename: ")
        #star_map.save_image(filename)

    # read in the star data from a CSV file
    star_data = pd.read_csv('hyg.csv')

    # create an EarthLocation object with the user's coordinates
    user_location = EarthLocation(lat=lat, lon=lon)

    # create a Time object for the current time
    time_custom = Time(date_time, format='iso', scale='utc')

    # create a SkyCoord object for each star in the star_data dataframe
    star_coords = SkyCoord(ra=star_data['RA'], dec=star_data['Dec'], unit='deg')

    # transform the star coordinates to the user's location and current time
    aa_frame = AltAz(location=user_location, obstime=time_custom)
    star_aa = star_coords.transform_to(aa_frame)

    # filter the stars to only show those with magnitude less than or equal to 6
    mask = star_data['Mag'] <= 6
    visible_stars = star_data[mask]

    # plot the visible stars on a scatter plot
    plt.scatter(visible_stars['RA'], visible_stars['Dec'], s=5)
    plt.xlabel('Right Ascension (degrees)')
    plt.ylabel('Declination (degrees)')
    plt.title('All Stars at {}, {}'.format(lat, lon))
    plt.show()

if __name__ == '__main__':
    main()
