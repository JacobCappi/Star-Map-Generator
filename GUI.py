import tkinter as tk

window = tk.Tk()

#frame for text displayed at top of GUI
text_frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth = 5)

title = tk.Label(
    text="Star Map Generator",
    font = ("Arial", 28),
    fg="blue4",
    master = text_frame
)
title.pack()
instructions = tk.Label(
    text="Enter Latitude, Longitude, and a Date to begin generation.",
    font = ("Arial", 12),
    fg="blue4",
    height=1,
    master = text_frame
)
instructions.pack()
text_frame.pack()

#frames for coordinate entries
coords_frame = tk.Frame(master = window, borderwidth = 5)
lat_frame = tk.Frame(master = coords_frame, borderwidth = 2)
long_frame = tk.Frame(master = coords_frame, borderwidth = 2)

coord_text = tk.Label(
    text="Coordinates",
    font = ("Arial", 20),
    fg="blue4",
    master = coords_frame
)
coord_text.pack()

lat_text = tk.Label(
    text="Latitude",
    fg="blue4",
    master = lat_frame
)
lat_text.pack(side=tk.LEFT)

#entry used to get latitude from user
lat_entry = tk.Entry(
    fg="black",
    width=20,
    master = lat_frame
)
lat_entry.pack(side=tk.RIGHT)

long_text = tk.Label(
    text="Longitude",
    fg="blue4",
    master = long_frame
)
long_text.pack(side=tk.LEFT)

#entry used to get latitude from user
long_entry = tk.Entry(
    fg="black",
    width=20,
    master = long_frame
)
long_entry.pack(side=tk.RIGHT)

lat_frame.pack(side=tk.LEFT)
long_frame.pack(side=tk.RIGHT)
coords_frame.pack()

#frames for date
date_frame = tk.Frame(master = window, borderwidth = 5)
month_frame = tk.Frame(master = date_frame, borderwidth = 2)
day_frame = tk.Frame(master = date_frame, borderwidth = 2)
year_frame = tk.Frame(master = date_frame, borderwidth = 2)

date_text = tk.Label(
    text="Date",
    font = ("Arial", 20),
    fg="blue4",
    master = date_frame
)
date_text.pack()

month_text = tk.Label(
    text="Month",
    fg="blue4",
    master = month_frame
)
month_text.pack(side=tk.LEFT)

#entry used to get month from user
month_entry = tk.Entry(
    fg="black",
    width=20,
    master = month_frame
)
month_entry.pack(side=tk.RIGHT)

day_text = tk.Label(
    text="Day",
    fg="blue4",
    master = day_frame
)
day_text.pack(side=tk.LEFT)

#entry used to get day from user
day_entry = tk.Entry(
    fg="black",
    width=20,
    master = day_frame
)
day_entry.pack(side=tk.RIGHT)

year_text = tk.Label(
    text="Year",
    fg="blue4",
    master = year_frame
)
year_text.pack(side=tk.LEFT)

#entry used to get year from user
year_entry = tk.Entry(
    fg="black",
    width=20,
    master = year_frame
)
year_entry.pack(side=tk.RIGHT)

month_frame.pack(side=tk.LEFT)
day_frame.pack(side=tk.LEFT)
year_frame.pack(side=tk.LEFT)
date_frame.pack()

#frames for time
time_frame = tk.Frame(master = window, borderwidth = 5)
hour_frame = tk.Frame(master = time_frame, borderwidth = 2)
minute_frame = tk.Frame(master = time_frame, borderwidth = 2)

time_text = tk.Label(
    text="Time of Day",
    font = ("Arial", 20),
    fg="blue4",
    master = time_frame
)
time_text.pack()

hour_text = tk.Label(
    text="Hours",
    fg="blue4",
    master = hour_frame
)
hour_text.pack(side=tk.LEFT)

#entry used to get time from user
hour_entry = tk.Entry(
    fg="black",
    width=20,
    master = hour_frame
)
hour_entry.pack(side=tk.LEFT)

minute_text = tk.Label(
    text="Minutes",
    fg="blue4",
    master = minute_frame
)
minute_text.pack(side=tk.LEFT)

#entry used to get time from user
minute_entry = tk.Entry(
    fg="black",
    width=20,
    master = minute_frame
)
minute_entry.pack(side=tk.LEFT)

hour_frame.pack(side=tk.LEFT)
minute_frame.pack(side=tk.LEFT)
time_frame.pack()





#called when button is pressed
def button_pressed(event):
    #read values in entry boxes
    lat = 0.0

    lat = lat_entry.get() #between -90 and 90
    long = long_entry.get() #between -180 and 180
    month = month_entry.get() #between 1 and 12
    day = day_entry.get() #between 1 and 31
    year = year_entry.get() #between 1900 and 2100
    hour = hour_entry.get() #between 1 and 24
    minute = minute_entry.get() #between 1 and 60

    print(lat)

#button
button_frame = tk.Frame(master = window, borderwidth = 15)
button = tk.Button(
    text="Generate Star Map",
    width=20,
    height=3,
    bg="blue4",
    fg="white",
    master = button_frame
)
button.pack()
button_frame.pack()
button.bind("<Button-1>", button_pressed) #bind button to button_pressed()

window.mainloop()