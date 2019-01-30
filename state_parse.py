import pycountry

def state_parsing(state):
    for subdivision in pycountry.subdivisions:
        if state == subdivision.name:
            return subdivision.country.alpha_3
    return "XXX"