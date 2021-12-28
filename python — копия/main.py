from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import math
import pyautogui
import tkinter as tk
from tkinter.filedialog import *

# вывод окна
Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# добовление иконки и названия
window.setWindowTitle('КАЛЬКУЛЯТОР ДЛЯ РАСЧЕТА ПЛОЩАДИ СЕЧЕНИЯ АРМАТУРЫ')
window.setWindowIcon(QIcon('calc.png'))

# подсказки для пользователя
form.input_bf.setPlaceholderText("например: 1500")
form.input_hf.setPlaceholderText("например: 50")
form.input_b.setPlaceholderText("например: 200")
form.input_h.setPlaceholderText("например: 400")
form.input_a.setPlaceholderText("например: 80")
form.input_m.setPlaceholderText("например: 260")

# оживляем комбо боксы
form.output_bet_2.addItems(("B10", "B15", "B20", "B25", "B30", "B35", "B40", "B45", "B50", "B55", "B60"))
form.output_bet_3.addItems(("A240", "A300", "A400", "A500"))

bet = {     'B5': 2.8,
            'B10': 6,
            'B15': 8.5,
            'B20': 11.5,
            'B25': 14.5,
            'B30': 17,
            'B35': 19.5,
            'B40': 22,
            'B45': 25,
            'B50': 27.5,
            'B55': 30,
            'B60': 33}

arm = {
            'A240':  215,
            'A300':  270,
            'A400':  355,
            'A500':  435}


def func():
    # ввод переменных
    try:
        input_bf = float(form.input_bf.text())
        input_hf = float(form.input_hf.text())
        input_b = float(form.input_b.text())
        input_h = float(form.input_h.text())
        input_a = float(form.input_a.text())
        input_m = float(form.input_m.text())
        input_rb = bet[form.output_bet_2.currentText()]
        input_rs = arm[form.output_bet_3.currentText()]
    except:
        form.output_as.setText("Поля не заполнены")
        return

# решение задачи
    h0 = input_h - input_a
    alfar = 0.391
    x = input_rb * input_bf * input_hf * (h0 - (1.0 / 2) * input_hf)
    if (x > input_m):
        input_b = input_bf
        y = (input_m * 10 ** 6 / (input_rb * input_bf * h0 * h0))
    elif (x < input_m):
        y = (input_m - input_rb * (h0 - (1.0 / 2) * input_h) - input_rs * (h0 - input_a)) / (
                    input_rb * input_b * h0 ** 2)

    if (y < alfar):
        otvet1 = ((input_rb * input_bf * h0 * (1 - math.sqrt(1 - 2 * y))) / input_rs)
        form.output_as.setText(f'{otvet1}')
    elif (y > alfar):
        otvet2 = ((input_rb * input_b * h0 * (1 - math.sqrt(1 - 2 * y)) + input_rb + input_rs) / input_rs)
        form.output_as.setText(f'{otvet2}')

form.btn_as.clicked.connect(func)

# калькулятор
def calc():
    x = form.input_user.text()
    y = eval(x)
    form.output_otv.setText(f"{y}")

form.btn_calcl.clicked.connect(calc)

# сохранение
def save():
    scr = pyautogui.screenshot()
    save_path = asksaveasfilename()
    scr.save(save_path+"_screenshot.png")

form.odin.clicked.connect(save)

app.exec()