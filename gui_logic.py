from gui import Ui_Dialog
from PyQt5 import QtWidgets


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)
        # Установка пользовательского интерфейс
        self.setupUi(dialog)
        # Обработка нажатий клавиш
        self.pushButton_0.clicked.connect(self.actions_from_0)
        self.pushButton_1.clicked.connect(self.actions_from_1)
        self.pushButton_2.clicked.connect(self.actions_from_2)
        self.pushButton_3.clicked.connect(self.actions_from_3)
        self.pushButton_plus.clicked.connect(lambda: self.set_value("+"))
        self.pushButton_minus.clicked.connect(lambda: self.set_value("-"))
        self.pushButton_calculate.clicked.connect(self.calculate)

    def actions_from_0(self) -> None:
        self.set_value("0")

    def actions_from_1(self) -> None:
        self.set_value("1")

    def actions_from_2(self) -> None:
        self.set_value("2")

    def actions_from_3(self) -> None:
        self.set_value("3")

    def actions_from_plus(self) -> None:
        self.set_value("+")

    def set_value(self, sign: str) -> None:
        text_now = self.label.text()

        if "=" in text_now:
            text_now = ""

        self.label.setText(text_now + sign)

    def calculate(self) -> None:
        text_now = self.label.text()

        if "=" in text_now:
            text_now = ""
        else:
            self.label.setText(text_now+"=")
            print(text_now)
            self.lineEdit.setText(str(eval(text_now)))
