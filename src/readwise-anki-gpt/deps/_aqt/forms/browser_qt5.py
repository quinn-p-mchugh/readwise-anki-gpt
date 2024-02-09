# Form implementation generated from reading ui file 'qt/aqt/forms/browser.ui'
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
        Dialog.resize(750, 493)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:anki.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 6, 6, 12)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 6)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchEdit = QtWidgets.QComboBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setEditable(True)
        self.searchEdit.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tableView = QtWidgets.QTableView(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 150))
        self.tableView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(20)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.fieldsArea = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setMinimumSize(QtCore.QSize(50, 200))
        self.fieldsArea.setObjectName("fieldsArea")
        self.horizontalLayout2.addWidget(self.fieldsArea)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.verticalLayout_3.addWidget(self.splitter)
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuJump = QtWidgets.QMenu(parent=self.menubar)
        self.menuJump.setObjectName("menuJump")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Cards = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Cards.setObjectName("menu_Cards")
        self.menuFlag = QtWidgets.QMenu(parent=self.menu_Cards)
        self.menuFlag.setObjectName("menuFlag")
        self.menu_Notes = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Notes.setObjectName("menu_Notes")
        self.menuqt_accel_view = QtWidgets.QMenu(parent=self.menubar)
        self.menuqt_accel_view.setObjectName("menuqt_accel_view")
        self.menuLayout = QtWidgets.QMenu(parent=self.menuqt_accel_view)
        self.menuLayout.setObjectName("menuLayout")
        Dialog.setMenuBar(self.menubar)
        self.actionSelectAll = QtWidgets.QAction(parent=Dialog)
        self.actionSelectAll.setShortcut("Ctrl+Alt+A")
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionUndo = QtWidgets.QAction(parent=Dialog)
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.setObjectName("actionUndo")
        self.actionInvertSelection = QtWidgets.QAction(parent=Dialog)
        self.actionInvertSelection.setShortcut("Ctrl+Alt+S")
        self.actionInvertSelection.setObjectName("actionInvertSelection")
        self.actionFind = QtWidgets.QAction(parent=Dialog)
        self.actionFind.setShortcut("Ctrl+F")
        self.actionFind.setObjectName("actionFind")
        self.actionNote = QtWidgets.QAction(parent=Dialog)
        self.actionNote.setShortcut("Ctrl+Shift+N")
        self.actionNote.setObjectName("actionNote")
        self.actionNextCard = QtWidgets.QAction(parent=Dialog)
        self.actionNextCard.setShortcut("Ctrl+N")
        self.actionNextCard.setObjectName("actionNextCard")
        self.actionPreviousCard = QtWidgets.QAction(parent=Dialog)
        self.actionPreviousCard.setShortcut("Ctrl+P")
        self.actionPreviousCard.setObjectName("actionPreviousCard")
        self.actionGuide = QtWidgets.QAction(parent=Dialog)
        self.actionGuide.setShortcut("F1")
        self.actionGuide.setObjectName("actionGuide")
        self.actionChangeModel = QtWidgets.QAction(parent=Dialog)
        self.actionChangeModel.setShortcut("Ctrl+Shift+M")
        self.actionChangeModel.setObjectName("actionChangeModel")
        self.actionSelectNotes = QtWidgets.QAction(parent=Dialog)
        self.actionSelectNotes.setObjectName("actionSelectNotes")
        self.actionFindReplace = QtWidgets.QAction(parent=Dialog)
        self.actionFindReplace.setShortcut("Ctrl+Alt+F")
        self.actionFindReplace.setObjectName("actionFindReplace")
        self.actionSidebarFilter = QtWidgets.QAction(parent=Dialog)
        self.actionSidebarFilter.setShortcut("Ctrl+Shift+F")
        self.actionSidebarFilter.setObjectName("actionSidebarFilter")
        self.actionCardList = QtWidgets.QAction(parent=Dialog)
        self.actionCardList.setShortcut("Ctrl+Shift+L")
        self.actionCardList.setObjectName("actionCardList")
        self.actionFindDuplicates = QtWidgets.QAction(parent=Dialog)
        self.actionFindDuplicates.setObjectName("actionFindDuplicates")
        self.actionReposition = QtWidgets.QAction(parent=Dialog)
        self.actionReposition.setShortcut("Ctrl+Shift+S")
        self.actionReposition.setObjectName("actionReposition")
        self.actionFirstCard = QtWidgets.QAction(parent=Dialog)
        self.actionFirstCard.setShortcut("Home")
        self.actionFirstCard.setObjectName("actionFirstCard")
        self.actionLastCard = QtWidgets.QAction(parent=Dialog)
        self.actionLastCard.setShortcut("End")
        self.actionLastCard.setObjectName("actionLastCard")
        self.actionClose = QtWidgets.QAction(parent=Dialog)
        self.actionClose.setShortcut("Ctrl+W")
        self.actionClose.setObjectName("actionClose")
        self.action_Info = QtWidgets.QAction(parent=Dialog)
        self.action_Info.setShortcut("Ctrl+Shift+I")
        self.action_Info.setObjectName("action_Info")
        self.actionAdd_Tags = QtWidgets.QAction(parent=Dialog)
        self.actionAdd_Tags.setShortcut("Ctrl+Shift+A")
        self.actionAdd_Tags.setObjectName("actionAdd_Tags")
        self.actionRemove_Tags = QtWidgets.QAction(parent=Dialog)
        self.actionRemove_Tags.setShortcut("Ctrl+Alt+Shift+A")
        self.actionRemove_Tags.setObjectName("actionRemove_Tags")
        self.actionToggle_Suspend = QtWidgets.QAction(parent=Dialog)
        self.actionToggle_Suspend.setCheckable(True)
        self.actionToggle_Suspend.setShortcut("Ctrl+J")
        self.actionToggle_Suspend.setObjectName("actionToggle_Suspend")
        self.actionDelete = QtWidgets.QAction(parent=Dialog)
        self.actionDelete.setShortcut("Ctrl+Del")
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd = QtWidgets.QAction(parent=Dialog)
        self.actionAdd.setShortcut("Ctrl+E")
        self.actionAdd.setObjectName("actionAdd")
        self.actionChange_Deck = QtWidgets.QAction(parent=Dialog)
        self.actionChange_Deck.setShortcut("Ctrl+D")
        self.actionChange_Deck.setObjectName("actionChange_Deck")
        self.actionRed_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionRed_Flag.setCheckable(True)
        self.actionRed_Flag.setShortcut("Ctrl+1")
        self.actionRed_Flag.setObjectName("actionRed_Flag")
        self.actionOrange_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionOrange_Flag.setCheckable(True)
        self.actionOrange_Flag.setShortcut("Ctrl+2")
        self.actionOrange_Flag.setObjectName("actionOrange_Flag")
        self.actionGreen_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionGreen_Flag.setCheckable(True)
        self.actionGreen_Flag.setShortcut("Ctrl+3")
        self.actionGreen_Flag.setObjectName("actionGreen_Flag")
        self.actionBlue_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionBlue_Flag.setCheckable(True)
        self.actionBlue_Flag.setShortcut("Ctrl+4")
        self.actionBlue_Flag.setObjectName("actionBlue_Flag")
        self.actionSidebar = QtWidgets.QAction(parent=Dialog)
        self.actionSidebar.setShortcut("Ctrl+Shift+R")
        self.actionSidebar.setObjectName("actionSidebar")
        self.actionClear_Unused_Tags = QtWidgets.QAction(parent=Dialog)
        self.actionClear_Unused_Tags.setObjectName("actionClear_Unused_Tags")
        self.actionManage_Note_Types = QtWidgets.QAction(parent=Dialog)
        self.actionManage_Note_Types.setObjectName("actionManage_Note_Types")
        self.actionToggle_Mark = QtWidgets.QAction(parent=Dialog)
        self.actionToggle_Mark.setCheckable(True)
        self.actionToggle_Mark.setShortcut("Ctrl+K")
        self.actionToggle_Mark.setObjectName("actionToggle_Mark")
        self.actionExport = QtWidgets.QAction(parent=Dialog)
        self.actionExport.setShortcut("Ctrl+Shift+E")
        self.actionExport.setObjectName("actionExport")
        self.actionCreateFilteredDeck = QtWidgets.QAction(parent=Dialog)
        self.actionCreateFilteredDeck.setShortcut("Ctrl+G")
        self.actionCreateFilteredDeck.setObjectName("actionCreateFilteredDeck")
        self.action_set_due_date = QtWidgets.QAction(parent=Dialog)
        self.action_set_due_date.setShortcut("Ctrl+Shift+D")
        self.action_set_due_date.setObjectName("action_set_due_date")
        self.action_forget = QtWidgets.QAction(parent=Dialog)
        self.action_forget.setShortcut("Ctrl+Alt+N")
        self.action_forget.setObjectName("action_forget")
        self.action_toggle_mode = QtWidgets.QAction(parent=Dialog)
        self.action_toggle_mode.setShortcut("Ctrl+Alt+T")
        self.action_toggle_mode.setObjectName("action_toggle_mode")
        self.actionRedo = QtWidgets.QAction(parent=Dialog)
        self.actionRedo.setShortcut("Ctrl+Shift+Z")
        self.actionRedo.setObjectName("actionRedo")
        self.actionPink_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionPink_Flag.setCheckable(True)
        self.actionPink_Flag.setShortcut("Ctrl+5")
        self.actionPink_Flag.setObjectName("actionPink_Flag")
        self.actionTurquoise_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionTurquoise_Flag.setCheckable(True)
        self.actionTurquoise_Flag.setShortcut("Ctrl+6")
        self.actionTurquoise_Flag.setObjectName("actionTurquoise_Flag")
        self.actionPurple_Flag = QtWidgets.QAction(parent=Dialog)
        self.actionPurple_Flag.setCheckable(True)
        self.actionPurple_Flag.setShortcut("Ctrl+7")
        self.actionPurple_Flag.setObjectName("actionPurple_Flag")
        self.actionCopy = QtWidgets.QAction(parent=Dialog)
        self.actionCopy.setShortcut("Ctrl+Alt+E")
        self.actionCopy.setObjectName("actionCopy")
        self.actionFullScreen = QtWidgets.QAction(parent=Dialog)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.actionZoomIn = QtWidgets.QAction(parent=Dialog)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(parent=Dialog)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionResetZoom = QtWidgets.QAction(parent=Dialog)
        self.actionResetZoom.setShortcut("Ctrl+0")
        self.actionResetZoom.setObjectName("actionResetZoom")
        self.actionLayoutAuto = QtWidgets.QAction(parent=Dialog)
        self.actionLayoutAuto.setCheckable(True)
        self.actionLayoutAuto.setObjectName("actionLayoutAuto")
        self.actionLayoutVertical = QtWidgets.QAction(parent=Dialog)
        self.actionLayoutVertical.setCheckable(True)
        self.actionLayoutVertical.setObjectName("actionLayoutVertical")
        self.actionLayoutHorizontal = QtWidgets.QAction(parent=Dialog)
        self.actionLayoutHorizontal.setCheckable(True)
        self.actionLayoutHorizontal.setObjectName("actionLayoutHorizontal")
        self.actionbrowsing_toggle_showing_cards_notes = QtWidgets.QAction(parent=Dialog)
        self.actionbrowsing_toggle_showing_cards_notes.setObjectName("actionbrowsing_toggle_showing_cards_notes")
        self.action_toggle_bury = QtWidgets.QAction(parent=Dialog)
        self.action_toggle_bury.setCheckable(True)
        self.action_toggle_bury.setShortcut("Ctrl+Shift+J")
        self.action_toggle_bury.setObjectName("action_toggle_bury")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionSelectNotes)
        self.menuEdit.addAction(self.actionInvertSelection)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClose)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCreateFilteredDeck)
        self.menuJump.addAction(self.actionFind)
        self.menuJump.addAction(self.actionSidebarFilter)
        self.menuJump.addAction(self.actionSidebar)
        self.menuJump.addAction(self.actionNote)
        self.menuJump.addAction(self.actionCardList)
        self.menuJump.addSeparator()
        self.menuJump.addAction(self.actionFirstCard)
        self.menuJump.addAction(self.actionPreviousCard)
        self.menuJump.addAction(self.actionNextCard)
        self.menuJump.addAction(self.actionLastCard)
        self.menu_Help.addAction(self.actionGuide)
        self.menuFlag.addAction(self.actionRed_Flag)
        self.menuFlag.addAction(self.actionOrange_Flag)
        self.menuFlag.addAction(self.actionGreen_Flag)
        self.menuFlag.addAction(self.actionBlue_Flag)
        self.menuFlag.addAction(self.actionPink_Flag)
        self.menuFlag.addAction(self.actionTurquoise_Flag)
        self.menuFlag.addAction(self.actionPurple_Flag)
        self.menu_Cards.addAction(self.actionChange_Deck)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.action_set_due_date)
        self.menu_Cards.addAction(self.action_forget)
        self.menu_Cards.addAction(self.actionReposition)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.actionToggle_Suspend)
        self.menu_Cards.addAction(self.action_toggle_bury)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.menuFlag.menuAction())
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.action_Info)
        self.menu_Notes.addAction(self.actionAdd)
        self.menu_Notes.addAction(self.actionCopy)
        self.menu_Notes.addAction(self.actionExport)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionAdd_Tags)
        self.menu_Notes.addAction(self.actionRemove_Tags)
        self.menu_Notes.addAction(self.actionClear_Unused_Tags)
        self.menu_Notes.addAction(self.actionToggle_Mark)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionChangeModel)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionFindDuplicates)
        self.menu_Notes.addAction(self.actionFindReplace)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionManage_Note_Types)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionDelete)
        self.menuLayout.addAction(self.actionLayoutAuto)
        self.menuLayout.addSeparator()
        self.menuLayout.addAction(self.actionLayoutVertical)
        self.menuLayout.addAction(self.actionLayoutHorizontal)
        self.menuqt_accel_view.addAction(self.action_toggle_mode)
        self.menuqt_accel_view.addSeparator()
        self.menuqt_accel_view.addAction(self.actionFullScreen)
        self.menuqt_accel_view.addSeparator()
        self.menuqt_accel_view.addAction(self.actionZoomIn)
        self.menuqt_accel_view.addAction(self.actionZoomOut)
        self.menuqt_accel_view.addAction(self.actionResetZoom)
        self.menuqt_accel_view.addSeparator()
        self.menuqt_accel_view.addAction(self.menuLayout.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuqt_accel_view.menuAction())
        self.menubar.addAction(self.menu_Notes.menuAction())
        self.menubar.addAction(self.menu_Cards.menuAction())
        self.menubar.addAction(self.menuJump.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(Dialog)
        self.actionSelectAll.triggered.connect(self.tableView.selectAll) # type: ignore  # type: ignore
        self.actionClose.triggered.connect(Dialog.close) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.menuEdit.setTitle(tr.qt_accel_edit())
        self.menuJump.setTitle(tr.qt_accel_go())
        self.menu_Help.setTitle(tr.qt_accel_help())
        self.menu_Cards.setTitle(tr.qt_accel_cards())
        self.menuFlag.setTitle(tr.browsing_flag())
        self.menu_Notes.setTitle(tr.qt_accel_notes())
        self.menuqt_accel_view.setTitle(tr.qt_accel_view())
        self.menuLayout.setTitle(tr.qt_accel_layout())
        self.actionSelectAll.setText(tr.qt_accel_select_all())
        self.actionUndo.setText(tr.qt_accel_undo())
        self.actionInvertSelection.setText(tr.qt_accel_invert_selection())
        self.actionFind.setText(tr.qt_accel_find())
        self.actionNote.setText(tr.qt_accel_note())
        self.actionNextCard.setText(tr.qt_accel_next_card())
        self.actionPreviousCard.setText(tr.qt_accel_previous_card())
        self.actionGuide.setText(tr.qt_accel_guide())
        self.actionChangeModel.setText(tr.browsing_change_note_type2())
        self.actionSelectNotes.setText(tr.qt_accel_select_notes())
        self.actionFindReplace.setText(tr.qt_accel_find_and_replace())
        self.actionSidebarFilter.setText(tr.qt_accel_filter())
        self.actionCardList.setText(tr.browsing_card_list())
        self.actionFindDuplicates.setText(tr.qt_accel_find_duplicates())
        self.actionReposition.setText(tr.browsing_reposition())
        self.actionFirstCard.setText(tr.browsing_first_card())
        self.actionLastCard.setText(tr.browsing_last_card())
        self.actionClose.setText(tr.actions_close())
        self.action_Info.setText(tr.qt_accel_info())
        self.actionAdd_Tags.setText(tr.browsing_add_tags2())
        self.actionRemove_Tags.setText(tr.browsing_remove_tags())
        self.actionToggle_Suspend.setText(tr.browsing_toggle_suspend())
        self.actionDelete.setText(tr.actions_delete())
        self.actionAdd.setText(tr.browsing_add_notes())
        self.actionChange_Deck.setText(tr.browsing_change_deck2())
        self.actionRed_Flag.setText(tr.actions_flag_red())
        self.actionOrange_Flag.setText(tr.actions_flag_orange())
        self.actionGreen_Flag.setText(tr.actions_flag_green())
        self.actionBlue_Flag.setText(tr.actions_flag_blue())
        self.actionSidebar.setText(tr.browsing_sidebar())
        self.actionClear_Unused_Tags.setText(tr.browsing_clear_unused_tags())
        self.actionManage_Note_Types.setText(tr.browsing_manage_note_types())
        self.actionToggle_Mark.setText(tr.browsing_toggle_mark())
        self.actionExport.setText(tr.qt_accel_export_notes())
        self.actionCreateFilteredDeck.setText(tr.qt_misc_create_filtered_deck())
        self.action_set_due_date.setText(tr.qt_accel_set_due_date())
        self.action_forget.setText(tr.qt_accel_forget())
        self.action_toggle_mode.setText(tr.browsing_toggle_showing_cards_notes())
        self.actionRedo.setText(tr.qt_accel_redo())
        self.actionPink_Flag.setText(tr.actions_flag_pink())
        self.actionTurquoise_Flag.setText(tr.actions_flag_turquoise())
        self.actionPurple_Flag.setText(tr.actions_flag_purple())
        self.actionCopy.setText(tr.actions_create_copy())
        self.actionFullScreen.setText(tr.qt_accel_full_screen())
        self.actionZoomIn.setText(tr.qt_accel_zoom_editor_in())
        self.actionZoomOut.setText(tr.qt_accel_zoom_editor_out())
        self.actionResetZoom.setText(tr.qt_accel_reset_zoom())
        self.actionLayoutAuto.setText(tr.qt_accel_layout_auto())
        self.actionLayoutVertical.setText(tr.qt_accel_layout_vertical())
        self.actionLayoutHorizontal.setText(tr.qt_accel_layout_horizontal())
        self.actionbrowsing_toggle_showing_cards_notes.setText(tr.browsing_toggle_showing_cards_notes())
        self.action_toggle_bury.setText(tr.browsing_toggle_bury())