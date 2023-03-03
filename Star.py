

# Column Values from the hyg.csv
# Model representing a star type
class Star:
    def __init__(self, starId = '', hip = '', hd = '', hr = '', gliese = '', bayerFlamsteed = '', properName = '', ra = '', dec = '', distance = '', mag = '', absMag = '', spectrum = '', colorIndex = ''):
        self.starId = starId
        self.hip = hip
        self.hd = hd
        self.hr = hr
        self.gliese = gliese
        self.bayerFlamsteed = bayerFlamsteed
        self.properName = properName
        self.ra = ra
        self.dec = dec
        self.distance = distance
        self.mag = mag
        self.absMag = absMag
        self.spectrum = spectrum
        self.colorIndex = colorIndex

    @property
    def starId(self):
        return self._starId

    @property
    def hip(self):
        return self._hip

    @property
    def hd(self):
        return self._hd

    @property
    def hr(self):
        return self._hr

    @property
    def gliese(self):
        return self._gliese

    @property
    def bayerFlamsteed(self):
        return self._bayerFlamsteed

    @property
    def properName(self):
        return self._properName

    @property
    def ra(self):
        return self._ra

    @property
    def dec(self):
        return self._dec

    @property
    def distance(self):
        return self._distance

    @property
    def mag(self):
        return self._mag

    @property
    def absMag(self):
        return self._absMag

    @property
    def spectrum(self):
        return self._spectrum

    @property
    def colorIndex(self):
        return self._colorIndex

    @starId.setter
    def starId(self, value):
        if (value.isnumeric()):
            self._starId = float(value)
        else:
            self._starId = None

    @hip.setter
    def hip(self, value):
        if (value.isnumeric()):
            self._hip = float(value)
        else:
            self._hip = None


    @hd.setter
    def hd(self, value):
        if (value.isnumeric()):
            self._hd = float(value)
        else:
            self._hd = None


    @hr.setter
    def hr(self, value):
        if (value.isnumeric()):
            self._hr = value
        else:
            self._hr = None


    @gliese.setter
    def gliese(self, value):
        self._gliese = value

    @bayerFlamsteed.setter
    def bayerFlamsteed(self, value):
        self._bayerFlamsteed = value

    @properName.setter
    def properName(self, value):
        self._properName = value

    @ra.setter
    def ra(self, value):
        if (value.isnumeric()):
            self._ra = float(value)
        else:
            self._ra = None


    @dec.setter
    def dec(self, value):
        if (value.isnumeric()):
            self._dec = float(value)
        else:
            self._dec = None


    @distance.setter
    def distance(self, value):
        if (value.isnumeric()):
            self._distance = float(value)
        else:
            self._distance = None


    @mag.setter
    def mag(self, value):
        if (value.isnumeric()):
            self._mag = float(value)
        else:
            self._mag = None


    @absMag.setter
    def absMag(self, value):
        if (value.isnumeric()):
            self._absMag = float(value)
        else:
            self._absMag = None


    @spectrum.setter
    def spectrum(self, value):
        self._spectrum = value

    @colorIndex.setter
    def colorIndex(self, value):
        if (value.isnumeric()):
            self._colorIndex = float(value)
        else:
            self._colorIndex = None
