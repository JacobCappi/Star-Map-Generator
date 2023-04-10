import tkinter as tk
from Star import Star
from Planets import Planet
from MathEquations import MathEquations
from Constellations import Constellations
from MessierObjects import MessierObjects
from PIL import Image, ImageTk
from datetime import datetime
from datetime import timezone
import csv
import time
from astropy.coordinates import SkyCoord, AltAz, EarthLocation
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord, AltAz
from astropy.time import Time
import matplotlib.pyplot as plt
import math

class StarMap:
    # TO map (UI) : az N:0, E:90, S:180, W:270
    #               alt: 90 : zenith, 0 horizon

    # After init, list of all stars [starid, starname, az, alt]
    _stars = []

    # After init, this has all constelations for UI. See that file for more info
    _constellations = []
    
    # after init, will hold list of [planetName, Az, Alt]. That should be all that's needed in UI
    _planets = []

    # based on the enum I got
    _moonPhase = None

    # az and Alt [az, alt]
    _moonCoord = []

    # the objects [num, name, az, alt]
    _messierObjects = []

    # --- These, set these values from UI
    _lat = 0
    _long = 0

    _isNorth = True
    _isEast = False

    _location = 0
    _elv = 0
    
    # TODO: change this to input
    _time = datetime.now(timezone.utc)

    #----

    _equations = MathEquations()

    # get time in format datetime, north and east are bools for if lat and long is E or N
    def __init__(self, lat = 0, long = 0, isNorth = True, isEast = False, time = datetime.now(timezone.utc)):
        self._lat = lat
        self._long = long
        self._isNorth = isNorth
        self._isEast = isEast

        _time = datetime.now(timezone.utc)

        (self._stars, self._planets) = self.load_star_catalog()

        stars = []
        for star in self._stars:
            az, alt = self._equations.ConvertRAandDecToAziAndAlt(star.ra, star.dec)
            stars.append([star.starId, star.properName, az, alt])
            if (len(star.properName) > 1):
                print(star.properName)
        self._stars = stars

        self._equations.InitMathEquations(self._time, self._planets, self._lat, self._long, self._isNorth, self._isEast)

        self._planets = self._equations.GetPlanetsRAandD()

        planetAzAlt = []

        for planet in self._planets:
            (az, alt) = self._equations.ConvertRAandDecToAziAndAlt(planet[1], planet[2])
            planetAzAlt.append([planet[0], az, alt])
        
        self._planets = planetAzAlt
        print(self._planets)

        self._moonPhase = self._equations.GetLunarPhase()
        print(self._moonPhase)

        self._moonCoord = self._equations.GetMoonPosition()
        print(self._moonCoord)

        constellations = Constellations()
        self._constellations = constellations.ConstellationsList

        messier = MessierObjects()
        messierObjects =  messier.MessierList
        messierList = []

        for num, rah, ram, ras, deh, dem, des, name in messierObjects:
            ra, dec = self._equations.ConvertRAandDecLONGToAziAndAlt(rah, ram, ras, deh, dem, des)
            messierList.append([num, name, ra, dec])
        
        self._messierObjects = messierList


    # Load the star catalog data from the Yale Star Catalog
    # Return the data as a dictionary with star names as keys and locations as values
    def load_star_catalog(self):
        allStarsfromFile = []
        allPlanetsfromFile = []

        with open('hyg.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip the first row
            for row in reader:
                if all(val.strip() == '' for val in row):
                    break  # exit loop if row is completely empty
                if float(row[10]) <= 6:
                    allStarsfromFile.append(Star(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12], row[13]))

        with open('Planets.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip the first row
            for row in reader:
                if all(val.strip() == '' for val in row):
                    break  # exit loop if row is completely empty
                allPlanetsfromFile.append(Planet(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

        return allStarsfromFile, allPlanetsfromFile


    def printPlanets(self):
        for planet in self._planets:
            print(planet.ToString())
                

    def printStars(self):
        print(self._stars)

    def save_image(self, image, filename):
        # Generate the star map image and save it to disk in the JPEG format
        # ...
        image.save(filename, 'JPEG')
        return image

    def show_on_screen(self):
        window = tk.Tk()
        window.title("Star Map")
        # Create a canvas widget with a white background
        canvas = tk.Canvas(window, width=1920, height=1080, bg="black")
        canvas.pack()

        for star in self._stars:
            x = math.cos(star[3]) * math.sin(star[2])
            y = math.cos(star[3]) * math.cos(star[2])
            print(x, y)
            x *= 600
            y *= 600

            x += 810
            y += 540

    # After init, list of all stars [starid, starname, az, alt]
            canvas.create_oval(x, y, x+1, y+1, fill="white")
        # Show the window
        window.mainloop() 
        
    def drawstars(self):

        starmap = tk.Canvas(width=1920, height=1080)
        starmap.config(scrollregion=(0, 0, 1920, 1080)) # make it scrollable

        scrollbar = tk.Scrollbar(starmap, orient=tk.VERTICAL)  # Add a scrollbar to the canvas
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=starmap.yview)
        scrollbar2 = tk.Scrollbar(starmap, orient=tk.HORIZONTAL)  # Add a scrollbar to the canvas
        scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar2.config(command=starmap.yview)

        starmap.config(yscrollcommand=scrollbar.set)
        starmap.config(xscrollcommand=scrollbar2.set)

        # Add an image to the canvas
        image = tk.PhotoImage(file="image.png")
        starmap.create_image(0, 0, anchor=tk.NW, image=image)

        # Display the canvas
        starmap.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        canvas_width = 1920
        canvas_height = 1080

        # define the range of x and y coordinates
        x_min = -1
        x_max = 1
        y_min = -1
        y_max = 1

        # calculate the scaling factors
        x_scale = canvas_width / (x_max - x_min)
        y_scale = canvas_height / (y_max - y_min)

        
        
        
        # After init, list of all stars [starid, starname, az, alt]
        self._location = EarthLocation.from_geodetic(self._long, self._lat, self._elv*u.m)
        print(self._location)
        for star in self._stars:
            print(star)
            #azi, alti = self._equations.ConvertRAandDecToAziAndAlt(star.ra, star.dec)
             
            coord = SkyCoord(unit = "deg", alt=star[3], az=star[2], frame=AltAz(obstime=self._time, location=self._location))
            x = coord.cartesian.x.value
            y = coord.cartesian.y.value
            print (x,y)
            x_scaled = (x - x_min) * x_scale
            y_scaled = (y - y_min) * y_scale
            # plot the star on the canvas
            starmap.create_oval(y_scaled - 2, x_scaled - 2, y_scaled +  2, x_scaled + 2, fill="white")
       
        
            
        
        # Show the window
        starmap.mainloop()

# Create a main function to run the program
def main():
    star_map = StarMap()
    star_map.load_star_catalog()
    star_map.show_on_screen()

    

if __name__ == '__main__':
    main()
