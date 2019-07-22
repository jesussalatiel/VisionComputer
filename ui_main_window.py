from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1096, 738)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setMaximumSize(QtCore.QSize(800, 600))
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(700, 1800))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Asistente Virtual"))
        self.image_label.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", '<html><head/><body><p><img src={0}/></p></body></html>'.format('./Images/alexa.gif')))


