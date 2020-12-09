import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from gui import main_window
from lang_school import LanguageSchool


class LanguageSchoolApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = LanguageSchoolApp()
    form.show()
    app.exec_()

    db_connection = f"sqlite:///:memory:"
    my_school = LanguageSchool(connection_string=db_connection)

    my_school.add_levels([
        ["A1", "Beginner"],
        ["A2", "Pre-Intermediate"],
        ["B1", "Intermediate"],
        ["B2", "Upper-Intermediate"],
        ["C1", "Advanced"],
        ["C2", "Proficient"]
    ]
    )

    my_school.add_categories(
        [
            'kurs konwersacyjny',
            'kurs biznesowy',
            'kurs dla dorosłych',
            'kurs dla dzieci',
            'kurs egzaminacyjny',
            'cena'
        ]
    )
    my_school.add_languages(
        ['English',
         'Niemiecki',
         'Francuski',
         'Hiszpański',
         'Włoski'
         ]
    )

    levels = my_school.levels()
    for level in levels:
        print(level)
