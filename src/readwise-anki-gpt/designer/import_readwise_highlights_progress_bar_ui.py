# Form implementation generated from reading ui file 'import_readwise_highlights_progress_bar.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReadwiseImportHighlightsProgressBar(object):
    def setupUi(self, ReadwiseImportHighlightsProgressBar):
        ReadwiseImportHighlightsProgressBar.setObjectName("ReadwiseImportHighlightsProgressBar")
        ReadwiseImportHighlightsProgressBar.resize(400, 111)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReadwiseImportHighlightsProgressBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=ReadwiseImportHighlightsProgressBar)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(parent=ReadwiseImportHighlightsProgressBar)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ReadwiseImportHighlightsProgressBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Abort)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(ReadwiseImportHighlightsProgressBar)
        self.buttonBox.accepted.connect(ReadwiseImportHighlightsProgressBar.accept) # type: ignore
        self.buttonBox.rejected.connect(ReadwiseImportHighlightsProgressBar.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ReadwiseImportHighlightsProgressBar)

    def retranslateUi(self, ReadwiseImportHighlightsProgressBar):
        _translate = QtCore.QCoreApplication.translate
        ReadwiseImportHighlightsProgressBar.setWindowTitle(_translate("ReadwiseImportHighlightsProgressBar", "Dialog"))
        self.label.setText(_translate("ReadwiseImportHighlightsProgressBar", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Importing highlights from Readwise…</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReadwiseImportHighlightsProgressBar = QtWidgets.QDialog()
    ui = Ui_ReadwiseImportHighlightsProgressBar()
    ui.setupUi(ReadwiseImportHighlightsProgressBar)
    ReadwiseImportHighlightsProgressBar.show()
    sys.exit(app.exec())
