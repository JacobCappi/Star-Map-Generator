import tkinter as tk
from tkinter import Canvas, Scrollbar
from Star import Star
from Planets import Planet
from MathEquations import MathEquations
from Constellations import Constellations
from MessierObjects import MessierObjects
from PIL import Image, ImageTk
import datetime
from datetime import timezone
import math
import csv
import tkinter.filedialog as fd
from PIL import ImageGrab

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
    _longt = 0

    _isNorth = True
    _isEast = False

    
    # TODO: change this to input
    #_time = datetime.now(timezone.utc)

    #----

    _equations = MathEquations()

    # get time in format datetime, north and east are bools for if lat and long is E or N
    def __init__(self, lat, longt, isNorth, isEast, time, resolution):
        self._lat = lat
        self._longt = longt
        self._isNorth = isNorth
        self._isEast = isEast
        self._time = time
        self._resolution = resolution

        (self._stars, self._planets) = self.load_star_catalog()

        stars = []
        for star in self._stars:
            if (((star.ra *7.5)-90) > lat - 45) and (((star.ra * 7.5) - 90) < lat + 45 ) and (star.dec < longt + 45) and (star.dec > longt - 45):
#               ^^^ generates field of view by converting RA to +/- 90 degrees and defining a 90 degree viewing range in both RA and Dec
#                   based on the viewer's position
                az, alt = self._equations.ConvertRAandDecToAziAndAlt(star.ra, star.dec)
                stars.append([star.starId, star.properName, az, alt, star.mag])
                if (len(star.properName) > 1):
                    print(star.properName)
            
        self._stars = stars

        self._equations.InitMathEquations(self._time, self._planets, self._lat, self._longt, self._isNorth, self._isEast)

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

    def show_on_screen(self):
        window = tk.Tk()
        window.title("Star Map")

        # Create a frame for the checkbox and label
        panel = tk.Frame(window)
        panel.pack(side=tk.LEFT, fill=tk.Y, pady=5)

        # Create a label to display "Show Labels" or "Hide Labels"
        label = tk.Label(panel, text="Show Labels")
        label.pack(side=tk.TOP, pady=5)

        # Create a BooleanVar object to hold the checkbox value
        show_labels = tk.BooleanVar()
        show_labels.set(True)  # set default value to True

        # Create a Checkbutton widget
        checkbutton = tk.Checkbutton(panel, variable=show_labels, text="")
        checkbutton.pack(side=tk.TOP)

        # Create a frame to hold the canvas and scrollbars
        frame = tk.Frame(window)
        frame.pack(fill=tk.BOTH, expand=tk.YES)

        # Create a function to generate the JPEG image
        def generate_jpeg():
            # get the coordinates of the window
            x = frame.winfo_rootx()
            y = frame.winfo_rooty()
            width = frame.winfo_width()
            height = frame.winfo_height()

            image = ImageGrab.grab((x, y, x+width, y+height))

            # Open a file dialog to save the JPEG image
            filename = fd.asksaveasfilename(defaultextension=".jpg")
            
            # Save the image as a JPEG file
            image.save(filename)

        button = tk.Button(panel, text="Generate JPEG", command=generate_jpeg)
        button.pack(pady=10)

        # Create a canvas widget with a black background
        canvas = Canvas(frame, width=self._resolution[0], height=self._resolution[1], bg="black")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # Create vertical and horizontal scrollbars
        vscrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        hscrollbar = Scrollbar(window, orient=tk.HORIZONTAL, command=canvas.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Define a function to show or hide the labels
        def toggle_labels(*args):
            state = "normal" if show_labels.get() else "hidden"
            for item in canvas.find_all():
                if canvas.type(item) == "text":
                    canvas.itemconfigure(item, state=state)

        # Bind the function to the BooleanVar object
        show_labels.trace_add("write", toggle_labels)

        def on_canvas_click(event):
            print("Clicked at x =", event.x, "y =", event.y)

        def on_mousewheel(event):
            """Zoom in/out on mouse wheel scroll."""
            if event.delta <= 0:
                for _ in range(abs(event.delta) // 120):
                    self.zoom_in()
                canvas.scale(tk.ALL, event.x, event.y, self._zoom_factor, self._zoom_factor)          
            else:
                for _ in range(abs(event.delta) // 120):
                    self.zoom_out()
                canvas.scale(tk.ALL, event.x, event.y, 1/self._zoom_factor, 1/self._zoom_factor)

        canvas.bind("<MouseWheel>", on_mousewheel)         
        
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))
        # Bind the left mouse button click event to the canvas
        canvas.bind("<Button-1>", on_canvas_click)

        starsToStarID = {}
        # Add stars to the canvas
        for star in self._stars:
            x = math.cos(star[3]) * math.sin(star[2])
            y = math.cos(star[3]) * math.cos(star[2])

            width = 15 - star[4] * 2.5
            height = 30 - star[4] * 5
            print(star)
            x *= 2000
            y *= 2000

            x += 810
            y += 540

            starsToStarID[star[0]] = [x, y]

            if ((star[3] > 0) and (star[3]<90)):
                # After init, list of all stars [starid, starname, az, alt]
                if (star[1]!= ' '):
                    canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#ADD8E6")
                    canvas.create_text(x,y+(width/2)+5, text=star[1], fill="#ADD8E6")
                else:
                    canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="white")

        #Constellation connection algorithm
        for constellation in self._constellations:
            for key in constellation.stars:
                for id in constellation.stars[key]:
                    print (key, id)
                    try:
                        canvas.create_line(starsToStarID[key][0], starsToStarID[key][1], starsToStarID[id][0], starsToStarID[id][1], fill="white")
                    except:
                        pass


        for planet in self._planets:
            x = math.cos(planet[2]) * math.sin(planet[1])
            y = math.cos(planet[2]) * math.cos(planet[1])
            
            width = 15 - .001 * 2.5
            #print(star)
            x *= 2000
            y *= 2000

            x += 810
            y += 540
            if (planet[0] != "Earth/Sun"):
                canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#FFFF00")
                canvas.create_text(x,y+(width/2)+5, text=planet[0], fill="#FFFF00")

        width = 15 - .25 * 2.5
        x = math.cos(self._moonCoord[1]) * math.sin(self._moonCoord[0])
        y = math.cos(self._moonCoord[1]) * math.cos(self._moonCoord[0])
        x *= 2000
        y *= 2000
        canvas.create_oval(x-(width/2), y-(width/2), x+(width/2), y+(width/2), fill="#C8A2C8")
        canvas.create_text(x,y+(width/2)+5, text="Moon", fill="red")
        # Configure the canvas to scroll
        canvas.configure(scrollregion=canvas.bbox(tk.ALL))

        rad = float(math.pi/180)
        x,y = 150.5 * rad, 32.7 * rad
        x *= 2000
        y *= 2000
        #canvas.create_text(x,y+(width/2)+5, text="Alpheratz", fill="red")
        
        canvas.scale(tk.ALL, self._resolution[0] / 2, self._resolution[1] / 2.25, self._resolution[1] / 4500, self._resolution[1] / 4500)
        # Show the window
        window.mainloop()

# Create a main function to run the program
def main():
    resolution = (1024, 768)
    star_map = StarMap(1, 1, True, False, datetime.datetime(2000, 6, 15, 15, 15, tzinfo=datetime.timezone.utc), resolution)
    star_map.show_on_screen()

if __name__ == '__main__':
    main()
