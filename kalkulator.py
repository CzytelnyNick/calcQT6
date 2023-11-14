import sys
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator
from PyQt6.QtCore import QSize, Qt, QRegularExpression
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QLCDNumber,
    QFormLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QCheckBox,
    QComboBox,
    QHBoxLayout,
)

operation = ""
val1 = 0
val2 = 0
suma = 0
# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        global operation
        global suma
        super().__init__()
        self.setWindowTitle("Kalkulator")
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber(self)
        self.lcd.setFixedSize(400, 100)
        self.setFixedSize(400, 500)
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        one = QPushButton("1")
        two = QPushButton("2")
        three = QPushButton("3")
        one.setFixedSize(100, 100)
        # one.
        display = self.lcd.value()
        print(display)
        # self.lcd.display(1)
        print(display)
        def write(number):
            display = self.lcd.value()
            if display != 0.0:

                self.lcd.display(f"{str(int(display)) + str(number)}")
            else:

                self.lcd.display(f"{str(number)}")
        def subtract():
            display = self.lcd.value()
            if display != 0:
                val1 = int(self.lcd.value())
                self.lcd.display(0)
                operation = "-"
            
        def add():
            display = self.lcd.value()
            if display != 0:
                val1 = int(self.lcd.value())
                self.lcd.display(0)
                operation = "+"
        def divide():
            display = self.lcd.value()
            if display != 0:
                val1 = int(self.lcd.value())
                self.lcd.display(0)
                operation = "/"
        def multipli():
            display = self.lcd.value()
            if display == 0:
                val1 = int(self.lcd.value())
                self.lcd.display(0)
                operation = "*"
                return operation, val1
        print(multipli()[0])
        def summ(val1, operation):
            global suma
            display = self.lcd.value()
            if display != 0:
                val2 = int(self.lcd.value())
                self.lcd.display(0)
                match operation:
                    case "-":
                        suma = val1 - val2 
                    case "+":
                        suma = val1 + val2
                    case "*":
                        suma = val1 * val2
                    case "/":
                        suma = val1 / val2
                print(suma,val1, val2, operation)
        
        # def
        row1.addWidget(one)
        row1.addWidget(two)
        row1.addWidget(three)
        four = QPushButton("4")
        five = QPushButton("5")
        six = QPushButton("6")
        row2.addWidget(four)
        row2.addWidget(five)
        row2.addWidget(six)
        seven = QPushButton("7")
        eight = QPushButton("8")
        nine = QPushButton("9")
        row3.addWidget(seven)
        row3.addWidget(eight)
        row3.addWidget(nine)
        zero = QPushButton("0")
        one.setFixedSize(100, 100)
        two.setFixedSize(100, 100)
        three.setFixedSize(100, 100)
        four.setFixedSize(100, 100)
        five.setFixedSize(100, 100)
        six.setFixedSize(100, 100)
        seven.setFixedSize(100, 100)
        eight.setFixedSize(100, 100)
        nine.setFixedSize(100, 100)
        vbox.addWidget(self.lcd)

        multi = QPushButton("*")
        plus = QPushButton("+")
        minus = QPushButton("-")
        div = QPushButton("/")
        sum = QPushButton("=")
        multi.clicked.connect(multipli)
        plus.clicked.connect(add)
        minus.clicked.connect(subtract)
        div.clicked.connect(divide)
        sum.clicked.connect(summ)
        multi.setFixedSize(100, 100)
        plus.setFixedSize(100, 100)
        minus.setFixedSize(100, 100)
        div.setFixedSize(140, 100)
        sum.setFixedSize(132, 100)
        zero.setFixedSize(140, 100)
        row1.addWidget(multi)
        row2.addWidget(plus)
        row3.addWidget(minus)
        row4.addWidget(div)
        row4.addWidget(zero)
        row4.addWidget(sum)
        vbox.addStretch()
        vbox.addLayout(row1)
        vbox.addStretch()
        vbox.addLayout(row2)
        vbox.addStretch()
        vbox.addLayout(row3)
        vbox.addStretch()
        vbox.addLayout(row4)
        one.clicked.connect(lambda: write(1))
        two.clicked.connect(lambda: write(2))
        three.clicked.connect(lambda: write(3))
        four.clicked.connect(lambda: write(4))
        five.clicked.connect(lambda: write(5))
        six.clicked.connect(lambda: write(6))
        seven.clicked.connect(lambda: write(7))
        eight.clicked.connect(lambda: write(8))
        nine.clicked.connect(lambda: write(9))
        zero.clicked.connect(lambda: write(0))

        self.setLayout(vbox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
