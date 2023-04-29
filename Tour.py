from City import City


class Tour:
    def __init__(self, cities: list[City]):
        self.cities = cities
        self.distance = 0
        # if Tour is initialized with cities already in the tour. calculate distance of the tour
        if len(cities) > 1:
            for i in range(len(cities) - 1):
                self.distance += cities[i].distance_to(cities[i + 1])

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
            self.distance += self.cities[-1].distance_to(city)
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
            self.distance += self.cities[i].distance_to(self.cities[i + 1])

    def show(self):
        # TODO - function for displaying the tour in a graph
        pass


if __name__ == "__main__":
    c1 = City("Utrecht", (0, 0))
    c2 = City("Amsterdam", (3, 4))
    c3 = City("Rotterdam", (2, 7))
    c4 = City("Den Haag", (10, 12))
    cities_list = [c1, c2, c3]
    t1 = Tour(cities_list)
    print(t1)
    print(t1.distance)
    t1.swap_cities(0, 1)
    print(t1)
    print(t1.distance)
    pass
