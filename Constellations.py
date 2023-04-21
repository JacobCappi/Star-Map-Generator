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

        




        # Creating Andromeda constellation
        image = ImageTk.PhotoImage(Image.open('constellations/andromeda.png'))
        
        andromeda = Constellation("Andromeda", 2183, image)
        constellationList.append(andromeda)
        
        # Creating Aquarius constellation
        image = ImageTk.PhotoImage(Image.open('constellations/aquarius.png'))
        print(image)
        aquarius = Constellation("Aquarius", 74474, image)
        constellationList.append(aquarius)

        # Creating Aries constellation
        image = ImageTk.PhotoImage(Image.open('constellations/aries.png'))
        aries = Constellation("Aries", 9257, image)
        constellationList.append(aries)

        # Creating Taurus constellation
        image = ImageTk.PhotoImage(Image.open('constellations/taurus.png'))
        taurus = Constellation("Taurus", 18796, image)
        constellationList.append(taurus)

        # Creating Gemini constellation
        image = ImageTk.PhotoImage(Image.open('constellations/gemini.png'))
        gemini = Constellation("Gemini", 27698, image)
        constellationList.append(gemini)

        # Creating Cancer constellation
        image = ImageTk.PhotoImage(Image.open('constellations/cancer.png'))
        cancer = Constellation("Cancer", 31816, image)
        constellationList.append(cancer)

        # Creating Leo constellation
        image = ImageTk.PhotoImage(Image.open('constellations/leo.png'))
        leo = Constellation("Leo", 35524, image)
        constellationList.append(leo)

        
        image = ImageTk.PhotoImage(Image.open('constellations/virgo.png'))
        Virgo = Constellation("Virgo", 52290, image)
        constellationList.append(Virgo)

        image = ImageTk.PhotoImage(Image.open('constellations/libra.png'))
        Libra = Constellation("Libra", 53308, image)
        constellationList.append(Libra)

        image = ImageTk.PhotoImage(Image.open('constellations/scorpio.png'))
        Scorpio = Constellation("Scorpio", 61677, image)
        constellationList.append(Scorpio)

        image = ImageTk.PhotoImage(Image.open('constellations/sagittarius.png'))
        Sagittarius = Constellation("Sagittarius", 67811, image)
        constellationList.append(Sagittarius)

        image = ImageTk.PhotoImage(Image.open('constellations/capricornus.png'))
        Capricornus = Constellation("Capricornus", 72769, image)
        constellationList.append(Capricornus)


        image = ImageTk.PhotoImage(Image.open('constellations/pisces.png'))
        Pisces = Constellation("Pisces", 3909, image)
        constellationList.append(Pisces)

        image = ImageTk.PhotoImage(Image.open('constellations/ursaMin.png'))
        UrsaMinor = Constellation("Ursa Minor", 8222, image)
        constellationList.append(UrsaMinor)

        image = ImageTk.PhotoImage(Image.open('constellations/ursaMaj.png'))
        UrsaMajor = Constellation("Ursa Major", 49038, image)
        constellationList.append(UrsaMajor)

        image = ImageTk.PhotoImage(Image.open('constellations/draco.png'))
        Draco = Constellation("Draco", 41542, image)
        constellationList.append(Draco)

        image = ImageTk.PhotoImage(Image.open('constellations/cepheus.png'))
        Cepheus = Constellation("Cepheus", 76423, image)
        constellationList.append(Cepheus)

        image = ImageTk.PhotoImage(Image.open('constellations/casiopea.png'))
        Cassiopeia = Constellation("Cassiopeia", 544, image)
        constellationList.append(Cassiopeia)


        image = ImageTk.PhotoImage(Image.open('constellations/auriga.png'))
        Auriga = Constellation("Auriga", 18021, image)
        constellationList.append(Auriga)

        image = ImageTk.PhotoImage(Image.open('constellations/bootes.png'))
        Bootes = Constellation("Bootes", 49140, image)
        constellationList.append(Bootes)

        image = ImageTk.PhotoImage(Image.open('constellations/centaurus.png'))
        Centaurus = Constellation("Centaurus", 51926, image)
        constellationList.append(Centaurus)

        image = ImageTk.PhotoImage(Image.open('constellations/cygnus.png'))
        Cygnus = Constellation("Cygnus", 74084, image)
        constellationList.append(Cygnus)

        image = ImageTk.PhotoImage(Image.open('constellations/orion.png'))
        Orion = Constellation("Orion", 17947, image)
        constellationList.append(Orion)

        image = ImageTk.PhotoImage(Image.open('constellations/hercules.png'))
        Hercules = Constellation("Hercules", 57888, image)
        constellationList.append(Hercules)

        image = ImageTk.PhotoImage(Image.open('constellations/aquila.png'))
        Aquila = Constellation("Aquila", 67320, image)
        constellationList.append(Aquila)

        image = ImageTk.PhotoImage(Image.open('constellations/canisMaj.png'))
        CanisMajor = Constellation("Canis Major", 26214, image)
        constellationList.append(CanisMajor)

        image = ImageTk.PhotoImage(Image.open('constellations/canisMin.png'))
        CanisMinor = Constellation("Canis Minor", 27267, image)
        constellationList.append(CanisMinor)

        image = ImageTk.PhotoImage(Image.open('constellations/crux.png'))
        Crux = Constellation("Crux", 45767, image)
        constellationList.append(Crux)

        image = ImageTk.PhotoImage(Image.open('constellations/hydra.png'))
        Hydra = Constellation("Hydra", 50094, image)
        constellationList.append(Hydra)

        image = ImageTk.PhotoImage(Image.open('constellations/lyra.png'))
        Lyra = Constellation("Lyra", 65795, image)
        constellationList.append(Lyra)



        image = ImageTk.PhotoImage(Image.open('constellations/pegasus.png'))
        Pegasus = Constellation("Pegasus", 79533, image)
        constellationList.append(Pegasus)

        image = ImageTk.PhotoImage(Image.open('constellations/perseus.png'))
        Perseus = Constellation("Perseus", 50098, image)
        constellationList.append(Perseus)

        # Return the list of constellations
        self.ConstellationsList = constellationList
        return constellationList

                
