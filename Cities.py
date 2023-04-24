import math


class City:
    def __init__(self, name: str, position: tuple[float | int, float | int]):
        """
        :param name: name of the city
        :param position: (x, y) position of the city
        """
        self.name = name
        self.position = position
        self.x, self.y = position[0], position[1]

    def __repr__(self):
        return f'{self.name.capitalize()}{self.position}'

    def distance_to(self, city) -> float:
        diff_x = abs(self.x - city.x)
        diff_y = abs(self.y - city.y)
        distance = math.sqrt((diff_x ** 2) + (diff_y ** 2))
        return distance

    def get_coordinates(self) -> tuple:
        return self.x, self.y


if __name__ == "__main__":
    c1 = City("Utrecht", (0, 0))
    c2 = City("Amsterdam", (3, 4))
    print(c1.distance_to(c2))
    print(c2.distance_to(c1))
    print(c1)
    print(c2)
    pass
