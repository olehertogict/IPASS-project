# IPASS project
This is an implementation of the Travelling Salesman Problem (TSP). In this repository there is a Graphical User 
Interface (GUI). You can use three different algorithms to calculate the 'optimal' route.
- Nearest Neighbour
- Evolutionary/Genetic
- 2-opt

## Installation
To install this project, first you have to clone the repository. Navigate to the directory where you want the project
to be installed. Then clone the project using this command:
```commandline
git clone "https://github.com/olehertogict/IPASS-project"
```
When the project is done cloning navigate to the project folder in the terminal.
```commandline
cd YOUR_PATH/IPASS-project 
```
And run the following command to install all required packages.
```commandline
pip install -r requirements.txt
```
Congratulations you are now done with all the installation. To run the project just run the 'main.py' file and the GUI
will appear.

## Usage
The usage of the GUI is fairly straight forward. You can select which algorithm to use for the next calculation using
the dropdown box. You can also choose to use a few different already made TSP problems. To calculate the route click on
'calculate route'. 
There also is the possibility to create an own set of cities to calculate a route for.

## File structure
All the .py files in the following directories are used to run the entire application.
- Algorithms
- Application
- Classes

The files in "Algorithms" can be used separately to calculate a route from a given list of cities. 
These algorithms can be used by inputting a list of cities and the return value will be the route 
found by the algorithm.

In the "Tests" folder are tests for the classes. In the "Data" directory is the file "time_data.csv", in this file all 
the lengths and calculation times of all the routes are stored. Using the "IPASS-data.xlsx" file you can get an overview 
of a few the average calculation times and route lengths.

Inside the "Docs" folder there is a poster for the project and a project summary.

