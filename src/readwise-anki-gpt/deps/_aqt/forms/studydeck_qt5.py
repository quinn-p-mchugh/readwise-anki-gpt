# Form implementation generated from reading ui file 'qt/aqt/forms/studydeck.ui'
#
# Created by: PyQt5 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filter = QtWidgets.QLineEdit(parent=Dialog)
        self.filter.setObjectName("filter")
        self.horizontalLayout.addWidget(self.filter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.list = QtWidgets.QListWidget(parent=Dialog)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.decks_study_deck())
        self.label.setText(tr.decks_filter())