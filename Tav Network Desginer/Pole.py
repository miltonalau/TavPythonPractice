
class Pole(object):
    lat = float(0)
    lon = float(0)

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

def make_pole(lat, lon):
    pole = Pole(lat, lon)
    return pole