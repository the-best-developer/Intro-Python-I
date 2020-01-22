# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

my_latlon = LatLon(10, 20)

print(f'class lat is: {my_latlon.lat}, class lon is: {my_latlon.lon}')

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

my_waypoint = Waypoint('chicken', 10, 20)

print(f'class lat is: {my_waypoint.lat}, class lon is: {my_waypoint.lon}, class name is: {my_waypoint.name}')

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
        

my_geocache = Geocache('chicken', 'really hard', 'large' , 10, 20)

print(f'class name is: {my_geocache.name}, class difficulty is: {my_geocache.difficulty}, class lon is: {my_geocache.lon}')

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

class OtherWaypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return f"Our waypoint is called: {self.name}, we're at {self.lat} x {self.lon}"

my_other_waypoint = OtherWaypoint('beef', 50, 100)

print(f'{my_other_waypoint.name}, {my_other_waypoint.lat}, {my_other_waypoint.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(my_other_waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

class OtherGeocache(Waypoint):

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (f"Our geocache is called: {self.name}, the difficulty is: {self.difficulty}, its {self.size} in size. It is located at {self.lat} x {self.lon}")
        
my_other_geocache = OtherGeocache('turkey', 'easy', 'small' , 25, 50)

print(f'{my_other_geocache.name}, {my_other_geocache.difficulty}, {my_other_geocache.size}, {my_other_geocache.lat}, {my_other_geocache.lon}')

# Print it--also make this print more nicely

print(my_other_geocache.__str__())
