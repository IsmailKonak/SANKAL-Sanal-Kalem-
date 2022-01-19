import sys
from place import idwrite,idread, first
from Kalibrasyon import renk
from PyQt5 import QtCore, QtWidgets
import pyautogui as pg
from Sankal_ana_program import main

screen_size = pg.size()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        posx = (screen_size[0] / 2) - (860 / 2)
        posy = (screen_size[1] / 2) - (550 / 2)
        MainWindow.move(posx, posy)
        MainWindow.resize(860, 550)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baslat = QtWidgets.QPushButton(self.centralwidget)
        self.baslat.setGeometry(QtCore.QRect(300, 210, 260, 80))
        self.baslat.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                  "background-color: rgb(255, 255, 255);")
        self.baslat.setObjectName("baslat")
        self.baslat.clicked.connect(self.run_baby)
        self.ayarlar = QtWidgets.QPushButton(self.centralwidget)
        self.ayarlar.clicked.connect(self.LoadSecondWindow)
        self.ayarlar.setGeometry(QtCore.QRect(340, 420, 171, 71))
        self.ayarlar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);")
        self.ayarlar.setObjectName("ayarlar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 291, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 24pt \"Wide Latin\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.producer = QtWidgets.QLabel(self.centralwidget)
        self.producer.setGeometry(QtCore.QRect(600, 480, 291, 21))
        self.producer.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    'font: 75 10pt "Script MT Bold";')
        self.producer.setAlignment(QtCore.Qt.AlignCenter)
        self.producer.setObjectName("producer")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.show()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SANKAL"))
        self.baslat.setText(_translate("MainWindow", "Başlat"))
        self.ayarlar.setText(_translate("MainWindow", "Kalibrasyon"))
        self.label.setText(_translate("MainWindow", "SANKAL"))
        self.producer.setText(_translate("MainWindow", "İsmail Konak tarafından hazırlandı"))

    def run_baby(self):
        msg = QtWidgets.QMessageBox()
        posx = (screen_size[0] / 2) - (300 / 2)
        posy = (screen_size[1] / 2) - (50 / 2)
        msg.move(posx, posy)
        msg.resize(70, 50)
        msg.setStyleSheet("background-color: rgb(0,0,0);\n"
                          "color: rgb(255, 255, 255);")
        msg.setWindowTitle("   Dikkat   ")
        msg.setText(f'Sanal Kalemden çıkmak için "e" tuşuna basınız.')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.show()
        x = msg.exec_()
        main()

    def LoadSecondWindow(self):
        first()
        SecondWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindowayar()
        ui.setupUi(SecondWindow)
        SecondWindow.show()


class Ui_MainWindowayar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 170)
        posx = (screen_size[0]/2)-(210/2)
        posy = (screen_size[1]/2)-(170/2)
        MainWindow.move(posx,posy)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baslat = QtWidgets.QPushButton(self.centralwidget)
        self.baslat.setGeometry(QtCore.QRect(70, 100, 91, 31))
        self.baslat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.baslat.setObjectName("baslat")
        self.baslat.clicked.connect(self.ayar_basla)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(140, 40, 42, 22))
        try:
            a = idread()
            self.spinBox.setValue(int(a))
        except FileNotFoundError:
            self.spinBox.setValue(0)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.show()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalibrasyon"))
        self.baslat.setText(_translate("MainWindow", "Başlat "))
        self.label.setText(_translate("MainWindow", "Kamera ID"))

    def ayar_basla(self):
        self.id = self.spinBox.value()
        idwrite(self.id)
        msg = QtWidgets.QMessageBox()
        posx = (screen_size[0] / 2) - (350 / 2)
        posy = (screen_size[1] / 2) - (50 / 2)
        msg.move(posx,posy)
        msg.resize(350,100)
        msg.setStyleSheet("background-color: rgb(0,0,0);\n"
                          "color: rgb(255, 255, 255);")
        msg.setWindowTitle("   Dikkat   ")
        msg.setText(f'Kalibrasyonları kaydedip çıkmak için "q" tuşuna basınız.'
                    f'Not: Değişikliklerin kaydedilmesi için programı tekrardan başlatınız.')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.show()
        x = msg.exec_()
        print(self.id)
        renk()



class Controller:

    def __init__(self):
        pass

    def Show_FirstWindow(self):
        self.FirstWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.FirstWindow)
        self.ui.ayarlar.clicked.connect(self.Show_SecondWindow)
        self.FirstWindow.show()

    def Show_SecondWindow(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowayar()
        self.ui.setupUi(self.SecondWindow)
        self.SecondWindow.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())