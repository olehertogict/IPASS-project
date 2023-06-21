from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
from main import *

class TspGui(QWidget):
    def __init__(self):
        super().__init__()
        self.current_algorithm = 'Nearest neighbour'
        self.problems = ['att48', 'a280', 'berlin52', 'ch130', 'ch150', 'dj38', 'fl1577', 'wi29']

        self.setWindowTitle('DHL route calculator')

        self.tour_length = calc_route('att48', 'Nearest Neighbour')

        # Create label widget to display the image
        self.image_label = QLabel(self)
        pixmap = QPixmap("images/animation.jpeg")
        self.image_label.setPixmap(pixmap)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.image_label)

        vbox1 = QVBoxLayout()

        self.label4 = QLabel()
        self.label4.setText(f'Length of the current tour = {round(self.tour_length, 2)}')
        vbox1.addWidget(self.label4)

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

        hbox1.addLayout(vbox1)

        self.setLayout(hbox1)

        self.show()

    def calculateRouteCall(self):
        self.current_algorithm = self.combo.currentText()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')

        self.tour_length = calc_route(self.combo1.currentText(), self.combo.currentText())

        pixmap = QPixmap("images/animation.jpeg")
        self.image_label.setPixmap(pixmap)

        self.label4.setText(f'Length of the current tour = {round(self.tour_length, 2)}')

    def createCities(self):
        self.extra_window = QMainWindow()
        self.extra_window.setWindowTitle("Extra Window")
        self.extra_window.setGeometry(200, 200, 400, 300)
        self.extra_window.show()


def runGUI():
    app = QApplication(sys.argv)
    ex = TspGui()
    sys.exit(app.exec_())

