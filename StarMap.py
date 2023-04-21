import tkinter as tk
from tkinter import Canvas, Scrollbar
from Star import Star
from Planets import Planet
from MathEquations import MathEquations
from Constellations import Constellations
from MessierObjects import MessierObjects
from PIL import Image, ImageTk, ImageGrab
from datetime import datetime
from datetime import timezone
import math
import csv
import time

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

    
    # TODO: change this to input
    _time = datetime.now(timezone.utc)

    #----

    _equations = MathEquations()

    # get time in format datetime, north and east are bools for if lat and long is E or N
    def __init__(self, lat, long, isNorth, isEast, time, resolution):
        self._lat = lat
        self._long = long
        self._isNorth = isNorth
        self._isEast = isEast
        self._time = time
        self._resolution = resolution

        (self._stars, self._planets) = self.load_star_catalog()

        stars = []
        for star in self._stars:
            az, alt = self._equations.ConvertRAandDecToAziAndAlt(star.ra, star.dec)
            stars.append([star.starId, star.properName, az, alt, star.mag])
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
        #print(self._planets)

        self._moonPhase = self._equations.GetLunarPhase()
        #print(self._moonPhase)

        self._moonCoord = self._equations.GetMoonPosition()
        #print(self._moonCoord)

        constellations = Constellations()
        self._constellations = constellations.ConstellationsList

        messier = MessierObjects()
        messierObjects =  messier.MessierList
        messierList = []

        for num, rah, ram, ras, deh, dem, des, name in messierObjects:
            ra, dec = self._equations.ConvertRAandDecLONGToAziAndAlt(rah, ram, ras, deh, dem, des)
            messierList.append([num, name, ra, dec])
        
        self._messierObjects = messierList
        self._resolution = resolution
        self._zoom_factor = min(resolution[0] / 1920, resolution[1] / 1080)
        
    def zoom_in(self):
        self._zoom_factor * 1.2

    def zoom_out(self):
        self._zoom_factor / 1.2

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

    def save_image(self, canvas, filename):
        print("saving")
        canvas.scale(tk.ALL, 0, 0, 1/1, 1/1)
        ImageGrab.grab(bbox=(
            canvas.winfo_rootx(),
            canvas.winfo_rooty(),
            canvas.winfo_rootx() + canvas.winfo_width(),
            canvas.winfo_rooty() + canvas.winfo_height()
        )).save(filename) 

    def showhide_names(self, canvas, names):
        for name in names:
            state = canvas.itemcget(name, 'state')
            print(state)
            if canvas.itemcget(name, 'state') == 'hidden':            
                canvas.itemconfig(name, state= 'normal')
            elif canvas.itemcget(name, 'state') == '' or canvas.itemcget(name, 'state') == 'normal':
                canvas.itemconfig(name, state= 'hidden')
    
        canvas.update()


    def show_on_screen(self):
        window = tk.Tk()
        window.title("Star Map")
        star_names = []
        planet_names = []
                
        
        
        # Create a frame to hold the canvas and scrollbars
        frame = tk.Frame(window)
        frame.pack(fill=tk.BOTH, expand=tk.YES)

        # Create a canvas widget with a black background
        canvas = Canvas(frame, width=self._resolution[0], height=self._resolution[1], bg="black")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # Create vertical and horizontal scrollbars
        vscrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        hscrollbar = Scrollbar(window, orient=tk.HORIZONTAL, command=canvas.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        canvas.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))

        def on_mousewheel(event):
            """Zoom in/out on mouse wheel scroll."""
            if event.delta > 0:
                for _ in range(abs(event.delta) // 120):
                    self.zoom_in()
                canvas.scale(tk.ALL, event.x, event.y, self._zoom_factor, self._zoom_factor)
            else:
                for _ in range(abs(event.delta) // 120):
                    self.zoom_out()
                canvas.scale(tk.ALL, event.x, event.y, 1/self._zoom_factor, 1/self._zoom_factor)

        canvas.bind("<MouseWheel>", on_mousewheel)

         
        starsToStarID = {}

        # Add stars to the canvas
        for star in self._stars:
            x = math.cos(star[3]) * math.sin(star[2])
            y = math.cos(star[3]) * math.cos(star[2])
            if -0.5 < x < 0.5 and -0.5 < y < 0.5: 
                
                width = 15 - star[4] * 2.5
                height = 30 - star[4] * 5
                #print(star)
                x *= 4000
                y *= 4000

                x += 810
                y += 540
                starsToStarID[star[0]] = (x, y)
                # After init, list of all stars [starid, starname, az, alt]

                if (star[1]!= ' '):
                    canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#ADD8E6")
                    text = canvas.create_text(x,y+(width/2)+5, text=star[1], fill="#ADD8E6")
                    star_names.append(text)
                else:
                    canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="white")
                    
            
        
        
        for constellation in self._constellations:
            print(constellation)
            if constellation.star in starsToStarID:
                x,y = starsToStarID[constellation.star]
                img = constellation.image
                canvas.create_image(x, y, image= img, anchor = 'nw')
        
        for planet in self._planets:
            x = math.cos(planet[2]) * math.sin(planet[1])
            y = math.cos(planet[2]) * math.cos(planet[1])
            if -0.5 < x < 0.5 and -0.5 < y < 0.5: 
                width = 35 - .001 * 2.5
                #print(star)
                x *= 4000
                y *= 4000

                x += 810
                y += 540
                if (planet[0] != "Earth/Sun"):
                    canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#FFFF00")
                    planet_names.append(canvas.create_text(x,y+(width/2)+5, text=planet[0], fill="#FFFF00"))

        width = 15 - .25 * 2.5
        x = math.cos(self._moonCoord[1]) * math.sin(self._moonCoord[0])
        y = math.cos(self._moonCoord[1]) * math.cos(self._moonCoord[0])
        if -0.5 < x < 0.5 and -0.5 < y < 0.5: 
            x *= 4000
            y *= 4000
            canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#C8A2C8")
            canvas.create_text(x,y+(width/2)+5, text="Moon", fill="#C8A2C8")
        # Configure the canvas to scroll
        canvas.configure(scrollregion=canvas.bbox(tk.ALL))
        


        # Add a button to the top of the window for saving images
        button = tk.Button(window, text="Save as Jpeg", command = lambda: self.save_image(canvas, "StarMap.jpg"))
        button.place(relx=0, rely=0, anchor="nw")
        
        # Add a button to the top of the window for show/hiding star names
        button1 = tk.Button(window, text="show/hide star names", command = lambda: self.showhide_names(canvas, star_names))
        button1.place(relx=0.1, rely=0, anchor="nw")
        
        # Add a button to the top of the window for show/hiding planet names
        button2 = tk.Button(window, text="show/hide planet names", command = lambda: self.showhide_names(canvas, planet_names))
        button2.place(relx=0.3, rely=0, anchor="nw")

        # Add a button to the top of the window for show/hiding constellation names
        button3 = tk.Button(window, text="show/hide constellation names", command = lambda: self.showhide_names(canvas, planet_names)) #needs to be constellation names
        button3.place(relx=0.5, rely=0, anchor="nw")


        window.attributes('-fullscreen', True)
        window.attributes('-fullscreen', False)
        window.attributes('-topmost', True)
        # Show the window
        window.mainloop()

# Create a main function to run the program
def main():
    resolution = (800, 600)
    star_map = StarMap(resolution)
    star_map.show_on_screen()

if __name__ == '__main__':
    main()


    """
    
    # define the button dimensions and position
        button_width = 100
        button_height = 50
        button_x = 200
        button_y = 200

    # create the button rectangle
        button_rect = canvas.create_rectangle(button_x, button_y, button_x + button_width, button_y + button_height, fill="blue")
        # create the button text
        button_text = canvas.create_text(button_x + button_width/2, button_y + button_height/2, text="Save Image", fill="white")
        def button_click():
            print("Button clicked!")
            self.save_image( canvas, "starmap.jpeg")
        
        # bind the button click event to the button_click function
        canvas.tag_bind(button_rect, "<Button-1>", lambda event: button_click())
    
    """