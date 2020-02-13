# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont
from pyspiltter import Ui_pysplitter
import os
import sys
import re
import string
import gettext
import xlrd
import xlwt
# 取得資料總筆數


# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def deleteDuplicatedElement(list):
    resultList = []
    print(resultList)
    for item in list:
        if not item in resultList:
            resultList.append(item)
        print(resultList)
    return resultList

# def deleteDuplicatedElement(listA):
    # return list(set(listA))
#    return sorted(set(listA), key=listA.index)

# 主程式段


class MainWindow(QtWidgets.QMainWindow, Ui_pysplitter):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.cb = QtWidgets.QApplication.clipboard()

        # 切分狀態欄為兩條
        self.hintmsg = QtWidgets.QLabel()
        self.alertmsg = QtWidgets.QLabel()
        self.statusbar.addPermanentWidget(self.hintmsg, stretch=1)
        self.statusbar.addPermanentWidget(self.alertmsg, stretch=1)
        # 針對
        # header_item = QTableWidgetItem("員工姓名")
        # header_item.setBackground(QtCore.Qt.red) # 헤더 배경색 설정 --> app.setStyle() 설정해야만 작동한다.
        # self.s_gen.setHorizontalHeaderItem(1, header_item)

        # self.setdataheader()

        # 針對單身表格設置
        self.datatable.setEditTriggers(
            QtWidgets.QAbstractItemView.SelectedClicked)
        # self.s_gen.verticalHeader().setVisible(False)
        # self.s_gen.horizontalHeader().setVisible(False)
        # 可以设定的选择模式：
        # QTableWidget.NoSelection 不能选择
        # QTableWidget.SingleSelection 选中单个目标
        # QTableWidget.MultiSelection 选中多个目标
        # QTableWidget.ExtendedSelection shift键的连续选择
        # QTableWidget.ContiguousSelection ctrl键的不连续的多个选择
        self.datatable.setSelectionMode(QTableWidget.ContiguousSelection)

        # 程式初始化
        # self.detail_init()
        self.statusbar.showMessage('開啟完畢', 5000)
        # 設定查詢按鈕功能
        # self.query.triggered.connect(lambda: self.whichbtn(self.query, 'cl'))
        self.exporttoexcel.triggered.connect(lambda: self.writeExcel())
        # self.statusbar.showMessage('查詢完畢!',5000)
        # self.query.triggered.connect(self.refresh_data)
        # self.Title.setText("hello Python")
        # self.World.clicked.connect(self.onWorldClicked)
        # self.China.clicked.connect(self.onChinaClicked)
        # self.lineEdit.textChanged.connect(self.onlineEditTextChanged)
        # Show widget

        # 產生按鈕
        # self.generate.clicked.connect(self.barcode_gen)
        # 儲存按鈕
        # self.download.clicked.connect(self.barcode_save)

        self.excel.clicked.connect(self.set_cb)

        # 離開按鈕
        self.exit.triggered.connect(self.closeEvent)
        self.exit2.triggered.connect(self.closeEvent)

        # 用不到按鈕關閉
        self.editcopy.setEnabled(False)
        self.editcut.setEnabled(False)
        self.insert.setEnabled(False)
        self.modify.setEnabled(False)
        self.delete_2.setEnabled(False)
        self.reproduce.setEnabled(False)
        self.invalid.setEnabled(False)
        self.show()

    def whichbtn(self, btn, db='cl'):

        print("sel db="+db)

        # self.alertmsg.showMessage('查詢完畢!',5000)
        self.alertmsg.setText('查詢完畢!')
        # self.cnt.setText(len(rows))
        # self.cnt.setText(str(g_rec_b))

    # def detail_init(self):
    #    global g_rec_b = 0
        # self.cnt.setAlignment(QtCore.Qt.AlignRight)
        # self.cnt.setText(str(g_rec_b))

    # 向剪贴板中写入
    def set_cb(self):
        # mdata = self.cb.mimeData()
        # print(type(mdata))
        word = self.cb.mimeData().text()
        # print(word)
        wordlist = word.split('\n')
        wordlist = [i for i in wordlist if i != '']

        wordlist = deleteDuplicatedElement(wordlist)
        excellist = wordlist
        # print(wordlist)
        # self.sqlediter.setText(word.text())
        self.datatable.setRowCount(len(wordlist))
        g_rec_b = len(wordlist)
        for i in range(0, g_rec_b):
            print(i, str(wordlist[i]))
            if str(wordlist[i]) == '':
                pass
            else:
                cell = QTableWidgetItem(str(wordlist[i]))
                self.datatable.setItem(i, 0, cell)
        self.set_pipediter(wordlist)

    def set_pipediter(self, excellist):
        print(excellist)
        sqllist = str(excellist)

        self.sqlediter.setText(sqllist)
        classtype = self.comboBox.currentIndex()
        self.alertmsg.setText('class='+str(classtype))
        pip = ''
        if str(classtype) == '0':
            print(str(classtype))
            pip = "|".join(excellist)
        elif str(classtype) == '1':
            print(str(classtype))
            pip = ",".join(excellist)
        elif str(classtype) == '2':
            print(str(classtype))
            pip = ";".join(excellist)
        else:
            pass

        self.pipediter.setText(pip)

    # 設定單身表頭

    def setdataheader(self):
        font = QFont('微軟正黑體', 10)
        # font.setBold(True)
        self.datatable.horizontalHeader().setFont(font)  # 设置表头字体
        for i in range(10):
            self.datatable.setColumnWidth(i, 100)
        # 設定自動調整欄位大小
        self.datatable.horizontalHeader().setSectionResizeMode(
            9, QtWidgets.QHeaderView.Stretch)
        self.datatable.horizontalHeader().setStyleSheet(
            'QHeaderView::section{background:yellow}')
        # 設定標題高度
        self.datatable.horizontalHeader().setFixedHeight(40)
        # self.s_gen.setColumnHidden(0,True)

    def writeExcel(self, p_path="", filename=r'spiltter.xls'):
        """p_path : 表示檔案路徑
        """
        # 開啟excel準備寫資料
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)

        # 取得列跟欄數
        rows = self.datatable.rowCount()
        columns = self.datatable.columnCount()

        headerList = []
        for i in range(columns):
            data = self.datatable.horizontalHeaderItem(i).text()
            headerList.append(data)

        for idex, val in enumerate(headerList):
            ws.write(0, idex, val, set_style('Times New Roman', 220, True))

        for i in range(rows):
            # 因为是边读边写，所以每次写完后，要把上次存储的数据清空，存储下一行读取的数据
            mainList = []
            # tablewidget一共有10列
            for j in range(10):
                try:
                    data = self.datatable.item(
                        i, j).text()  # 得出tablewidget每行每列的数据
                    mainList.append(data)  # 添加到数组
                except:
                    # 如果tablewidget没有对象，则data = ''
                    data = ''
                    mainList.append(data)

                ws.write(i+1, j, mainList[j])
        # 保存
        wb.save(filename)
# ==================================================


# 程式入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    g_rec_b = 0
    excellist = []
    mainWindow = MainWindow()
    # mainWindow.show()
    sys.exit(app.exec_())
