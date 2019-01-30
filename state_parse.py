import pycountry


def state_parsing(state):  # return find code of country or XXX
    for subdivision in pycountry.subdivisions:
        if state == subdivision.name:
            return subdivision.country.alpha_3
    return "XXX"
