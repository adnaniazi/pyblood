from PyQt4.QtGui import *
from PyQt4.QtCore import *

from my_gui import Ui_MainWindow

class MyMainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)
        self.comboBox_bloodChecker.currentIndexChanged.connect(self.can_donate_or_receive)
        self.comboBox_parent1.currentIndexChanged.connect(self.calculate_inherited_blood_type)
        self.comboBox_parent2.currentIndexChanged.connect(self.calculate_inherited_blood_type)
        self.row_count = 1
        app.setStyle(QStyleFactory.create('plastique'))

        # hide vertical header of the table as there is only one line
        v_header = self.tableWidget.verticalHeader()
        v_header.hide()

    def can_donate_or_receive(self):
        """Logic for matching blood types for safe transfusion"""

        selected_item = self.comboBox_bloodChecker.currentText()
        if selected_item == 'O':
                self.textEdit_donate_to.setPlainText('O \nA \nB \nAB')
                self.textEdit_receive_from.setPlainText('O')
        elif selected_item == 'A':
                self.textEdit_donate_to.setPlainText('A \nAB')
                self.textEdit_receive_from.setPlainText('O \nA')
        elif selected_item == 'B':
                self.textEdit_donate_to.setPlainText('B \nAB')
                self.textEdit_receive_from.setPlainText('O \nB')
        elif selected_item == 'AB':
               self.textEdit_donate_to.setPlainText('AB')
               self.textEdit_receive_from.setPlainText('O \nA \nB \nAB')
        else:
               self.textEdit_donate_to.setPlainText('')
               self.textEdit_receive_from.setPlainText('')

    def calculate_inherited_blood_type(self):
        """Logic for calculating possible blood types in progeny depending
        on blood type of parents"""

        parent1_text = self.comboBox_parent1.currentText()
        parent2_text = self.comboBox_parent2.currentText()
        if parent1_text == 'Select a blood type' or parent2_text == 'Select a blood type':
            self.tableWidget.setItem(0, 0, QTableWidgetItem(''))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(''))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(''))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(''))
            return
        else:
            self.tableWidget.setRowCount(self.row_count)
            if (parent1_text == 'AB' and parent2_text == 'AB') or \
                    (parent1_text == 'AB' and parent2_text == 'A') or \
                    (parent1_text == 'A' and parent2_text == 'AB') or \
                    (parent1_text == 'AB' and parent2_text == 'B') or \
                    (parent1_text == 'B' and parent2_text == 'AB'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('Yes'))
            elif (parent1_text == 'AB' and parent2_text == 'O') or\
                    (parent1_text == 'O' and parent2_text == 'AB'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('No'))
            elif (parent1_text == 'B' and parent2_text == 'B') or\
                    (parent1_text == 'O' and parent2_text == 'B') or\
                    (parent1_text == 'B' and parent2_text == 'O'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('No'))            
            elif (parent1_text == 'A' and parent2_text == 'B') or\
                    (parent1_text == 'B' and parent2_text == 'A'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('Yes'))            
            elif (parent1_text == 'A' and parent2_text == 'A') or\
                    (parent1_text == 'O' and parent2_text == 'A') or\
                    (parent1_text == 'A' and parent2_text == 'O'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('No'))            
            elif (parent1_text == 'O' and parent2_text == 'O'):
                 self.tableWidget.setItem(0, 0, QTableWidgetItem('Yes'))
                 self.tableWidget.setItem(0, 1, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 2, QTableWidgetItem('No'))
                 self.tableWidget.setItem(0, 3, QTableWidgetItem('No'))
            else:
                print('Error: Unknown case')

            # center all items
            item_O = self.tableWidget.item(0, 0)
            item_O.setTextAlignment(Qt.AlignCenter)
            item_A = self.tableWidget.item(0, 1)
            item_A.setTextAlignment(Qt.AlignCenter)
            item_B = self.tableWidget.item(0, 2)
            item_B.setTextAlignment(Qt.AlignCenter)
            item_AB = self.tableWidget.item(0, 3)
            item_AB.setTextAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())