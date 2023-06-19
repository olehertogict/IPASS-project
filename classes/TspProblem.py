from classes.City import City
from opencage.geocoder import OpenCageGeocode
import api_key
import tsplib95

class TspProblem:
    def __init__(self, cities: list[City] = None):
        if cities:
            self.cities = cities
        else:
            self.cities = []

    def get_cities_from_user(self) -> None:
        running = True
        print("If you which to exit type: 'exit'")
        while running:
            user_inp = input("Enter an address: ")
            if user_inp == 'exit':
                return
            geocoder = OpenCageGeocode(key=api_key.API_KEY)
            result = geocoder.geocode(user_inp)
            coords = (result[0]['geometry']['lat'], result[0]['geometry']['lng'])
            yes_no = input(f'is {City(user_inp, coords)} the city you want to add? (y/n) ')
            if yes_no in ['y', 'yes']:
                self.cities.append(City(user_inp, coords))
                print(f'saving: {City(user_inp, coords)} to tsp problem')

    def get_tsp_problem_from_file(self, file_name: str) -> None:
        problem = tsplib95.load(file_name)
        problem_dict = problem.as_name_dict()
        # File has to have a 'NODE_COORD_SECTION'
        c = problem_dict.get('node_coords')
        self.cities = [City(str(name), tuple(pos)) for name, pos in c.items()]

