# Form implementation generated from reading ui file 'qt/aqt/forms/customstudy.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioAhead = QtWidgets.QRadioButton(parent=Dialog)
        self.radioAhead.setObjectName("radioAhead")
        self.gridLayout.addWidget(self.radioAhead, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioForgot = QtWidgets.QRadioButton(parent=Dialog)
        self.radioForgot.setObjectName("radioForgot")
        self.gridLayout.addWidget(self.radioForgot, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioNew = QtWidgets.QRadioButton(parent=Dialog)
        self.radioNew.setObjectName("radioNew")
        self.gridLayout.addWidget(self.radioNew, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioRev = QtWidgets.QRadioButton(parent=Dialog)
        self.radioRev.setObjectName("radioRev")
        self.gridLayout.addWidget(self.radioRev, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioCram = QtWidgets.QRadioButton(parent=Dialog)
        self.radioCram.setObjectName("radioCram")
        self.gridLayout.addWidget(self.radioCram, 5, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.radioPreview = QtWidgets.QRadioButton(parent=Dialog)
        self.radioPreview.setObjectName("radioPreview")
        self.gridLayout.addWidget(self.radioPreview, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(parent=self.groupBox)
        self.title.setText("...")
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preSpin = QtWidgets.QLabel(parent=self.groupBox)
        self.preSpin.setText("...")
        self.preSpin.setObjectName("preSpin")
        self.horizontalLayout.addWidget(self.preSpin)
        self.spin = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spin.setObjectName("spin")
        self.horizontalLayout.addWidget(self.spin)
        self.postSpin = QtWidgets.QLabel(parent=self.groupBox)
        self.postSpin.setText("...")
        self.postSpin.setObjectName("postSpin")
        self.horizontalLayout.addWidget(self.postSpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.cardType = QtWidgets.QListWidget(parent=self.groupBox)
        self.cardType.setObjectName("cardType")
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        self.verticalLayout_2.addWidget(self.cardType)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.cardType.setCurrentRow(0)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.radioNew, self.radioRev)
        Dialog.setTabOrder(self.radioRev, self.radioForgot)
        Dialog.setTabOrder(self.radioForgot, self.radioAhead)
        Dialog.setTabOrder(self.radioAhead, self.radioPreview)
        Dialog.setTabOrder(self.radioPreview, self.radioCram)
        Dialog.setTabOrder(self.radioCram, self.spin)
        Dialog.setTabOrder(self.spin, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.actions_custom_study())
        self.radioAhead.setText(tr.custom_study_review_ahead())
        self.radioForgot.setText(tr.custom_study_review_forgotten_cards())
        self.radioNew.setText(tr.custom_study_increase_todays_new_card_limit())
        self.radioRev.setText(tr.custom_study_increase_todays_review_card_limit())
        self.radioCram.setText(tr.custom_study_study_by_card_state_or_tag())
        self.radioPreview.setText(tr.custom_study_preview_new_cards())
        __sortingEnabled = self.cardType.isSortingEnabled()
        self.cardType.setSortingEnabled(False)
        item = self.cardType.item(0)
        item.setText(tr.custom_study_new_cards_only())
        item = self.cardType.item(1)
        item.setText(tr.custom_study_due_cards_only())
        item = self.cardType.item(2)
        item.setText(tr.custom_study_all_review_cards_in_random_order())
        item = self.cardType.item(3)
        item.setText(tr.custom_study_all_cards_in_random_order_dont())
        self.cardType.setSortingEnabled(__sortingEnabled)