# Form implementation generated from reading ui file 'qt/aqt/forms/changemap.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_ChangeMap(object):
    def setupUi(self, ChangeMap):
        ChangeMap.setObjectName("ChangeMap")
        ChangeMap.resize(391, 360)
        self.vboxlayout = QtWidgets.QVBoxLayout(ChangeMap)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(parent=ChangeMap)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.fields = QtWidgets.QListWidget(parent=ChangeMap)
        self.fields.setObjectName("fields")
        self.vboxlayout.addWidget(self.fields)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ChangeMap)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChangeMap)
        self.buttonBox.accepted.connect(ChangeMap.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(ChangeMap.reject) # type: ignore  # type: ignore
        self.fields.doubleClicked['QModelIndex'].connect(ChangeMap.accept) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ChangeMap)

    def retranslateUi(self, ChangeMap):
        _translate = QtCore.QCoreApplication.translate
        ChangeMap.setWindowTitle(tr.actions_import())
        self.label.setText(tr.browsing_target_field())