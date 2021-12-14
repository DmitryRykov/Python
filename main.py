import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

class calc (QtWidgets.QMainWindow):
    def __init__(self):
        super(calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Подсчитай-ка!')
        self.setWindowIcon(QIcon('iconka.png'))
        self.ui.btn.clicked.connect(self.run)
        self.ui.pushButton.clicked.connect(self.runs)

    def function(self):
        input_a = float(self.ui.input_a.text())
        input_bf = float(self.ui.input_bf.text())
        input_hf = float(self.ui.input_hf.text())
        input_b = float(self.ui.input_b.text())
        input_h = float(self.ui.input_h.text())
        input_rb = float(self.ui.input_rb.text())
        input_rs = float(self.ui.input_rs.text())
        input_m = float(self.ui.input_m.text())
        input_user = float(self.ui.input_user.text())
        output_s = self.ui.output_S.text()
        output_ot = self.ui.output_f.text()

    def runs(self):
        input_a = float(self.ui.input_a.text())
        input_h = float(self.ui.input_h.text())
        input_hf = float(self.ui.input_hf.text())
        input_rb = float(self.ui.input_rb.text())
        input_bf = float(self.ui.input_bf.text())
        input_m = float(self.ui.input_m.text())
        input_b = float(self.ui.input_b.text())
        input_rs = float(self.ui.input_rs.text())

        h0 = input_h - input_a
        alfar = 0.391
        x = input_rb * input_bf * input_hf * (h0 - (1.0/2) * input_hf)
        if (x > input_m):
            input_b = input_bf
            y = (input_m * 10 ** 6 / (input_rb * input_bf * h0 * h0))
        elif (x < input_m):
            y = (input_m - input_rb * (h0 - (1.0/2)*input_h) - input_rs * (h0 - input_a)) / (input_rb * input_b * h0**2)

        if (y < alfar):
            otvet1 = ((input_rb * input_bf * h0 * (1 - math.sqrt(1 - 2 * y))) / input_rs)
            self.ui.output_S.setText(f'{otvet1:.1f}')
        elif (y > alfar):
            otvet2 = ((input_rb * input_b * h0 * (1 - math.sqrt(1 - 2 * y)) + input_rb + input_rs) / input_rs)
            self.ui.output_S.setText(f'{otvet2:.1f}')


    def run(self):
        output_ot = self.ui.output_f.text()
        input_user = self.ui.input_user.text()
        x = self.ui.input_user.text()
        y = eval(x)
        self.ui.output_f.setText(f"{y}")




app = QtWidgets.QApplication([])
application = calc()
application.show()

sys.exit(app.exec())

