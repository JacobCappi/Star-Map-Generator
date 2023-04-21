from tkinter import *
from PIL import Image, ImageTk

class Constellation:
    def __init__(self, name, star, image):
        self.name = name
        self.star = star
        self.image = image

class Constellations:

    @property
    def ConstellationsList(self):
        return self._constellationList
    
    @ConstellationsList.setter
    def ConstellationsList(self, value):
        self._constellationList = value

    def __init__(self):
        self._getAllConstellations()

    def _getAllConstellations(self):
        constellationList = []

        image_paths = {
            "Andromeda" : 'constellations/andromeda.png',
            "Aquarius" : 'constellations/aquarius.png',
            "Aries" : 'constellations/aries.png',
            "Taurus": 'constellations/taurus.png',
            "Gemini": 'constellations/gemini.png',
            "Pisces": 'constellations/pisces.png',
            "Capricornus":'constellations/capricornus.png',
            "Sagittarius":'constellations/sagittarius.png',
            "Scorpio":'constellations/scorpio.png',
            "Libra":'constellations/libra.png',
            "Virgo":'constellations/virgo.png',
            "Leo":'constellations/leo.png',
            "Cancer":'constellations/cancer.png',
            "Cygnus":'constellations/cygnus.png',
            "Auriga":'constellations/auriga.png',
            "Bootes":'constellations/bootes.png',
            "Centaurus":'constellations/centaurus.png',
            "Orion":'constellations/orion.png',
            "Hercules":'constellations/hercules.png',
            "Aquila":'constellations/aquila.png',
            "CanisMaj":'constellations/canisMaj.png',
            "CanisMin":'constellations/canisMin.png',
            "Crux":'constellations/crux.png',
            "Hydra":'constellations/hydra.png',
            "Lyra":'constellations/lyra.png',
            "Pegasus":'constellations/pegasus.png',
            "Perseus":'constellations/perseus.png',
            "Cassiopeia":'constellations/casiopea.png',
            "Cepheus":'constellations/cepheus.png',
            "Draco":'constellations/draco.png',
            "UrsaMaj":'constellations/ursaMaj.png',
            "UrsaMin":'constellations/ursaMin.png'
        }

        image_stars= {
            "Perseus": 50098,
            "Pegasus": 79533,
            "Lyra": 65795,
            "Hydra": 50094,
            "Crux": 45767,
            "CanisMin": 27267,
            "CanisMaj": 26214,
            "Aquila": 67320,
            "Hercules": 57888,
            "Orion": 17947,
            "Cygnus": 74084,
            "Centaurus": 51926,
            "Bootes": 49140,
            "Auriga": 18021,
            "Cassiopeia": 544,
            "Cepheus": 76423,
            "Draco": 41542,
            "UrsaMaj": 49038,
            "UrsaMin": 8222,
            "Pisces": 3909,
            "Capricornus": 72769,
            "Sagittarius": 67811,
            "Scorpio": 61677,
            "Libra": 53308,
            "Virgo": 52290,
            "Leo": 35524,
            "Cancer": 31816,
            "Gemini": 27698,
            "Taurus": 18796,
            "Aries": 9257,
            "Aquarius": 74474,
            "Andromeda": 2183
        }

        photo_images = {}

        # Load each image and create a PhotoImage instance for it
        for key, value in image_paths.items():
            path = value

            if path in photo_images:
                tk_image = photo_images[path]
            else:
                image = Image.open(path)
                rImage = image.resize((250, 250))
                
                tk_image = ImageTk.PhotoImage(rImage)
                photo_images[path] = tk_image

            constellation = Constellation(key, image_stars[key], tk_image)
            constellationList.append(constellation)

        # Return the list of constellations
        self.ConstellationsList = constellationList
        return constellationList

                
