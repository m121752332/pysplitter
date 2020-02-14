# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu,QTableWidget, QTableWidgetItem, QAction,QToolTip,QApplication,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication,Qt,QTimer
from pyspiltter import Ui_pysplitter
import os,sys
from random import randrange
import xlwt

#def deleteDuplicatedElement(list):
#    resultList = []
#    #print(resultList)
#    for item in list:
#        if not item in resultList:
#            resultList.append(item)
#        print(resultList)
#    return resultList

#高速清除重複版 透過利用python中集合元素惟一性特點，將列表轉為集合，將轉為列表返回
def deleteDuplicatedElement(list):
    # return list(set(list))
    return sorted(set(list), key=list.index)

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
        self.datatable.doubleClicked.connect(self.onDoubleClick)
        #self.datatable.addAction(QAction("複製", self.datatable, triggered=self.copyData))
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
        #self.keyPressEvent()

        # 程式初始化
        # self.detail_init()
        self.statusbar.showMessage('開啟完畢', 5000)
        # 設定查詢按鈕功能
        # self.query.triggered.connect(lambda: self.whichbtn(self.query, 'cl'))
        self.exporttoexcel.triggered.connect(lambda: self.writeExcel())
        self.help.triggered.connect(lambda: self.helpme())
        self.help2.triggered.connect(lambda: self.helpme())
        self.lang.triggered.connect(lambda: self.changelang())

        #self.help.triggered.connect(lambda: MessageBox(self.help, text='倒计时关闭对话框', auto=randrange(0, 2)).exec_())
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
        self.editpaste.triggered.connect(self.set_cb)
        self.convert.clicked.connect(self.set_excel)

        # 離開按鈕
        #self.exit.setShortcut('Esc')
        #self.exit2.setShortcut('Esc')
        self.exit.triggered.connect(QCoreApplication.instance().quit)
        self.exit2.triggered.connect(QCoreApplication.instance().quit)

        # 用不到按鈕關閉
        self.editcopy.setEnabled(False)
        self.editcut.setEnabled(False)
        self.insert.setEnabled(False)
        self.modify.setEnabled(False)
        self.delete_2.setEnabled(False)
        self.reproduce.setEnabled(False)
        self.exporttoexcel.setEnabled(False)
        self.invalid.setEnabled(False)
        self.detail.setEnabled(False)
        self.first.setEnabled(False)
        self.previous.setEnabled(False)
        self.jump.setEnabled(False)
        self.next.setEnabled(False)
        self.last.setEnabled(False)

        #QToolTip.setFont(QFont('SansSerif', 10))
        #self.setToolTip('This is a widget')
        self.convert.setToolTip('<b>將PIP過的字串轉回EXCEL資料欄位中</b> [convert]')#使用富文本格式
        self.pipediter.setToolTip('<b>依照區隔符號帶出合併字串</b> [pipediter]')#使用富文本格式
        self.sqlediter.setToolTip('<b>開發者用合併字串</b>[sqlediter]')#使用富文本格式
        self.datatable.setToolTip('<b>將剪貼簿上的資料貼進來</b>[datatable]')#使用富文本格式
        self.datatable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.datatable.customContextMenuRequested.connect(self.generateMenu)
        self.show()

    #資料欄位產生選單功能 多一個複製功能
    def generateMenu(self, pos):
        # rint( pos)
        row_num = -1
        for i in self.datatable.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num >0 :
            menu = QMenu()
            datacopy = menu.addAction(u"複製")
            action = menu.exec_(self.datatable.mapToGlobal(pos))
            if action == datacopy:
                self.copyData()
            else:
                return
        else:
            pass

    # 單身點兩下 顯示欄位資訊
    def onDoubleClick(self, index):
        print(index.row(), index.column(), index.data())

    # 控制ctrl+c
    def keyPressEvent(self, event):
        super(MainWindow, self).keyPressEvent(event)
        # Ctrl + C
        if event.modifiers() == Qt.ControlModifier \
            and event.key() == Qt.Key_C:
            self.copyData()

        # Esc 關閉程式
        if (event.key() == Qt.Key_Escape):
            QCoreApplication.instance().quit()

        # Ctrl + H
        if event.modifiers() == Qt.ControlModifier \
            and event.key() == Qt.Key_H:
            self.helpme()

    def copyData(self):
        count = len(self.datatable.selectedIndexes())
        if count == 0:
            return
        if count == 1:  # 只复制了一个
            QApplication.clipboard().setText(
                self.datatable.selectedIndexes()[0].data())  # 复制到剪贴板中
            QMessageBox.information(self.datatable, "提示", "已複製一列數據")
            return
        rows = set()
        cols = set()
        for index in self.datatable.selectedIndexes():  # 得到所有选择的
            rows.add(index.row())
            cols.add(index.column())
            # print(index.row(),index.column(),index.data())
        if len(rows) == 1:  # 一行
            QApplication.clipboard().setText("\t".join(
                [index.data() for index in self.datatable.selectedIndexes()]))  # 复制
            QMessageBox.information(self.datatable, "提示", "已複製多列數據")
            return
        if len(cols) == 1:  # 一列
            QApplication.clipboard().setText("\r\n".join(
                [index.data() for index in self.datatable.selectedIndexes()]))  # 复制
            QMessageBox.information(self.datatable, "提示", "已複製多列數據")
            return
        mirow, marow = min(rows), max(rows)  # 最(少/多)行
        micol, macol = min(cols), max(cols)  # 最(少/多)列
        print(mirow, marow, micol, macol)
        arrays = [
            [
                "" for _ in range(macol - micol + 1)
            ] for _ in range(marow - mirow + 1)
        ]  # 创建二维数组(并排除前面的空行和空列)
        print(arrays)
        # 填充数据
        for index in self.datatable.selectedIndexes():  # 遍历所有选择的
            arrays[index.row() - mirow][index.column() - micol] = index.data()
        print(arrays)
        data = ""  # 最后的结果
        for row in arrays:
            data += "\t".join(row) + "\r\n"
        print(data)
        QApplication.clipboard().setText(data)  # 复制到剪贴板中
        QMessageBox.information(self.datatable, "提示", "已複製")

    def whichbtn(self, btn, db='cl'):
        #print("sel db="+db)
        self.alertmsg.setText('查詢完畢!')

    # 向剪贴板中写入
    def set_excel(self):
        pipstr = ""
        pipstr = self.pipediter.toPlainText()
        #先修正不可換行
        pipstr = pipstr.replace("\n", "")
        self.pipediter.setText(pipstr)



        #取到區隔方式
        classtype = self.comboBox.currentIndex()
        #self.alertmsg.setText('class='+str(classtype))
        piptype = ''
        if str(classtype) == '0':
            piptype = '|'
        elif str(classtype) == '1':
            #print(str(classtype))
            piptype = ','
        elif str(classtype) == '2':
            #print(str(classtype))
            piptype = ';'
        else:
            pass

        wordlist = pipstr.split(piptype)
        #清掉重複
        wordlist = deleteDuplicatedElement(wordlist)
        self.datatable.setRowCount(len(wordlist))
        g_rec_b = len(wordlist)
        #print("g_rec_b=%d"%g_rec_b)
        for i in range(0, g_rec_b):
            #print(i, str(wordlist[i]))
            if str(wordlist[i]) == '':
                pass
            else:
                cell = QTableWidgetItem(str(wordlist[i]))
                self.datatable.setItem(i, 0, cell)

        #轉換list到sqllist
        self.set_pipediter(wordlist)
        sqllist = str(wordlist).replace('[','(').replace(']',')')
        self.sqlediter.setText(sqllist)

    # 向剪贴板中写入
    def set_cb(self):
        # mdata = self.cb.mimeData()
        # print(type(mdata))
        word = self.cb.mimeData().text()
        # print(word)
        wordlist = word.split('\n')
        wordlist = [i for i in wordlist if i != '']

        wordlist = deleteDuplicatedElement(wordlist)
        excellist = []
        # print(wordlist)
        # self.sqlediter.setText(word.text())
        self.datatable.setRowCount(len(wordlist))
        g_rec_b = len(wordlist)
        for i in range(0, g_rec_b):
            #print(i, str(wordlist[i]))
            if str(wordlist[i]) == '':
                pass
            else:
                cell_str = str(wordlist[i])
                cell_str = cell_str.replace("\r", "")
                #print("list = %s" % str(excellist))
                excellist.append(cell_str)
                cell = QTableWidgetItem(cell_str)
                self.datatable.setItem(i, 0, cell)
        self.set_pipediter(excellist)

    def set_pipediter(self, excellist):
        #print("list = %s" % str(excellist))
        #print("tuple = %s" % str(tuple(excellist)))
        sqllist = str(excellist).replace('[','(').replace(']',')')

        self.sqlediter.setText(sqllist)
        classtype = self.comboBox.currentIndex()
        self.alertmsg.setText('class='+str(classtype))
        pip = ''
        if str(classtype) == '0':
            #print(str(classtype))
            pip = "|".join(excellist)
        elif str(classtype) == '1':
            #print(str(classtype))
            pip = ",".join(excellist)
        elif str(classtype) == '2':
            #print(str(classtype))
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

    def helpme(self):
        #QMessageBox.information(self, "開發人員", "<b>由泰哥承製開發</b><br><br>歡迎洽詢")
        reply = QMessageBox.information(self,                         #使用infomation信息框
                "開發人員",
                "<b><font color='red'>版本: 1.03</b></font><br>"\
                "<b>由泰哥承製開發</b><br><br>歡迎洽詢",
                QMessageBox.Yes)

    def changelang(self):
        #QMessageBox.information(self, "開發人員", "<b>由泰哥承製開發</b><br><br>歡迎洽詢")
        reply = QMessageBox.about(self,                         #使用infomation信息框
                                    "切換語言",
                                    "<b>不支援喔，請確認</b>")

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
