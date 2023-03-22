# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blood_results.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Blood(object):

    def setupUi(self, BloodT):
        BloodT.setObjectName("Blood Test Results")
        BloodT.resize(438, 545)
        self.save_results = QtWidgets.QPushButton( BloodT)
        self.save_results.setGeometry(QtCore.QRect(170, 490, 75, 31))
        self.save_results.setObjectName("save_results")
        self.layoutWidget = QtWidgets.QWidget( BloodT)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 406, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cholestrol = QtWidgets.QLineEdit(self.layoutWidget)
        self.cholestrol.setObjectName("cholestrol")
        self.horizontalLayout.addWidget(self.cholestrol)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.glucose = QtWidgets.QLineEdit(self.layoutWidget)
        self.glucose.setObjectName("glucose")
        self.horizontalLayout_2.addWidget(self.glucose)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.hdl = QtWidgets.QLineEdit(self.layoutWidget)
        self.hdl.setObjectName("hdl")
        self.horizontalLayout_4.addWidget(self.hdl)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.bmi = QtWidgets.QLineEdit(self.layoutWidget)
        self.bmi.setObjectName("bmi")
        self.horizontalLayout_6.addWidget(self.bmi)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.sbp = QtWidgets.QLineEdit(self.layoutWidget)
        self.sbp.setObjectName("sbp")
        self.horizontalLayout_3.addWidget(self.sbp)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.dbp = QtWidgets.QLineEdit(self.layoutWidget)
        self.dbp.setObjectName("dbp")
        self.horizontalLayout_5.addWidget(self.dbp)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame( BloodT)
        self.line.setGeometry(QtCore.QRect(20, 430, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_14 = QtWidgets.QLabel( BloodT)
        self.label_14.setGeometry(QtCore.QRect(40, 400, 371, 20))
        self.label_14.setObjectName("label_14")
        self.widget = QtWidgets.QWidget( BloodT)
        self.widget.setGeometry(QtCore.QRect(20, 450, 381, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.diabet = QtWidgets.QLineEdit(self.widget)
        self.diabet.setObjectName("diabet")
        self.horizontalLayout_7.addWidget(self.diabet)

        self.retranslateUi( BloodT)
        QtCore.QMetaObject.connectSlotsByName( BloodT)

    def retranslateUi(self,  BloodT):
        _translate = QtCore.QCoreApplication.translate
        BloodT.setWindowTitle(_translate(" BloodT", " BloodT"))
        self.save_results.setText(_translate(" BloodT", "Save results"))
        self.label.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cholestrol</span></p></body></html>"))
        self.label_2.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">mg/dl</span></p></body></html>"))
        self.label_3.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Glucose</span></p></body></html>"))
        self.label_4.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">mg/dl</span></p></body></html>"))
        self.label_7.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HDL-chol</span></p></body></html>"))
        self.label_8.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">mg/dl</span></p></body></html>"))
        self.label_11.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Body to Mass Indicator</span></p></body></html>"))
        self.label_12.setText(_translate(" BloodT", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Systolic BP</span></p></body></html>"))
        self.label_6.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">mmHg</span></p></body></html>"))
        self.label_9.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Diastolic BP</span></p></body></html>"))
        self.label_10.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">mmHg</span></p></body></html>"))
        self.label_14.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">Enter the Preliminary Diagonistics depending on the values </span></p></body></html>"))
        self.label_13.setText(_translate(" BloodT", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Preliminary Diagnostics</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BloodT = QtWidgets.QDialog()
    ui = Ui_Blood()
    ui.setupUi( BloodT)
    BloodT.show()
    sys.exit(app.exec_())
