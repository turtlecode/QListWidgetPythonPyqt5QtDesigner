from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from listview import Ui_MainWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStudents()
        self.ui.add_button.clicked.connect(self.addStudent)
        self.ui.edit_button.clicked.connect(self.editStudent)
        self.ui.remove_button.clicked.connect(self.removeStudent)
        self.ui.up_button.clicked.connect(self.upStudent)
        self.ui.down_button.clicked.connect(self.downStudent)
        self.ui.sort_button.clicked.connect(self.sortStudent)
        self.ui.exit_button.clicked.connect(self.exitDesktopApp)

    def loadStudents(self):
        self.ui.list_object.addItems(['Adam','Axel','Washington','Gilbert'])
        self.ui.list_object.setCurrentRow(1)

    def addStudent(self):
        currentIndex = self.ui.list_object.currentRow()
        text, ok = QInputDialog.getText(self,"New Student","Student Name")
        if ok and text is not None:
            self.ui.list_object.insertItem(currentIndex,text)

    def editStudent(self):
        currentIndex = self.ui.list_object.currentRow()
        item = self.ui.list_object.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        currentIndex = self.ui.list_object.currentRow()
        item = self.ui.list_object.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self,"Remove Student",
                                        "Do you want to remove student?" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.list_object.takeItem(currentIndex)
            del item

    def upStudent(self):
        index = self.ui.list_object.currentRow()
        if index >= 1:
            item = self.ui.list_object.takeItem(index)
            self.ui.list_object.insertItem(index-1,item)
            self.ui.list_object.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.list_object.currentRow()
        if index < self.ui.list_object.count()-1:
            item = self.ui.list_object.takeItem(index)
            self.ui.list_object.insertItem(index + 1, item)
            self.ui.list_object.setCurrentItem(item)

    def sortStudent(self):
        self.ui.list_object.sortItems()

    def exitDesktopApp(self):
        question = QMessageBox.question(self,"Exit App?",
                                        "Do you want to quit?",
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            quit()





def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()
