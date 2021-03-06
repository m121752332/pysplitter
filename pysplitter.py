# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pysplitter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pysplitter(object):
    def setupUi(self, pysplitter):
        pysplitter.setObjectName("pysplitter")
        pysplitter.resize(1025, 614)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/icon/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pysplitter.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(pysplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.tab1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pipediter = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        self.pipediter.setFont(font)
        self.pipediter.setToolTip("")
        self.pipediter.setToolTipDuration(-1)
        self.pipediter.setStatusTip("")
        self.pipediter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pipediter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pipediter.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.pipediter.setAcceptRichText(False)
        self.pipediter.setPlaceholderText("")
        self.pipediter.setObjectName("pipediter")
        self.gridLayout_5.addWidget(self.pipediter, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setMaximumSize(QtCore.QSize(30, 16777215))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(1, 1, 1, 1)
        self.formLayout_2.setSpacing(1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.convert = QtWidgets.QPushButton(self.widget)
        self.convert.setMaximumSize(QtCore.QSize(20, 16777215))
        self.convert.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.convert.setIcon(icon1)
        self.convert.setObjectName("convert")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.convert)
        self.gridLayout_5.addWidget(self.widget, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sqlediter = QtWidgets.QTextEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        self.sqlediter.setFont(font)
        self.sqlediter.setToolTip("")
        self.sqlediter.setToolTipDuration(-1)
        self.sqlediter.setStatusTip("")
        self.sqlediter.setWhatsThis("")
        self.sqlediter.setReadOnly(True)
        self.sqlediter.setObjectName("sqlediter")
        self.horizontalLayout.addWidget(self.sqlediter)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/icon/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab1, icon2, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/icon/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab2, icon3, "")
        self.datatable = QtWidgets.QTableWidget(self.splitter_2)
        self.datatable.setMinimumSize(QtCore.QSize(180, 0))
        self.datatable.setMaximumSize(QtCore.QSize(180, 16777215))
        self.datatable.setMouseTracking(True)
        self.datatable.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.datatable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.datatable.setDragDropOverwriteMode(False)
        self.datatable.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.datatable.setAlternatingRowColors(True)
        self.datatable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.datatable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.datatable.setGridStyle(QtCore.Qt.SolidLine)
        self.datatable.setRowCount(20)
        self.datatable.setColumnCount(1)
        self.datatable.setObjectName("datatable")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(170, 255, 255))
        self.datatable.setHorizontalHeaderItem(0, item)
        self.datatable.horizontalHeader().setVisible(True)
        self.datatable.horizontalHeader().setCascadingSectionResizes(True)
        self.datatable.horizontalHeader().setDefaultSectionSize(130)
        self.datatable.verticalHeader().setVisible(True)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.excel = QtWidgets.QPushButton(self.groupBox)
        self.excel.setGeometry(QtCore.QRect(10, 10, 80, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excel.sizePolicy().hasHeightForWidth())
        self.excel.setSizePolicy(sizePolicy)
        self.excel.setMinimumSize(QtCore.QSize(80, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pic/icon/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.excel.setIcon(icon4)
        self.excel.setObjectName("excel")
        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)
        pysplitter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pysplitter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 21))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        pysplitter.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(pysplitter)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        pysplitter.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(pysplitter)
        self.statusbar.setObjectName("statusbar")
        pysplitter.setStatusBar(self.statusbar)
        self.lang = QtWidgets.QAction(pysplitter)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pic/icon/lingua.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lang.setIcon(icon5)
        self.lang.setObjectName("lang")
        self.editcopy = QtWidgets.QAction(pysplitter)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pic/icon/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/pic/icon/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editcopy.setIcon(icon6)
        self.editcopy.setObjectName("editcopy")
        self.editcut = QtWidgets.QAction(pysplitter)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/pic/icon/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editcut.setIcon(icon7)
        self.editcut.setObjectName("editcut")
        self.editpaste = QtWidgets.QAction(pysplitter)
        self.editpaste.setIcon(icon4)
        self.editpaste.setObjectName("editpaste")
        self.insert = QtWidgets.QAction(pysplitter)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/pic/icon/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.insert.setIcon(icon8)
        self.insert.setObjectName("insert")
        self.about = QtWidgets.QAction(pysplitter)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pic/icon/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(":/pic/icon/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.about.setIcon(icon9)
        self.about.setObjectName("about")
        self.controlz = QtWidgets.QAction(pysplitter)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pic/icon/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlz.setIcon(icon10)
        self.controlz.setObjectName("controlz")
        self.modify = QtWidgets.QAction(pysplitter)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pic/icon/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.modify.setIcon(icon11)
        self.modify.setObjectName("modify")
        self.delete_2 = QtWidgets.QAction(pysplitter)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/pic/icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.delete_2.setIcon(icon12)
        self.delete_2.setObjectName("delete_2")
        self.reproduce = QtWidgets.QAction(pysplitter)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/pic/icon/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reproduce.setIcon(icon13)
        self.reproduce.setObjectName("reproduce")
        self.invalid = QtWidgets.QAction(pysplitter)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/pic/icon/garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.invalid.setIcon(icon14)
        self.invalid.setObjectName("invalid")
        self.detail = QtWidgets.QAction(pysplitter)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/pic/icon/prop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.detail.setIcon(icon15)
        self.detail.setObjectName("detail")
        self.printer = QtWidgets.QAction(pysplitter)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/pic/icon/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.printer.setIcon(icon16)
        self.printer.setObjectName("printer")
        self.exporttoexcel = QtWidgets.QAction(pysplitter)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/pic/icon/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exporttoexcel.setIcon(icon17)
        self.exporttoexcel.setObjectName("exporttoexcel")
        self.query = QtWidgets.QAction(pysplitter)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/pic/icon/filefind.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.query.setIcon(icon18)
        self.query.setObjectName("query")
        self.qbe_select = QtWidgets.QAction(pysplitter)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/pic/icon/file_q.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap(":/pic/icon/filefind.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.qbe_select.setIcon(icon19)
        self.qbe_select.setObjectName("qbe_select")
        self.qbe_save = QtWidgets.QAction(pysplitter)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/pic/icon/file_w.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.qbe_save.setIcon(icon20)
        self.qbe_save.setObjectName("qbe_save")
        self.first = QtWidgets.QAction(pysplitter)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/pic/icon/gobegin.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.first.setIcon(icon21)
        self.first.setObjectName("first")
        self.previous = QtWidgets.QAction(pysplitter)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/pic/icon/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.previous.setIcon(icon22)
        self.previous.setObjectName("previous")
        self.jump = QtWidgets.QAction(pysplitter)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/pic/icon/balloon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.jump.setIcon(icon23)
        self.jump.setObjectName("jump")
        self.next = QtWidgets.QAction(pysplitter)
        self.next.setIcon(icon1)
        self.next.setObjectName("next")
        self.last = QtWidgets.QAction(pysplitter)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/pic/icon/goend.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.last.setIcon(icon24)
        self.last.setObjectName("last")
        self.key = QtWidgets.QAction(pysplitter)
        self.key.setIcon(icon10)
        self.key.setObjectName("key")
        self.help = QtWidgets.QAction(pysplitter)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/pic/icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.help.setIcon(icon25)
        self.help.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.help.setObjectName("help")
        self.exit = QtWidgets.QAction(pysplitter)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/pic/icon/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exit.setIcon(icon26)
        self.exit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.exit.setObjectName("exit")
        self.menu_1.addAction(self.help)
        self.menu_1.addAction(self.about)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.controlz)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.exit)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.toolBar.addAction(self.lang)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editcopy)
        self.toolBar.addAction(self.editcut)
        self.toolBar.addAction(self.editpaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.insert)
        self.toolBar.addAction(self.modify)
        self.toolBar.addAction(self.delete_2)
        self.toolBar.addAction(self.reproduce)
        self.toolBar.addAction(self.invalid)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.detail)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.printer)
        self.toolBar.addAction(self.exporttoexcel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.query)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.first)
        self.toolBar.addAction(self.previous)
        self.toolBar.addAction(self.jump)
        self.toolBar.addAction(self.next)
        self.toolBar.addAction(self.last)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.help)
        self.toolBar.addAction(self.exit)

        self.retranslateUi(pysplitter)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pysplitter)
        pysplitter.setTabOrder(self.tabWidget, self.pipediter)
        pysplitter.setTabOrder(self.pipediter, self.sqlediter)
        pysplitter.setTabOrder(self.sqlediter, self.datatable)
        pysplitter.setTabOrder(self.datatable, self.comboBox)

    def retranslateUi(self, pysplitter):
        _translate = QtCore.QCoreApplication.translate
        pysplitter.setWindowTitle(_translate("pysplitter", "資料分隔處理器"))
        self.groupBox_2.setTitle(_translate("pysplitter", "pip分隔語法"))
        self.groupBox_3.setTitle(_translate("pysplitter", "資料庫開發語法"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("pysplitter", "輸出頁面"))
        self.groupBox_4.setTitle(_translate("pysplitter", "條件設定"))
        self.label.setText(_translate("pysplitter", "區隔方式"))
        self.comboBox.setItemText(0, _translate("pysplitter", "使用 | 區隔"))
        self.comboBox.setItemText(1, _translate("pysplitter", "使用 , 區隔"))
        self.comboBox.setItemText(2, _translate("pysplitter", "使用 ; 區隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("pysplitter", "設置頁面"))
        self.datatable.setSortingEnabled(True)
        item = self.datatable.horizontalHeaderItem(0)
        item.setText(_translate("pysplitter", "資料欄位"))
        self.excel.setText(_translate("pysplitter", "資料貼上"))
        self.menu_1.setTitle(_translate("pysplitter", "畫面"))
        self.menu_2.setTitle(_translate("pysplitter", "編輯"))
        self.menu_3.setTitle(_translate("pysplitter", "資料"))
        self.menu_4.setTitle(_translate("pysplitter", "瀏覽"))
        self.toolBar.setWindowTitle(_translate("pysplitter", "toolBar"))
        self.lang.setText(_translate("pysplitter", "語言"))
        self.lang.setShortcut(_translate("pysplitter", "Ctrl+L"))
        self.editcopy.setText(_translate("pysplitter", "資料複製"))
        self.editcopy.setToolTip(_translate("pysplitter", "資料複製"))
        self.editcut.setText(_translate("pysplitter", "資料剪下"))
        self.editcut.setToolTip(_translate("pysplitter", "資料剪下"))
        self.editpaste.setText(_translate("pysplitter", "資料貼上"))
        self.editpaste.setToolTip(_translate("pysplitter", "資料貼上"))
        self.insert.setText(_translate("pysplitter", "新增"))
        self.insert.setToolTip(_translate("pysplitter", "[F1]建立資料"))
        self.insert.setShortcut(_translate("pysplitter", "F1"))
        self.about.setText(_translate("pysplitter", "程式資訊"))
        self.about.setToolTip(_translate("pysplitter", "程式資訊"))
        self.controlz.setText(_translate("pysplitter", "必要欄位"))
        self.controlz.setToolTip(_translate("pysplitter", "必要欄位"))
        self.controlz.setShortcut(_translate("pysplitter", "Ctrl+R"))
        self.modify.setText(_translate("pysplitter", "更改"))
        self.modify.setToolTip(_translate("pysplitter", "[u]修改資料"))
        self.modify.setShortcut(_translate("pysplitter", "U"))
        self.delete_2.setText(_translate("pysplitter", "刪除"))
        self.delete_2.setToolTip(_translate("pysplitter", "[F2]刪除資料"))
        self.delete_2.setShortcut(_translate("pysplitter", "F2"))
        self.reproduce.setText(_translate("pysplitter", "複製"))
        self.reproduce.setToolTip(_translate("pysplitter", "[c]複製目前資料"))
        self.reproduce.setShortcut(_translate("pysplitter", "C"))
        self.invalid.setText(_translate("pysplitter", "無效"))
        self.invalid.setToolTip(_translate("pysplitter", "[x]使資料無效"))
        self.invalid.setShortcut(_translate("pysplitter", "X"))
        self.detail.setText(_translate("pysplitter", "單身"))
        self.detail.setToolTip(_translate("pysplitter", "[b]編輯單身資料"))
        self.detail.setShortcut(_translate("pysplitter", "B"))
        self.printer.setText(_translate("pysplitter", "列印"))
        self.printer.setToolTip(_translate("pysplitter", "[o]列印報表"))
        self.printer.setShortcut(_translate("pysplitter", "P"))
        self.exporttoexcel.setText(_translate("pysplitter", "匯出Excel"))
        self.exporttoexcel.setToolTip(_translate("pysplitter", "[e]單身匯出Excel"))
        self.exporttoexcel.setShortcut(_translate("pysplitter", "E"))
        self.query.setText(_translate("pysplitter", "查詢"))
        self.query.setToolTip(_translate("pysplitter", "[q]尋找資料"))
        self.query.setShortcut(_translate("pysplitter", "Q"))
        self.qbe_select.setText(_translate("pysplitter", "條件查詢"))
        self.qbe_select.setToolTip(_translate("pysplitter", "[Ctrl+Q]查詢條件列表"))
        self.qbe_select.setShortcut(_translate("pysplitter", "Ctrl+Q"))
        self.qbe_save.setText(_translate("pysplitter", "條件儲存"))
        self.qbe_save.setToolTip(_translate("pysplitter", "[Ctrl+W]查詢條件儲存"))
        self.qbe_save.setShortcut(_translate("pysplitter", "Ctrl+W"))
        self.first.setText(_translate("pysplitter", "第一筆"))
        self.first.setToolTip(_translate("pysplitter", "[f]移到第一筆資料"))
        self.first.setShortcut(_translate("pysplitter", "F"))
        self.previous.setText(_translate("pysplitter", "上筆"))
        self.previous.setToolTip(_translate("pysplitter", "[p]移到上一筆資料"))
        self.previous.setShortcut(_translate("pysplitter", "P"))
        self.jump.setText(_translate("pysplitter", "指定筆"))
        self.jump.setToolTip(_translate("pysplitter", "[j]移到指定筆數資料"))
        self.jump.setShortcut(_translate("pysplitter", "J"))
        self.next.setText(_translate("pysplitter", "下筆"))
        self.next.setToolTip(_translate("pysplitter", "[n]移到下一筆資料"))
        self.next.setShortcut(_translate("pysplitter", "N"))
        self.last.setText(_translate("pysplitter", "末一筆"))
        self.last.setToolTip(_translate("pysplitter", "[l]移到最後一筆資料"))
        self.last.setShortcut(_translate("pysplitter", "L"))
        self.key.setText(_translate("pysplitter", "必要欄位"))
        self.key.setToolTip(_translate("pysplitter", "[Ctrl+R]必須輸入的欄位清單"))
        self.key.setShortcut(_translate("pysplitter", "Ctrl+R"))
        self.help.setText(_translate("pysplitter", "說明"))
        self.help.setToolTip(_translate("pysplitter", "[Ctrl+H]內容說明"))
        self.help.setShortcut(_translate("pysplitter", "Ctrl+H"))
        self.exit.setText(_translate("pysplitter", "離開"))
        self.exit.setToolTip(_translate("pysplitter", "[Esc]離開程式"))
import pysplitter_rc
