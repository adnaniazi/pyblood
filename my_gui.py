# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created: Sun Jul  5 11:21:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(449, 388)
        MainWindow.setMinimumSize(QtCore.QSize(446, 388))
        MainWindow.setMaximumSize(QtCore.QSize(470, 388))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/blood_drop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(429, 329))
        self.tabWidget.setMaximumSize(QtCore.QSize(429, 329))
        self.tabWidget.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"Background:transparent;\n"
"\n"
"}"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_8.addWidget(self.label_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.comboBox_bloodChecker = QtGui.QComboBox(self.tab)
        self.comboBox_bloodChecker.setObjectName(_fromUtf8("comboBox_bloodChecker"))
        self.comboBox_bloodChecker.addItem(_fromUtf8(""))
        self.comboBox_bloodChecker.addItem(_fromUtf8(""))
        self.comboBox_bloodChecker.addItem(_fromUtf8(""))
        self.comboBox_bloodChecker.addItem(_fromUtf8(""))
        self.comboBox_bloodChecker.addItem(_fromUtf8(""))
        self.verticalLayout_7.addWidget(self.comboBox_bloodChecker)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolButton_3 = QtGui.QToolButton(self.tab)
        self.toolButton_3.setToolTip(_fromUtf8(""))
        self.toolButton_3.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"Background:transparent;\n"
"\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/blood_recive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.verticalLayout.addWidget(self.toolButton_3)
        self.label = QtGui.QLabel(self.tab)
        self.label.setToolTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.textEdit_receive_from = QtGui.QPlainTextEdit(self.tab)
        self.textEdit_receive_from.setToolTip(_fromUtf8(""))
        self.textEdit_receive_from.setObjectName(_fromUtf8("textEdit_receive_from"))
        self.horizontalLayout_4.addWidget(self.textEdit_receive_from)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.toolButton_4 = QtGui.QToolButton(self.tab)
        self.toolButton_4.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"Background:transparent;\n"
"\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/blood_donate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.verticalLayout_6.addWidget(self.toolButton_4)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.textEdit_donate_to = QtGui.QPlainTextEdit(self.tab)
        self.textEdit_donate_to.setObjectName(_fromUtf8("textEdit_donate_to"))
        self.horizontalLayout_5.addWidget(self.textEdit_donate_to)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.toolButton_2 = QtGui.QToolButton(self.tab_3)
        self.toolButton_2.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"Background:transparent;\n"
"\n"
"}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/parent_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon3)
        self.toolButton_2.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboBox_parent1 = QtGui.QComboBox(self.tab_3)
        self.comboBox_parent1.setObjectName(_fromUtf8("comboBox_parent1"))
        self.comboBox_parent1.addItem(_fromUtf8(""))
        self.comboBox_parent1.addItem(_fromUtf8(""))
        self.comboBox_parent1.addItem(_fromUtf8(""))
        self.comboBox_parent1.addItem(_fromUtf8(""))
        self.comboBox_parent1.addItem(_fromUtf8(""))
        self.verticalLayout_4.addWidget(self.comboBox_parent1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(self.tab_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.toolButton = QtGui.QToolButton(self.tab_3)
        self.toolButton.setStyleSheet(_fromUtf8("QToolButton\n"
"{\n"
"Background:transparent;\n"
"\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/parent_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon4)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.comboBox_parent2 = QtGui.QComboBox(self.tab_3)
        self.comboBox_parent2.setObjectName(_fromUtf8("comboBox_parent2"))
        self.comboBox_parent2.addItem(_fromUtf8(""))
        self.comboBox_parent2.addItem(_fromUtf8(""))
        self.comboBox_parent2.addItem(_fromUtf8(""))
        self.comboBox_parent2.addItem(_fromUtf8(""))
        self.comboBox_parent2.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.comboBox_parent2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_10.addWidget(self.label_7)
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: transparent;\n"
"border: none;\n"
"}"))
        self.pushButton_3.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/iib-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(130, 60))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_10.addWidget(self.pushButton_3)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_10.addWidget(self.label_11)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: transparent;\n"
"border: none;\n"
"}"))
        self.pushButton_4.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/email.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_9.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_10.addWidget(self.label_15)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: transparent;\n"
"border: none;\n"
"}"))
        self.pushButton_2.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cc_license.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QtCore.QSize(88, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_10.addWidget(self.pushButton_2)
        spacerItem6 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBlood", None))
        self.label_5.setText(_translate("MainWindow", "Choose a blood type below and you will know the specific ways in which \n"
"blood types must be matched for safe transfusion", None))
        self.comboBox_bloodChecker.setItemText(0, _translate("MainWindow", "Select a blood type:", None))
        self.comboBox_bloodChecker.setItemText(1, _translate("MainWindow", "O", None))
        self.comboBox_bloodChecker.setItemText(2, _translate("MainWindow", "A", None))
        self.comboBox_bloodChecker.setItemText(3, _translate("MainWindow", "B", None))
        self.comboBox_bloodChecker.setItemText(4, _translate("MainWindow", "AB", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Can\n"
"receive\n"
"blood\n"
"from: ", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Can\n"
"donate\n"
"blood\n"
"to:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Safe blood transfusion", None))
        self.label_6.setText(_translate("MainWindow", "Please choose the blood type of parents. The possible blood type that can \n"
" appear in the progeny will be displayed in the table below ", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.label_3.setText(_translate("MainWindow", "    Parent 1", None))
        self.comboBox_parent1.setItemText(0, _translate("MainWindow", "Select a blood type", None))
        self.comboBox_parent1.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_parent1.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_parent1.setItemText(3, _translate("MainWindow", "AB", None))
        self.comboBox_parent1.setItemText(4, _translate("MainWindow", "O", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.label_4.setText(_translate("MainWindow", "   Parent 2", None))
        self.comboBox_parent2.setItemText(0, _translate("MainWindow", "Select a blood type", None))
        self.comboBox_parent2.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_parent2.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_parent2.setItemText(3, _translate("MainWindow", "AB", None))
        self.comboBox_parent2.setItemText(4, _translate("MainWindow", "O", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "O", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Inheritance of blood types", None))
        self.label_7.setText(_translate("MainWindow", "   Created by Masooma Qaiser and Fakhriya Fayyaz at", None))
        self.label_11.setText(_translate("MainWindow", "CECOS University of IT & Emerging Sciences\n"
"Peshawar, Pakistan.", None))
        self.label_8.setText(_translate("MainWindow", "masooma.qaiser1@gmail.com ", None))
        self.label_9.setText(_translate("MainWindow", "fakhriya.khan@gmail.com ", None))
        self.label_15.setText(_translate("MainWindow", "This work is being distributed under a \n"
"Creative Commons Attribution 4.0 International License.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

