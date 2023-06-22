from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QMainWindow, \
    QDialog, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
from main import *
import ast


class CreateCitiesDialog(QDialog):
    def __init__(self, tsp_gui):
        super().__init__()
        self.tsp_gui = tsp_gui
        self.cities = []
        self.setWindowTitle('Create TSP Problem')
        layout = QVBoxLayout()

        label = QLabel('Enter a city name in the left box and the coordinates in the right box in this format (20, 4.5)')
        layout.addWidget(label)

        hbox = QHBoxLayout()

        self.city_input = QLineEdit()
        hbox.addWidget(self.city_input)

        self.coords_input = QLineEdit()
        hbox.addWidget(self.coords_input)

        layout.addLayout(hbox)

        self.submit_button = QPushButton('Submit', self)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.submit_city)

        self.done_button = QPushButton('Done', self)
        layout.addWidget(self.done_button)
        self.done_button.clicked.connect(self.done_button_clicked)

        self.setLayout(layout)

    def submit_city(self):
        city_name = self.city_input.text()
        coords = self.coords_input.text()
        self.city_input.setText('')
        self.coords_input.setText('')
        self.cities.append(City(city_name, ast.literal_eval(coords)))

    def done_button_clicked(self):
        self.tsp_gui.cities = self.cities
        self.close()

class TspGui(QWidget):
    def __init__(self):
        super().__init__()
        self.cities = []
        self.current_algorithm = 'Nearest neighbour'
        self.problems = ['att48', 'a280', 'berlin52', 'ch130', 'ch150', 'dj38', 'fl1577', 'wi29']

        self.setWindowTitle('DHL route calculator')
        self.setStyleSheet("QPushButton { background-color: white; color: black; border-radius: 5px; }")

        self.tour_data = calc_route('att48', 'Nearest Neighbour')

        self.image_label = QLabel(self)
        pixmap = QPixmap("images/animation.jpeg")
        self.image_label.setPixmap(pixmap)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.image_label)

        vbox1 = QVBoxLayout()

        self.image_label2 = QLabel(self)
        pixmap = QPixmap("images/DHL-LOGO.jpg")
        resized_pixmap = pixmap.scaled(270, 120)
        self.image_label2.setPixmap(resized_pixmap)
        vbox1.addWidget(self.image_label2)

        self.label4 = QLabel()
        self.label4.setText(f'Length of the current tour: {round(self.tour_data["distance"], 2)}')
        vbox1.addWidget(self.label4)

        self.label5 = QLabel()
        self.label5.setText(f'Calculation time: {round(self.tour_data["time"], 8)}')
        vbox1.addWidget(self.label5)

        self.label1 = QLabel()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')
        vbox1.addWidget(self.label1)

        self.label2 = QLabel()
        self.label2.setText('select an algorithm to use:')
        vbox1.addWidget(self.label2)

        self.combo = QComboBox(self)
        self.combo.addItem('Nearest Neighbour')
        self.combo.addItem('Evolutionary/Genetic')
        self.combo.addItem('2-Opt')
        vbox1.addWidget(self.combo)

        self.label3 = QLabel()
        self.label3.setText('Select an existing TSP problem:')
        vbox1.addWidget(self.label3)

        self.combo1 = QComboBox(self)
        for p_name in self.problems:
            self.combo1.addItem(p_name)
        vbox1.addWidget(self.combo1)

        self.button1 = QPushButton('Calculate route', self)
        vbox1.addWidget(self.button1)
        self.button1.clicked.connect(self.calculateRouteCall)

        self.button2 = QPushButton('Create TSP problem', self)
        vbox1.addWidget(self.button2)
        self.button2.clicked.connect(self.createCities)

        self.button3 = QPushButton('Calc own TSP problem', self)
        vbox1.addWidget(self.button3)
        self.button3.clicked.connect(self.calculateRouteCall)

        hbox1.addLayout(vbox1)

        self.setLayout(hbox1)

        self.show()

    def calculateRouteCall(self):
        self.current_algorithm = self.combo.currentText()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')

        if not self.cities:
            self.tour_data = calc_route(self.combo1.currentText(), self.combo.currentText())
        else:
            self.tour_data = calc_route('OwnAlgorithm', self.combo.currentText(), self.cities)

        pixmap = QPixmap("images/animation.jpeg")
        self.image_label.setPixmap(pixmap)

        self.label4.setText(f'Length of the current tour: {round(self.tour_data["distance"], 2)}')
        self.label5.setText(f'Calculation time: {round(self.tour_data["time"], 8)}')

    def createCities(self):
        dialog = CreateCitiesDialog(self)
        dialog.exec_()


def runGUI():
    app = QApplication(sys.argv)
    ex = TspGui()
    sys.exit(app.exec_())

