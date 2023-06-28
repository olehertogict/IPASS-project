import unittest
from Classes.Tour import Tour
from Classes.City import City


class TourTest(unittest.TestCase):
    def test_init(self):
        c = [City('1', (0, 0)), City('2', (1, 1)), City('3', (2, 2))]
        tour = Tour(c)
        self.assertEqual(tour.cities, c)
        self.assertEqual(tour.distance, 4)

    def test_magic_methods(self):
        c = [City('1', (0, 0)), City('2', (1, 1)), City('3', (2, 2))]
        tour = Tour(c)
        self.assertEqual(len(tour), 3)
        self.assertEqual(tour.__repr__(), '[1(0, 0), 2(1, 1), 3(2, 2)]')
        # __getitem__()
        self.assertEqual(tour[1], c[1])
        tour_copy = tour.__copy__()
        self.assertIsNot(tour, tour_copy)
        self.assertEqual(tour.cities, tour_copy.cities)
        # Check if original object is not modified
        tour_copy.cities.append(City('4', (3, 3)))
        self.assertNotEqual(tour.cities, tour_copy.cities)

    def test_add_city(self):
        c = [City('1', (0, 0)), City('2', (1, 1)), City('3', (2, 2))]
        tour = Tour(c)
        city = City('4', (3, 3))
        tour.add_city(city)
        self.assertEqual(len(tour), 4)
        self.assertEqual(tour[3], city)

    def test_swap_cities(self):
        c = [City('1', (0, 0)), City('2', (1, 1)), City('3', (2, 2))]
        tour = Tour(c)
        tour.swap_cities(0, 1)
        self.assertEqual(tour[0].name, '2')
        self.assertEqual(tour[1].name, '1')

    def test_calc_distances(self):
        c = [City('1', (4, 0)), City('2', (0, 0)), City('3', (0, 6))]
        tour = Tour(c)
        self.assertEqual(tour.calc_distance(), 10)
        self.assertEqual(tour.calc_distance2(), 52)


if __name__ == '__main__':
    unittest.main()
