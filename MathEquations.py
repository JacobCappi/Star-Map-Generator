# Jacob Cappi : notes:
    # Planet is for planet calls

from Planets import Planet
from datetime import datetime
import math

class MathEquations:
    __RADS = float(math.pi /180.0)
    __DEGS = float(180.0 / math.pi)

    _cy = 0
    _julianDate = 0

    _lat = 0
    _long = 0

    _planets = []
    
# API
    def GetPlanetsRAandD(self):
        planetCoords = [[]]
        e = None

        for planet in self._planets:
            if planet.planetName == "Earth/Sun":
                e = planet
                break

        # Earth Coordinates
        mE = self._moduloTwoPi(e.L - e.W)
        vE = self._trueAnomoly(mE, e.E)
        rE = e.A * (1- (e.E)**2) / (1 + e.E*math.cos(vE))
        xE = rE * math.cos(vE + e.O)
        yE = rE * math.sin(vE + e.O)
        zE = 0.0

        # Rest of the planets
        for p in self._planets:

            pM = self._moduloTwoPi(p.L - p.W)
            pV = self._trueAnomoly(pM, p.E)
            pR = p.A * (1- (p.E)**2) / (1 + p.E*math.cos(pV))

            pXh = 0.0
            pYh = 0.0
            pZh = 0.0

            # No need to do earth since helio should be 0
            if p.planetName != "Earth/Sun":
                pXh = pR * (math.cos(p.O) * math.cos(pV + p.W - p.O) - math.sin(p.O) * math.sin(pV + p.W - p.O) * math.cos(p.I))
                pYh = pR * (math.sin(p.O) * math.cos(pV + p.W - p.O) + math.cos(p.O) * math.sin(pV + p.W - p.O) * math.cos(p.I))
                pZh = pR * (math.sin(pV + p.W - p.O) * math.sin(p.I))
            
            # p geo convert using earth
            pXg = pXh - xE
            pYg = pYh - yE
            pZg = pZh - zE

            # eclipt to equ
            ecl = 23.439281 * self.__RADS
            xEQ = pXg
            yEQ = pYg*math.cos(ecl) - pZg *math.sin(ecl)
            zEQ = pYg*math.sin(ecl) + pZg*math.cos(ecl)

            pRA = self._moduloTwoPi(math.atan2(yEQ, xEQ)) * self.__DEGS
            pDec = math.atan(zEQ / math.sqrt(xEQ**2 + yEQ **2)) *self.__DEGS
            pDist = math.sqrt(xEQ**2 + yEQ**2 + zEQ**2)

            planetCoords.append([pRA, pDec, pDist])

            print("\n**************************")
            print(p.planetName)
            print(pRA, pDec, pDist)
            print("**************************\n")
        return planetCoords
        
    
    # returns tuple (azi, alt)
    def ConvertRAandDecToAziAndAlt(self, RA, Dec):
        pass


    def InitMathEquations(self, time, planets, lat, long, isNorth, isEast):
        self._getRelativeJulianDay(time)

        self._lat = lat if isNorth else lat*-1
        self._long = long if isEast else long*-1

        self._cy = self._julianDate / 36525
        self._planets = planets
        self._calcPlanets()

# Private
    # Assumes rads
    def _moduloTwoPi(self, angle):
        B = angle / (2*math.pi)
        adjB = math.floor(B) if B >= 0 else math.ceil(B)

        A = (2*math.pi) * (B - adjB)
        A = A + (2*math.pi) if A < 0 else A
        return A
    
    # Assumes rads
    def _trueAnomoly(self, m, pE):
        E = m + pE*math.sin(m) * (1.0 + pE*math.cos(m))

        tmpE = E
        E = tmpE - ((tmpE - pE*math.sin(tmpE) - m) / (1-pE*math.cos(tmpE)))

        while (abs(E - tmpE) > 1.0e-12):
            tmpE = E
            E = tmpE - ((tmpE - pE*math.sin(tmpE) - m) / (1-pE*math.cos(tmpE)))
        
        V = 2 * math.atan(math.sqrt((1 + pE)/(1-pE))) * math.tan(0.5*E)
        if V < 0:
            V = V + (2*math.pi)
        return V

    # Checked with doc value, this eq works
    def _getExactJulianDate(self, time):
        Y = int(time.year)
        M = int(time.month)
        Dd = float(time.day) + float((float(time.hour) + (float(time.minute)/60)) / 24)

        if not (M > 2):
            Y = Y-1
            M = M+12
        
        if (time > datetime(year=1582, month=10, day=15)):
            # Python is stupid and has no types, assuming this static cast will work
            A = int(Y/100)
            B = int(2 - A + int(A/4))
        else:
            B = 0
        
        self._julianDate = int(365.25*Y) + int(30.6001*(M+1)) + Dd + 1720994.5 + B
        print(self._julianDate)
        pass

    # The equation in the doc lists MM as both Month and Minutes.... wtf?
    # Apparently the relative for j2000 is just JD - 2451545
    # Checked with calculators, also correct
    # J2000 number : Use this 
    def _getRelativeJulianDay(self, time):
        self._getExactJulianDate(time)
        self._julianDate -= 2451545.0
        print(self._julianDate)

    def _calcPlanets(self):
        for planet in self._planets:
            planet.A = self._calcAxisOfOrbit(planet)
            planet.E = self._calcEccentricity(planet)
            planet.I = self._calcInclination(planet)
            planet.W = self._calcPerihelion(planet)
            planet.O = self._calcLongitudeOfAscending(planet)
            planet.L = self._calcMeanLogitude(planet)

            print("\n**************************")
            print(planet.planetName)
            print(planet.PostCalcString())
            print("**************************\n")
        
    def _calcAxisOfOrbit(self, planet):
        # Another stupid thing, eq calls for Aprop, spreadsheet calls this Aconst... ........
        return planet.aScal + planet.aConst * self._cy

    def _calcEccentricity(self, planet):
        return planet.eScal + planet.eProp * self._cy

    def _calcInclination(self, planet):
        return (planet.lScal - planet.lProp * self._cy/3600) * self.__RADS

    def _calcPerihelion(self, planet):
        # jesus.... Perihelion is just ? in the spreadsheet, instead of omega... why????
        return (planet.wScal + planet.wProp * self._cy/3600) * self.__RADS

    def _calcLongitudeOfAscending(self, planet):
        return (planet.oScal + planet.oProp * self._cy/3600) * self.__RADS

    def _calcMeanLogitude(self, planet):
        return self._moduloTwoPi((planet.lScal + planet.lProp * self._cy/3600) *self.__RADS)

