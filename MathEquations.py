# Jacob Cappi : notes:
    # Planet is for planet calls

from Planets import Planet
from Moon import MoonPhases
from datetime import datetime
from datetime import timezone
import math

class MathEquations:
    __RADS = float(math.pi /180.0)
    __DEGS = float(180.0 / math.pi)

    _time = None

    _cy = 0
    _julianDate = 0
    _MST = 0

    _lat = 0
    _long = 0

    _planets = []
    
# API
    # list is [NAME, RA, DEC, DIST]
    def GetPlanetsRAandD(self):
        planetCoords = []
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

            planetCoords.append([p.planetName, pRA, pDec, pDist])

            print("\n**************************")
            print(p.planetName)
            print(pRA, pDec, pDist)
            print("**************************\n")
        return planetCoords
        
    # returns tuple (azi, alt)
    def ConvertRAandDecToAziAndAlt(self, RA, Dec):
        angleHR = self._MST - RA

        angleHR = angleHR+360 if angleHR < 0.0 else angleHR

        radDec = Dec * self.__RADS
        radLat = self._lat * self.__RADS
        radHR = angleHR * self.__RADS

        alt = math.asin((math.sin(radDec) * math.sin(radLat)) + (math.cos(radDec) * math.cos(radLat)*math.cos(radHR)))

        try:
            az = math.acos(math.sin(radDec) - math.sin(alt) * math.sin(radLat) / (math.cos(alt) *math.cos(radLat)))
        except:
            az = 0

        alt *= self.__DEGS
        az *= self.__DEGS

        if (math.sin(radHR) > 0.0):
            az = 360.0 - az

        return (az, alt)
    
    # Math EQs must be init 
    # PDF was just... dumb... for this part, so I used this website's formula with some adjustments to account for range
    # https://www.subsystems.us/uploads/9/8/9/4/98948044/moonphase.pdf
    def GetLunarPhase(self):
        moonphase = None
        
        # since range is 1900 - 2100, this JD is from Jan 1 1900 : 13:52 as that was the last full moon in range
        thatDate = datetime(year=1900, month=1, day=1, hour=13, minute=52, tzinfo=timezone.utc)
        # that 13 minute gap is now accounted for
        if (self._time < thatDate):
            return MoonPhases.NEW

        jdDate = self._getExactJulianDate(thatDate)
        current = self._getExactJulianDate(self._time)

        daySinceNew = current - jdDate
        NewMoons = daySinceNew / 29.53 # days for moon cycle
        daysIntoCycle = (NewMoons%1) *29.53
        print(daysIntoCycle)

        # This is the approximation as we don't account for lunation or exact types...
        if (daysIntoCycle < 0.5 or daysIntoCycle > 29):
            return MoonPhases.NEW
        elif (daysIntoCycle < 7.5):
            return MoonPhases.WAXINGC
        elif (daysIntoCycle < 8.5):
            return MoonPhases.FIRSTQ
        elif (daysIntoCycle < 15.5):
            return MoonPhases.WAXINGG
        elif (daysIntoCycle < 16.5):
            return MoonPhases.FULL
        elif (daysIntoCycle < 22.5):
            return MoonPhases.WANINGG
        elif (daysIntoCycle < 23.5):
            return MoonPhases.THIRDQ
        elif (daysIntoCycle < 28.5):
            return MoonPhases.WANINGC

    # another instance of the pdf being bad, but jd here is based on 1900.1.1 and I just had to ... figure it out?
    # these are also in Lat, Long. UI might have a hard time displaying moon here w/o a good understanding of Az elv
    # same format as the other eq
    def GetMoonPosition(self):
        # since range is 1900 - 2100, this JD is from Jan 1 1900 : 13:52 as that was the last full moon in range
        thatDate = datetime(year=1900, month=1, day=1, tzinfo=timezone.utc)

        jdDate = self._getExactJulianDate(thatDate)
        current = self._getExactJulianDate(self._time)

        T = (current - jdDate) / 36525
        # Degree ver
        LP = 270.434164+(481267.883*T) #Moon mean long
        M = 358.47833 + (35999.0498*T) # Sun Mean anomaly
        MP = 296.104608 + (477198.849*T) # Moon mean annoaly
        D = 350.737486 + (445267.1142*T) # moon mean elong
        F = 11.250889 + (483202.0251*T) # Mean dist from asc node


        # Rad ver
        RLP = self._moduloTwoPi(LP *self.__RADS)
        RM = self._moduloTwoPi(M * self.__RADS)
        RMP = self._moduloTwoPi(MP * self.__RADS)
        RD = self._moduloTwoPi(D * self.__RADS)
        RF = self._moduloTwoPi(F * self.__RADS)

        e = 1 - (0.002495*T) - (0.00000752*(T**2))

        la = RLP + (6.288750*math.sin(RMP)) + (1.274018*math.sin(2*RD-RMP))
        lb = (0.658309*math.sin(2*RD)) + (0.213616*math.sin(2*RMP)) - (0.185596*math.sin(RM) * e) - (0.114336*math.sin(2*RF))
        lc = (0.058793*math.sin(2*RD-2*RMP)) + (0.057212 * math.sin(2*RD-RM-RMP) * e) + (0.053320*math.sin(2*RD+RMP))
        ld = (0.045874*math.sin(2*RD-RM) * e)

        alpha = la + lb + lc + ld

        qa = (5.128189*math.sin(RF)) + (0.280606*math.sin(RMP+RF)) + (0.277693*math.sin(RMP-RF))
        qb = (0.173238 * math.sin(2*RD-RF)) + (0.055413*math.sin(2*RD+RF-RMP))
        qc = (0.046272 * math.sin(2*RD - RF - RMP)) + (0.032573*math.sin(2*RD+RF)) + (0.017198*math.sin(2*RMP+RF))
        qd = (0.009267*math.sin(2*RD+RMP-RF)) + (0.008823 * math.sin(2*RMP-RF))

        beta = qa+qb+qc+qd

        return self.ConvertRAandDecToAziAndAlt(alpha, beta)
    

    def InitMathEquations(self, time, planets, lat, long, isNorth, isEast):
        self._time = time
        self._getRelativeJulianDay(time)
        self._getMST(time)

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
    
    def _getMST(self, time):
        Y = float(time.year)
        M = float(time.month)
        D = float(time.day)
        H = float(time.hour)
        MIN = float(time.minute)
        S = float(time.second)

        if M <= 2:
            Y -= 1
            M += 12
        
        a = math.floor(Y/100.0)
        b = 2 - a + math.floor(a/4)
        c = math.floor(365.25 * Y)
        d = math.floor(30.6001 *(M+1))

        jd = b + c + d - 730550.5 + D + (H + MIN/60 + S/3600) / 24
        jt = jd/36525.0

        mst= 280.46061837 + (360.98564736629 * jd) + (0.000387933 * jt**2) - (jt**3 / 38710000) + self._long
        if mst > 0.0:
            while (mst > 360.0): mst -= 360.0
        else:
            while (mst < 0.0): mst += 360.0
        self._MST = mst



    # Checked with doc value, this eq works
    def _getExactJulianDate(self, time):
        Y = int(time.year)
        M = int(time.month)
        Dd = float(time.day) + float((float(time.hour) + (float(time.minute)/60)) / 24)

        if not (M > 2):
            Y = Y-1
            M = M+12
        
        if (time > datetime(year=1582, month=10, day=15, tzinfo=timezone.utc)):
            # Python is stupid and has no types, assuming this static cast will work
            A = int(Y/100)
            B = int(2 - A + int(A/4))
        else:
            B = 0
        
        julianDate = int(365.25*Y) + int(30.6001*(M+1)) + Dd + 1720994.5 + B
        return julianDate

    # The equation in the doc lists MM as both Month and Minutes.... wtf?
    # Apparently the relative for j2000 is just JD - 2451545
    # Checked with calculators, also correct
    # J2000 number : Use this for celestials
    def _getRelativeJulianDay(self, time):
        jd = self._getExactJulianDate(time)
        self._julianDate = jd - 2451545.0
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

