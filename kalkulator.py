#!/usr/bin/python3
"""
Python QT
Opis modułu jako całości
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from mnoz import DivMul

ts = DivMul()

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi('main_ui.ui', self)
		self.znak = 'x'
		self.znaki = '0'
		self.ilosc = 50		

		self.tabWidget.setCurrentIndex(0)
		self.tabWidget.tabBar().hide()
		self.btn_start.clicked.connect(self.open_calc_dialog)
		self.btn_del.clicked.connect(self.usun)
		self.btn_wynik.clicked.connect(self.sprawdz)
		self.btn_0.clicked.connect(lambda: self.btn_clk('0'))
		self.btn_1.clicked.connect(lambda: self.btn_clk('1'))
		self.btn_2.clicked.connect(lambda: self.btn_clk('2'))
		self.btn_3.clicked.connect(lambda: self.btn_clk('3'))
		self.btn_4.clicked.connect(lambda: self.btn_clk('4'))
		self.btn_5.clicked.connect(lambda: self.btn_clk('5'))
		self.btn_6.clicked.connect(lambda: self.btn_clk('6'))
		self.btn_7.clicked.connect(lambda: self.btn_clk('7'))		
		self.btn_8.clicked.connect(lambda: self.btn_clk('8'))
		self.btn_9.clicked.connect(lambda: self.btn_clk('9'))
		self.btn_restart.clicked.connect(self.restartuj)
	
	def gen_rownanie(self):
		self.znaki = '0'
		self.labNumer.setText(f'Zadanie {ts.aktualne} z {ts.liczba_zadan}')
		if not ts.koniec_listy:
			ts.pobierz_pytanie()
		self.lineZadanie.setText(ts.rownanie)

	def btn_clk(self, txt):
		if not ts.koniec_listy:
			if len(self.znaki) < 4:
				self.znaki = (self.znaki + txt).lstrip("0")
				self.lineZadanie.setText(ts.rownanie + self.znaki)

	def usun(self):		
		self.znaki = self.znaki[:-1]
		if self.znaki == '':
			self.znaki = '0'
			self.lineZadanie.setText(ts.rownanie)
		else:
			self.lineZadanie.setText(ts.rownanie + self.znaki)

	def sprawdz(self):
		ts.sprawdz_wynik(int(self.znaki))
		# if ts.ok:
		#     self.lbl.color = [0, 1, 0, 1]
		# if ts.nok:
		#     self.lbl.color = [1, 0, 0, 1]
		# time.sleep(0.5)
		self.gen_rownanie()
		if ts.koniec_listy:
			self.labWynik.setText(f'Poprawnie: {str(ts.liczba_zadan - len(ts.bledy))} na {str(ts.liczba_zadan)}')
			self.labWynik_zly.setText(f'Błędy: {len(ts.bledy)}')
			self.listZle.clear()
			for i in ts.bledy:
				widgitItem = QtWidgets.QListWidgetItem() 
				widget = QtWidgets.QWidget()
				widgetText =  QtWidgets.QLabel(f'{i[0]}<font color=#ff0000>{i[1]},</font><font color=#00aa00> poprawnie <b>{i[2]}</b></font>')
				widgetLayout = QtWidgets.QHBoxLayout()
				widgetLayout.addWidget(widgetText)
				widget.setLayout(widgetLayout)
				widgitItem.setSizeHint(QtCore.QSize(widget.sizeHint().width(), 46))
				self.listZle.addItem(widgitItem)
				 
				self.listZle.setItemWidget(widgitItem, widget)

			self.tabWidget.setCurrentIndex(2)

	def restartuj(self):
		self.tabWidget.setCurrentIndex(0)

	def open_calc_dialog(self):
		if self.btn_mul.isChecked():
			self.znak = 'x'
		elif self.btn_div.isChecked():
			self.znak = ':'

		if self.btn_50.isChecked():
			self.ilosc = 50
		elif self.btn_30.isChecked():
			self.ilosc = 30
		elif self.btn_10.isChecked():
			self.ilosc = 10

		ts.generuj_test(self.znak, self.ilosc)
		self.gen_rownanie()
		self.tabWidget.setCurrentIndex(1)

def main():
	'''
	Główna funkcja modułu.
	'''
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
	

if __name__ == '__main__':
    main()
