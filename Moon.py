from enum import Enum

# Only these 4 are used, as intermediates cannot be calc accurately without 
# advanced formulas... and they aren't in the pdf
class MoonPhases(Enum):
    NEW = 0,
    WAXINGC = 1
    FIRSTQ = 2,
    WAXINGG = 3,
    FULL = 4,
    WANINGG = 5,
    THIRDQ = 6,
    WANINGC = 7,


