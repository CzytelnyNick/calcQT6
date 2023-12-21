import sys
import math
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
import re
operation = ""
val1 = 0
operation2 = ""
val2 = 0
suma = 0
dotCheck = 0
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
        self.setFixedSize(400, 600)
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        row5 = QHBoxLayout()
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
            global dotCheck
            global operation2
            display = self.lcd.value()
            print(display)
            if display != 0.0:
                if operation2 == "dot":
                    if dotCheck == 0:
                        self.lcd.display(f"{str(int(display))}.{str(number)}")
                        dotCheck = 1
                        print(dotCheck)
                    else: 
                         print(dotCheck)
                         self.lcd.display(f"{str((display)) + str(number)}")
                else:
                    self.lcd.display(f"{str(int(display)) + str(number)}")
            else:
                if operation2 == "dot":
                    if dotCheck == 0:
                        self.lcd.display(f"0.{str(number)}")
                        dotCheck = 1
                        print(dotCheck)
                    else: 
                         print(dotCheck)
                         self.lcd.display(f"{str(float(display)) + str(number)}")
                else:
                     self.lcd.display(f"{str(number)}")
            
        def subtract():
            global val1, operation, operation2
            operation2 = ""
            display = self.lcd.value()
            if display != 0 and operation == "":
                val1 = float(self.lcd.value())
                self.lcd.display(0)
                operation = "-"
            
        def add():
                global val1, operation, operation2
                display = self.lcd.value()
            
                val1 = float(self.lcd.value())
                self.lcd.display(0)
                operation = "+"
                operation2 = ""
        def divide():
                global val1, operation, operation2
                display = self.lcd.value()
                operation2 = ""
            
                
                val1 = float(self.lcd.value())
                self.lcd.display(0)
                operation = "/"
        def multipli():
                global val1, operation, operation2
                display = self.lcd.value()

            
                val1 = float(self.lcd.value())
                self.lcd.display(0)
                operation2 = ""
                operation = "*"
                return operation, val1
        def minuss():
                global val1, operation, operation2
                display = float(self.lcd.value())
                operation2 = ""
            
                val1 = display
                self.lcd.display(int(display * -1))
                return operation, val1
        # print()
        def sqrtFunc():
                global val1,operation2
                display = float(self.lcd.value())
            
                val1 = display
                operation = "sqrt"
                operation2 = ""
                if self.lcd.value() >= 0:
                            self.lcd.display(math.sqrt(self.lcd.value()))
                else:
                            self.lcd.display("Error") 
                return operation, val1
        def dotFunc():
            global operation2,dotCheck
            display = float(self.lcd.value())
            dotCheck = 0
            haveDot = (str(self.lcd.value())).find(".")
            print(haveDot, str(self.lcd.value()))
            val1 = f"{str(int(display))}."
            operation2 = "dot"
            print(val1)
            self.lcd.display(val1)
        def clearFunc():
             global val1, val2, operation, operation2, suma
             val1 = ""
             val2 = ""
             operation = ""
             operation2 = ""
             
             self.lcd.display(0)
             suma = self.lcd.value()
        def summ():
            if self.lcd.value() != "Error":
                 
                global suma, operation,operation2
                display = self.lcd.value()
                
                print(operation)
                val2 = float(self.lcd.value())
                self.lcd.display(0)
                match operation:
                    case "-":
                            suma = val1 - val2 
                    case "+":
                            suma = val1 + val2
                    case "*":
                            suma = val1 * val2
                    case "/":
                        if not math.isnan(val2) and val2 != 0.0:
                            suma = val1 / val2
                        else:
                            self.lcd.display("Error")
                print(suma,val1, val2, operation)
                self.lcd.display(suma)
                operation=""
                operation2=""
            else:
                 self.lcd.display(0)
        
        # def
        sqrt = QPushButton("√")
        dot = QPushButton(".")
        clear = QPushButton("C")
        clear.setFixedSize(140,100)
        clear.clicked.connect(clearFunc)
        sqrt.setFixedSize(140, 100)
        dot.setFixedSize(100, 100)
        
        row5.addWidget(clear)
        row5.addWidget(sqrt)
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
        minusss = QPushButton("-/+")
        minusss.setFixedSize(100,100)
        multi = QPushButton("*")
        plus = QPushButton("+")
        minus = QPushButton("-")
        div = QPushButton("/")
        sum = QPushButton("=")
        minusss.clicked.connect(minuss)
        multi.clicked.connect(multipli)
        plus.clicked.connect(add)
        minus.clicked.connect(subtract)
        div.clicked.connect(divide)
        sum.clicked.connect(summ)
        sqrt.clicked.connect(sqrtFunc)
        dot.clicked.connect(dotFunc)
        multi.setFixedSize(100, 100)
        plus.setFixedSize(100, 100)
        minus.setFixedSize(100, 100)
        div.setFixedSize(100, 100)
        sum.setFixedSize(132, 100)
        zero.setFixedSize(100, 100)
        row1.addWidget(multi)
        row2.addWidget(plus)
        row3.addWidget(minus)
        row4.addWidget(div)
        row4.addWidget(zero)
        row4.addWidget(dot)
        row4.addWidget(minusss)
        # row4.addWidget()
        # row5.addWidget(minusss)
        row5.addWidget(sum)
        
        vbox.addStretch()
        vbox.addLayout(row1)
        vbox.addStretch()
        vbox.addLayout(row2)
        vbox.addStretch()
        vbox.addLayout(row3)
        vbox.addStretch()
        vbox.addLayout(row4)
        vbox.addStretch()
        vbox.addLayout(row5)
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
