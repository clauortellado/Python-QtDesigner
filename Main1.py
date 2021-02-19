#cargar archivo .ui en código Python

from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])

win = uic.loadUi("MainDesign.ui")

win.show()

sys.exit(app.exec())
