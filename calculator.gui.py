from typing import Self
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from interface import *
import sys
from PyQt6 import *



class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.my_result =''
        self.result = ''
        self.lineEdit.setText(self.result)
        self.pushButton_multiply.clicked.connect(self.multiply)
        self.pushButto_delimetr.clicked.connect(self.delimetr)
        self.pushButton_point.clicked.connect(self.point)
        self.pushButton_1.clicked.connect(self.add_1)
        self.pushButton_2.clicked.connect(self.add_2)
        self.pushButton_3.clicked.connect(self.add_3)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_deleter.clicked.connect(self.deleter)
        self.pushButton_4.clicked.connect(self.add_4) 
        self.pushButton_5.clicked.connect(self.add_5)
        self.pushButton_6.clicked.connect(self.add_6)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_7.clicked.connect(self.add_7)
        self.pushButton_8.clicked.connect(self.add_8)
        self.pushButton_9.clicked.connect(self.add_9)
        self.pushButton_0.clicked.connect(self.add_0)
        self.pushButton_plus_or_minus.clicked.connect(self.add_plus_or_minus)
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_result.clicked.connect(self.result_count)

    def add_0(self):
        self.result += '0'
        self.lineEdit.setText(self.result)
    
    def add_1(self):
        self.result +='1'
        self.lineEdit.setText(self.result)
        
    
    def add_2(self):
        self.result += '2'
        self.lineEdit.setText(self.result)


    def add_3(self):
        self.result += '3'
        self.lineEdit.setText(self.result)

        
    
    def add_4(self):
        self.result += '4'
        self.lineEdit.setText(self.result)


    def add_5(self):
        self.result += '5'
        self.lineEdit.setText(self.result)


    def add_6(self):
        self.result +='6'
        self.lineEdit.setText(self.result)


    def add_7(self):
        self.result +='7'
        self.lineEdit.setText(self.result)

    
    def add_8(self):
        self.result +='8'
        self.lineEdit.setText(self.result)

    
    def add_9(self):
        self.result += '9'
        self.lineEdit.setText(self.result)


    def multiply(self):
        self.result +='*'
        self.lineEdit.setText(self.result)

    
    def minus(self):
        self.result +='-'
        self.lineEdit.setText(self.result)

    
    def plus(self):
        self.result +='+'
        self.lineEdit.setText(self.result)

    
    def point(self):
        self.result += '.'
        self.lineEdit.setText(self.result)

    
    def delimetr(self):
        self.result += '/'
        self.lineEdit.setText(self.result)


    def add_plus_or_minus(self):
        if self.result[0] !='-':
            self.result = '-' + self.result
            self.lineEdit.setText(self.result)

        else:
            self.result = self.result.replace(self.result[0],'')
            self.lineEdit.setText(self.result)
            
    def reset(self):
        self.result = ''
        self.lineEdit.setText(self.result)

    
    def deleter(self):
        self.result = self.result.replace(self.result[-1],'')
        self.lineEdit.setText(self.result)


   
    def result_count(self):
        if len(self.result)> 10:
            self.lineEdit.setText('LIMIT ERROR')

        try:
            self.my_result = eval(self.result)
            self.lineEdit.setText(str(eval(self.result)))
        except ZeroDivisionError:
            self.lineEdit.setText('ZeroDivisionError')
        except TypeError:
            self.lineEdit.setText('ZeroDivisionError')
        except SyntaxError:
            self.lineEdit.setText('SyntaxError')
        except IndexError:
             self.lineEdit.setText('IndexError')




app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())