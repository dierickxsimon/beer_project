import random

def tempratureHandler(temprature, fridge, warm_element, calibrated_T):
    if not temprature:
        temprature = 23
    match (fridge, warm_element):
        case (True, True):
            return 'error'

        case (True, False):
            temprature_diff = -0.5
            deviation_temprature_diff = 0.2

        case (False, True):
            temprature_diff = 0.5
            deviation_temprature_diff = 0.2

        case (False, False):
            temprature_diff = -0.2
            deviation_temprature_diff = 0.2

    new_temperature = temprature + random.gauss(temprature_diff, deviation_temprature_diff) + calibrated_T
    return new_temperature