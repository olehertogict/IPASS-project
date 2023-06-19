from classes.City import City


class Tour:
    def __init__(self, cities: list[City]):
        self.cities = cities
        self.distance = 0
        # if Tour is initialized with cities already in the tour. calculate distance of the tour
        if len(cities) > 1:
            for i in range(len(cities) - 1):
                self.distance += cities[i].distance2(cities[i + 1])

    def __len__(self) -> int:
        """
        :return: The amount of cities in the current tour
        """
        return len(self.cities)

    def __repr__(self) -> str:
        return f'{self.cities}'

    def __getitem__(self, i: int) -> City:
        return self.cities[i]

    def __copy__(self):
        return Tour(self.cities.copy())

    def add_city(self, city: City) -> None:
        """
        :param city: Add a city to the Tour
        """
        if len(self.cities) > 1:
            self.distance += self.cities[-1].distance2(city)
        self.cities.append(city)

    def swap_cities(self, i: int, j: int) -> None:
        """
        Swap cities in the tour on index i and index j
        :param i: City on index i
        :param j: City on index j
        """
        self.cities[i], self.cities[j] = self.cities[j], self.cities[i]
        # Recalculate distance
        self.distance = 0
        for i in range(len(self.cities) - 1):
            self.distance += self.cities[i].distance2(self.cities[i + 1])

    def calc_distance(self) -> float:
        self.distance = 0
        for i in range(len(self.cities) - 1):
            self.distance += self.cities[i].distance_to(self.cities[i + 1])
        return self.distance

    def calc_distance2(self) -> float:
        self.distance = 0
        for i in range(len(self.cities) - 1):
            self.distance += self.cities[i].distance2(self.cities[i + 1])
        return self.distance

