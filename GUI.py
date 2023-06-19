from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox
from PyQt5.QtGui import QPixmap
import sys
from main import *

class TspGui(QWidget):
    def __init__(self):
        super().__init__()
        self.current_algorithm = 'Nearest neighbour'
        self.problems = ['att48', 'a280', 'berlin52', 'ch130', 'ch150', 'dj38', 'fl1577', 'wi29']

        self.setWindowTitle('Travelling Salesman Problem')

        self.tour_length = run(f'TestProblems/att48.tsp', 'Nearest Neighbour')

        # Create label widget to display the image
        self.image_label = QLabel(self)
        pixmap = QPixmap("animation.jpeg")
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

        self.button3 = QPushButton('Calculate route', self)
        vbox1.addWidget(self.button3)
        self.button3.clicked.connect(self.calculateRouteCall)

        hbox1.addLayout(vbox1)

        self.setLayout(hbox1)

        self.show()

    def button1_call(self):
        self.current_algorithm = self.combo.currentText()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')

    def calculateRouteCall(self):
        self.button1_call()

        self.tour_length = run(f'TestProblems/{self.combo1.currentText()}.tsp', self.combo.currentText())

        pixmap = QPixmap("animation.jpeg")
        self.image_label.setPixmap(pixmap)

        self.label4.setText(f'Length of the current tour = {round(self.tour_length, 2)}')


def runGUI():
    app = QApplication(sys.argv)
    ex = TspGui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    runGUI()
