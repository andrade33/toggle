
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import sys

class RegApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegApp, self).__init__(parent=parent)
        self.setupUi(self)

        self.toggleBtn.clicked.connect(lambda: self.openLeftTab_menu())

    def openLeftTab_menu(self):
        
        width = self.left.width()
        if width == 0:
            newWid = 150;
        else:
            newWid = 0

        self.animation = QPropertyAnimation(self.left, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWid)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegApp()
    window.show()
    sys.exit(app.exec())