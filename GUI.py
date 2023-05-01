from PyQt5.QtWidgets import \
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox
from PyQt5.QtGui import QMovie
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.current_algorithm = 'Nearest neighbour'
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Travelling Salesman Problem')
        # Create label widget to display the GIF
        self.movie_label = QLabel(self)
        self.movie = QMovie("animation.gif")
        self.movie_label.setMovie(self.movie)
        self.movie.start()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.movie_label)

        vbox1 = QVBoxLayout()
        self.label1 = QLabel()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')
        vbox1.addWidget(self.label1)

        self.label2 = QLabel()
        self.label2.setText('select an algorithm to use:')
        vbox1.addWidget(self.label2)

        self.combo = QComboBox(self)
        self.combo.addItem('Nearest neighbour')
        self.combo.addItem('Algorithm 2')
        self.combo.addItem('Algorithm 3')
        vbox1.addWidget(self.combo)

        self.button1 = QPushButton('submit', self)
        vbox1.addWidget(self.button1)
        self.button1.clicked.connect(self.button1_call)

        hbox2 = QHBoxLayout()
        self.x_label = QLabel()
        self.x_label.setText('X = ')
        hbox2.addWidget(self.x_label)
        self.x_input = QLineEdit(self)
        hbox2.addWidget(self.x_input)

        hbox3 = QHBoxLayout()
        self.y_label = QLabel()
        self.y_label.setText('Y = ')
        hbox3.addWidget(self.y_label)
        self.y_input = QLineEdit(self)
        hbox3.addWidget(self.y_input)

        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)

        self.button2 = QPushButton('submit', self)
        vbox1.addWidget(self.button2)
        self.button2.clicked.connect(self.button1_call)

        hbox1.addLayout(vbox1)

        self.setLayout(hbox1)

        self.show()

    def button1_call(self):
        self.current_algorithm = self.combo.currentText()
        self.label1.setText(f'Currently using algorithm: {self.current_algorithm}')
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
