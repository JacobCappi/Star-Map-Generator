

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
        try:
            self._starId = float(value)
        except:
            pass

    @hip.setter
    def hip(self, value):
        try:
            self._hip = float(value)
        except:
            pass


    @hd.setter
    def hd(self, value):
        try:
            self._hd = float(value)
        except:
            pass


    @hr.setter
    def hr(self, value):
        try:
            self._hr = value
        except:
            pass

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
        try:
            self._ra = float(value)
        except:
            pass


    @dec.setter
    def dec(self, value):
        try:
            self._dec = float(value)
        except:
            pass


    @distance.setter
    def distance(self, value):
        try:
            self._distance = float(value)
        except:
            pass


    @mag.setter
    def mag(self, value):
        try:
            self._mag = float(value)
        except:
            pass


    @absMag.setter
    def absMag(self, value):
        try:
            self._absMag = float(value)
        except:
            pass


    @spectrum.setter
    def spectrum(self, value):
        self._spectrum = value

    @colorIndex.setter
    def colorIndex(self, value):
        try:
            self._colorIndex = float(value)
        except:
            pass
