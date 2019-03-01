import math

class Test():

    def distance(self):
        lat = math.radians(float(input("Starting lat: ")))
        lon = math.radians(float(input("Starting long: ")))
        elat = math.radians(float(input("Ending lat: ")))
        elon = math.radians(float(input("Ending long: ")))
        Dm = (637100*math.acos(math.sin(lat)*math.sin(elat)
        + math.cos(lat)*math.cos(elat)*math.cos(lon-elon)))
        print("Distance in meters: ", end="")
        print(Dm)

Test = Test()

Test.distance()