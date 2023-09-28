#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 559)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(30, 20, 470, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        
        self.percentButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(30, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        
        self.cButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("C"))
        self.cButton_2.setGeometry(QtCore.QRect(90, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cButton_2.setFont(font)
        self.cButton_2.setObjectName("cButton_2")
        
        self.sqrtButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.sqrt_it())
        self.sqrtButton.setGeometry(QtCore.QRect(270, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sqrtButton.setFont(font)
        self.sqrtButton.setObjectName("sqrtButton")
        
        self.divideButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("/"))
        self.divideButton_4.setGeometry(QtCore.QRect(210, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.divideButton_4.setFont(font)
        self.divideButton_4.setObjectName("divideButton_4")
        
        self.arrowButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.remove_it())
        self.arrowButton_3.setGeometry(QtCore.QRect(150, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.arrowButton_3.setFont(font)
        self.arrowButton_3.setObjectName("arrowButton_3")
        
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(30, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        
        self.eightButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(90, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        
        self.powButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pow_it())
        self.powButton.setGeometry(QtCore.QRect(270, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.powButton.setFont(font)
        self.powButton.setObjectName("powButton")
        
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(210, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        
        self.nineButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(150, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        
        self.fourButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(30, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(90, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        
        self.logButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("log"))
        self.logButton.setGeometry(QtCore.QRect(270, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        
        self.minusButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(210, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        
        self.sixButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(150, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        
        self.oneButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(30, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        
        self.twoButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(90, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        
        self.factorialButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("!"))
        self.factorialButton.setGeometry(QtCore.QRect(270, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.factorialButton.setFont(font)
        self.factorialButton.setObjectName("factorialButton")
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(210, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        
        self.threeButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(150, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        
        self.plusminus = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.plus_minus_it())
        self.plusminus.setGeometry(QtCore.QRect(30, 350, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(90, 350, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        
        self.equalButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(210, 350, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(150, 350, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        
        self.absButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.abs_it())
        self.absButton.setGeometry(QtCore.QRect(330, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.absButton.setFont(font)
        self.absButton.setObjectName("absButton")
        
        self.piButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pi_it())
        self.piButton.setGeometry(QtCore.QRect(330, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.piButton.setFont(font)
        self.piButton.setObjectName("piButton")
        
        self.eButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.exp_it())
        self.eButton.setGeometry(QtCore.QRect(330, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.eButton.setFont(font)
        self.eButton.setObjectName("eButton")
        
        self.reciprocalButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.reciprocal_it())
        self.reciprocalButton.setGeometry(QtCore.QRect(330, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reciprocalButton.setFont(font)
        self.reciprocalButton.setObjectName("reciprocalButton")
        
            
        self.ToBinaryButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.Binary_it())
        self.ToBinaryButton.setGeometry(QtCore.QRect(270, 350, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ToBinaryButton.setFont(font)
        self.ToBinaryButton.setObjectName("ToBinaryButton")    
        
        self.sinbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.sin_it())
        self.sinbutton.setGeometry(QtCore.QRect(390, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sinbutton.setFont(font)
        self.sinbutton.setObjectName("sinbutton")    
        
        self.cosbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.cos_it())
        self.cosbutton.setGeometry(QtCore.QRect(390, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cosbutton.setFont(font)
        self.cosbutton.setObjectName("cosbutton")   
        
        self.tanbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.tan_it())
        self.tanbutton.setGeometry(QtCore.QRect(390, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tanbutton.setFont(font)
        self.tanbutton.setObjectName("tanbutton") 
   
        self.cotButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.cot_it())
        self.cotButton.setGeometry(QtCore.QRect(450, 230, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cotButton.setFont(font)
        self.cotButton.setObjectName("cotButton")  
        
        self.secButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.sec_it())
        self.secButton.setGeometry(QtCore.QRect(450, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.secButton.setFont(font)
        self.secButton.setObjectName("secButton")  
      
        self.cscButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.csc_it())
        self.cscButton.setGeometry(QtCore.QRect(450, 170, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cscButton.setFont(font)
        self.cscButton.setObjectName("cscButton")

        self.bracketleftButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("("))
        self.bracketleftButton.setGeometry(QtCore.QRect(390, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bracketleftButton.setFont(font)
        self.bracketleftButton.setObjectName("bracketleftButton")

        self.bracketrightButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it(")"))
        self.bracketrightButton.setGeometry(QtCore.QRect(450, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bracketrightButton.setFont(font)
        self.bracketrightButton.setObjectName("bracketrightButton")                 
   
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def math_it(self):
        global math
        screen = self.outputLabel.text()
        try:
            if "log" in screen:
                answer = round(math.log10(float(screen[3:])),4)
#             elif "sqrt" in screen:
#                 answer = round(math.sqrt(float(screen[1:])),4)
            elif "!" in screen:
                answer = round(math.factorial(float(screen[:-1])))
#             elif "abs" in screen:
#                 answer = abs(float(screen[3:]))    
            else:  
                answer=eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")
            
    def sqrt_it(self):
        try:
            screen = float(self.outputLabel.text())
            answer = round(math.sqrt(float(screen)),4)
            self.outputLabel.setText(str(answer))
            
        except:
            self.outputLabel.setText("ERROR")      
            
    def abs_it(self):
        try:
            screen = float(self.outputLabel.text())
            answer = abs(screen)
            self.outputLabel.setText(str(answer))
            
        except:
            self.outputLabel.setText("ERROR")   
    
    def pi_it(self):
        try:
            pi = round(math.pi,4)
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{str(pi)}')
            
        except:
            self.outputLabel.setText("ERROR")        
    
    def exp_it(self):
        try:
            exp = round(math.exp(1),4)
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{str(exp)}')
            
        except:
            self.outputLabel.setText("ERROR")          
        
    def sin_it(self):
        try:
            screen = float(self.outputLabel.text())
            sin = round(math.sin(screen*math.pi/180),4)
            self.outputLabel.setText(str(sin))
        except:
            self.outputLabel.setText("ERROR")        
    
    def cos_it(self):
        try:
            screen = float(self.outputLabel.text())
            cos = round(math.cos(screen*math.pi/180),4)
            self.outputLabel.setText(str(cos))
        except:
            self.outputLabel.setText("ERROR")    
        
    def tan_it(self):
        try:
            screen = float(self.outputLabel.text())
            tan = round(math.tan(screen*math.pi/180),4)
            self.outputLabel.setText(str(tan))
        except:
            self.outputLabel.setText("ERROR")    

    def cot_it(self):
        try:
            screen=float(self.outputLabel.text())
            tan=round(math.tan(screen*math.pi/180),4)
            cot=round(1/tan,4)
            self.outputLabel.setText(str(cot))
        except:
            self.outputLabel.setText("ERROR")
        
    def sec_it(self):
        try:
            screen=float(self.outputLabel.text())
            cos=round(math.cos(screen*math.pi/180),4)
            sec=round(1/cos,4)
            self.outputLabel.setText(str(sec))
        except:
            self.outputLabel.setText("ERROR")    
        
    def csc_it(self):
        try:
            screen=float(self.outputLabel.text())
            sin=round(math.sin(screen*math.pi/180),4)
            csc=round(1/sin,4)
            self.outputLabel.setText(str(csc))
        except:
            self.outputLabel.setText("ERROR")  

    def pow_it(self):
        try:
            screen=self.outputLabel.text()
            self.outputLabel.setText(f'{screen}**')        
        except:
            self.outputLabel.setText("ERROR")
                    
    def plus_minus_it(self):
        screen=self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-",""))
        else:
            self.outputLabel.setText(f'-{screen}')

    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1]==".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')
            
    def reciprocal_it(self):
        screen = self.outputLabel.text()
        answer = float(screen)
        reciprocal=round((1/answer),4)
        self.outputLabel.setText(str(reciprocal))

    def press_it(self,pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    
    def Binary_it(self):
        try:
            screen=int(self.outputLabel.text())
            Binary=format(screen, '08b')
            self.outputLabel.setText(str(Binary))
        except:
                self.outputLabel.setText("ERROR")
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculater"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton_2.setText(_translate("MainWindow", "C"))
        self.sqrtButton.setText(_translate("MainWindow", "√"))
        self.divideButton_4.setText(_translate("MainWindow", "÷"))
        self.arrowButton_3.setText(_translate("MainWindow", "<<"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.powButton.setText(_translate("MainWindow", "pow"))
        self.multiplyButton.setText(_translate("MainWindow", "×"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.logButton.setText(_translate("MainWindow", "log"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.factorialButton.setText(_translate("MainWindow", "n!"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusminus.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.absButton.setText(_translate("MainWindow", "|x|"))
        self.piButton.setText(_translate("MainWindow", "π"))
        self.eButton.setText(_translate("MainWindow", "e"))
        self.reciprocalButton.setText(_translate("MainWindow", "1/x"))
        self.ToBinaryButton.setText(_translate("MainWindow", "ToBinary"))
        self.sinbutton.setText(_translate("MainWindow", "sin"))
        self.cosbutton.setText(_translate("MainWindow", "cos"))
        self.tanbutton.setText(_translate("MainWindow", "tan"))
        self.cotButton.setText(_translate("MainWindow", "cot"))
        self.secButton.setText(_translate("MainWindow", "sec"))
        self.cscButton.setText(_translate("MainWindow", "csc"))
        self.bracketleftButton.setText(_translate("MainWindow", "("))
        self.bracketrightButton.setText(_translate("MainWindow", ")"))

if __name__ == '__main__':
    import sys
    import math
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# In[ ]:





# In[ ]:




