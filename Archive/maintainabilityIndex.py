import math
from SLOCCalculator import SLOC_calculator
from McCabeCalculator import mccabe_calculator
from HalsteadVolumeCalculator import calculate_halstead_volume


def calculateIndex():
    mi_values = list()
    sloc_values = SLOC_calculator()
    McCabe_values = mccabe_calculator()
    halstead_volume_values = calculate_halstead_volume()

    for i in range(0, len(sloc_values)):
        if sloc_values[i] <= 0:
            print(sloc_values[i], i)
        mi = 171 - 5.2 * math.log(halstead_volume_values[i]) - 0.23 * math.log(McCabe_values[i]) - 16.2 * math.log(
            sloc_values[i])
        mi_values.append(mi)
    print(mi_values)


calculateIndex()
