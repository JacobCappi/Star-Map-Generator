# Column Values from the hyg.csv
# Model representing a star type
class Planets:
    def __init__(self, planetName = '', lScal = '', lProp = '', aScal = '', aConst = '', eScal = '', eProp = '', iScal = '', iProp = '', wScal = '', wProp = '', oScal = '', oProp = ''):
        self.planetName = planetName
        self.lScal = lScal
        self.lProp = lProp
        self.aScal = aScal
        self.aConst = aConst
        self.eScal = eScal
        self.eProp = eProp
        self.iScal = iScal
        self.iProp = iProp
        self.wScal = wScal
        self.wProp = wProp
        self.oScal = oScal
        self.oProp = oProp

    @property
    def planetName(self):
        return self._planetName

    @property
    def lScal(self):
        return self._lScal

    @property
    def lProp(self):
        return self._lProp

    @property
    def aScal(self):
        return self._aScal

    @property
    def aConst(self):
        return self._aConst

    @property
    def eScal(self):
        return self._eScal

    @property
    def eProp(self):
        return self._eProp

    @property
    def iScal(self):
        return self._iScal

    @property
    def iProp(self):
        return self._iProp

    @property
    def wScal(self):
        return self._wScal

    @property
    def wProp(self):
        return self._wProp

    @property
    def oScal(self):
        return self._oScal

    @property
    def oProp(self):
        return self._oProp

    @planetName.setter
    def planetName(self, value):
        try:
            self._planetName = float(value)
        except:
            pass

    @lScal.setter
    def lScal(self, value):
        try:
            self._lScal = float(value)
        except:
            pass


    @lProp.setter
    def lProp(self, value):
        try:
            self._lProp = float(value)
        except:
            pass


    @aScal.setter
    def aScal(self, value):
        try:
            self._aScal = float(value)
        except:
            pass


    @aConst.setter
    def aConst(self, value):
        try:
            self._aConst = float(value)
        except:
            pass

    @eScal.setter
    def eScal(self, value):
        try:
            self._eScal = float(value)
        except:
            pass

    @eProp.setter
    def eProp(self, value):
        try:
            self._eProp = float(value)
        except:
            pass

    @iScal.setter
    def iScal(self, value):
        try:
            self._iScal = float(value)
        except:
            pass


    @iProp.setter
    def iProp(self, value):
        try:
            self._iProp = float(value)
        except:
            pass


    @wScal.setter
    def wScal(self, value):
        try:
            self._wScal = float(value)
        except:
            pass


    @wProp.setter
    def wProp(self, value):
        try:
            self._wProp = float(value)
        except:
            pass


    @oScal.setter
    def oScal(self, value):
        try:
            self._oScal = float(value)
        except:
            pass


    @oProp.setter
    def oProp(self, value):
        try:
            self._oProp = float(value)
        except:
            pass
