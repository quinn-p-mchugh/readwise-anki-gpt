# Form implementation generated from reading ui file 'qt/aqt/forms/template.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 1081)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.template_box = QtWidgets.QGroupBox(parent=Form)
        self.template_box.setTitle("GroupBox")
        self.template_box.setObjectName("template_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.template_box)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.front_button = QtWidgets.QRadioButton(parent=self.template_box)
        self.front_button.setToolTip("")
        self.front_button.setText("FRONT")
        self.front_button.setChecked(True)
        self.front_button.setObjectName("front_button")
        self.horizontalLayout.addWidget(self.front_button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.back_button = QtWidgets.QRadioButton(parent=self.template_box)
        self.back_button.setToolTip("")
        self.back_button.setText("BACK")
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.style_button = QtWidgets.QRadioButton(parent=self.template_box)
        self.style_button.setToolTip("")
        self.style_button.setText("STYLE")
        self.style_button.setObjectName("style_button")
        self.horizontalLayout.addWidget(self.style_button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.search_edit = QtWidgets.QLineEdit(parent=self.template_box)
        self.search_edit.setObjectName("search_edit")
        self.verticalLayout.addWidget(self.search_edit)
        self.changes_affect_label = QtWidgets.QLabel(parent=self.template_box)
        self.changes_affect_label.setText("CHANGES_WILL_AFFECT")
        self.changes_affect_label.setWordWrap(True)
        self.changes_affect_label.setObjectName("changes_affect_label")
        self.verticalLayout.addWidget(self.changes_affect_label)
        self.edit_area = QtWidgets.QTextEdit(parent=self.template_box)
        self.edit_area.setObjectName("edit_area")
        self.verticalLayout.addWidget(self.edit_area)
        self.verticalLayout_2.addWidget(self.template_box)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(tr.card_templates_form())