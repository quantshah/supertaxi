"""
Environment which simulates a taxi movement
"""


class Taxi:
    """
    A taxi class to keep track of the internal state for each taxi.
    """
    def __init__(self, number, start_location):
        super().__init__(number, start_location)
        self._number = number
        self.available = True
        self.current_location = start_location
        self.destination = []
        self.path = []
        self.path_generator = None

    @property
    def number(self):
        return self._number

    def hire(self, destination):
        if self.available == True:
            self.available = False
            self.destination = destination
            self.path = nx.shortest_path(road_network, self.current_location, self.destination)
            self.path_generator = (p for p in self.path)

    def reset(self):
        self.available = True
        self.destination = []
        self.path = []

    def step(self):
        if not self.available:
            if self.current_location == self.destination:
                self.reset()
            else:
                self.current_location = next(self.path_generator)

    def __repr__(self):
        return str(self.number)