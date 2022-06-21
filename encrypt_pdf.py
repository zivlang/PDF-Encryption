import random
import string

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

stylesheet = """
    QMainWindow {
    border-image: url(Hadassah_transparent.png) 0 0 0 0 stretch stretch;
    background-repeat: no-repeat;
    background-position: center;
    }
    """


class Ui_PDF_files_encryption(object):
    def setupUi(self, PDF_files_encryption):
        PDF_files_encryption.setObjectName("PDF_files_encryption")
        PDF_files_encryption.resize(1252, 835)
        PDF_files_encryption.setMinimumSize(QtCore.QSize(0, 600))
        PDF_files_encryption.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(PDF_files_encryption)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.open_select_files_dialog = QtWidgets.QPushButton(self.horizontalFrame)
        self.open_select_files_dialog.setEnabled(True)
        self.open_select_files_dialog.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        self.open_select_files_dialog.setFont(font)
        self.open_select_files_dialog.setObjectName("open_select_files_dialog")
        self.horizontalLayout.addWidget(self.open_select_files_dialog)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalFrame_2)
        self.lineEdit.setFont(font)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(360, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.horizontalFrame_2)

        self.horizontalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame1)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.horizontalFrame_3 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.horizontalFrame_3)
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.verticalFrame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 450))
        self.tableWidget.setMaximumSize(QtCore.QSize(302, 450))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        spacerItem9 = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.frame_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        PDF_files_encryption.setCentralWidget(self.centralwidget)
        self.retranslateUi(PDF_files_encryption)
        QtCore.QMetaObject.connectSlotsByName(PDF_files_encryption)

    def retranslateUi(self, PDF_files_encryption):
        _translate = QtCore.QCoreApplication.translate
        PDF_files_encryption.setWindowTitle(_translate("PDF_files_encryption", "PDF Files Encryption"))
        self.label.setText(_translate("PDF_files_encryption", "PDF Files Encryption"))
        self.open_select_files_dialog.setText(_translate("PDF_files_encryption", "Select PDF files"))
        self.pushButton_2.setText(_translate("PDF_files_encryption", "Get password"))
        self.pushButton.setText(_translate("PDF_files_encryption", "Set password"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PDF_files_encryption", "File"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PDF_files_encryption", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PDF_files_encryption", "Status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PDF_files_encryption", ''))


def copy_password(password):
    clipboard.setText(password)


class EncryptPDF(QtWidgets.QMainWindow, Ui_PDF_files_encryption):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_PDF_files_encryption()
        self.ui.setupUi(self)
        self.ui.label_3.setStyleSheet('color: red')
        self.ui.open_select_files_dialog.clicked.connect(self.select_files_click)
        self.ui.pushButton.clicked.connect(self.set_password_click)
        self.ui.pushButton_2.clicked.connect(self.generate_password)
        self.ui.lineEdit.returnPressed.connect(self.set_password_click)
        self.password = ''
        self.files = []
        self.file = ''
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

    def generate_password(self):
        password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 16))
        self.ui.lineEdit.setText(password)

    def copy_password(self):
        print(self)

    def insert_datum(self, rows_number, i, item):
        datum = QtWidgets.QTableWidgetItem(item)
        self.ui.tableWidget.setItem(rows_number, i, datum)
        datum.setTextAlignment(QtCore.Qt.AlignCenter)

    def insert_to_table(self, file_password_results):
        rows_number = self.ui.tableWidget.rowCount()  # getting the number of rows in the table
        self.ui.tableWidget.insertRow(rows_number)  # creating a new row
        for i, item in enumerate(file_password_results):
            self.insert_datum(rows_number, i, item)
        if 'Error' not in file_password_results:
            copy_button = QtWidgets.QPushButton()
            copy_button.setText('Copy Password')
            self.ui.tableWidget.setCellWidget(rows_number, 3, copy_button)
            # Todo: debug the following line.
            copy_button.clicked.connect(lambda: copy_password(file_password_results[1]))

    def set_password_click(self):
        password = self.ui.lineEdit.text()
        if len(password) < 8:
            self.ui.label_3.setText('The password must be at least 8 characters long')
            self.ui.label_3.show()
            return
        else:
            self.ui.label_3.setText('asdasd')
            result = self.encrypt_pdf(password, self.files[0])
            self.ui.label_3.setText('')

        if not self.ui.tableWidget.isEnabled():
            self.ui.tableWidget.setEnabled(True)
            self.ui.tableWidget.setStyleSheet(
                "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "padding:4px;"
                "}"
                "QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "}"
            )
        file_password_result = [self.files[0].split('/')[-1], password]
        if result:
            file_password_result.append('Done')
        else:
            file_password_result.append('Error')

        self.insert_to_table(file_password_result)

        if len(self.files) > 1:
            self.files = self.files[1:]
            self.ui.label_2.setText(f'File: "{self.files[0].split("/")[-1]}"')
            self.ui.lineEdit.clear()
        else:
            self.ui.pushButton.setDisabled(True)
            self.ui.label_2.setText('')
            self.ui.lineEdit.clear()
            self.ui.lineEdit.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)

    def is_encrypted(input_file: str) -> bool:
        """Checks if the inputted file is encrypted using PyPDF4 library"""
        with open(input_file, 'rb') as pdf_file:
            pdf_reader = PdfFileReader(pdf_file, strict=False)
            return pdf_reader.is_encrypted

    def encrypt_pdf(self, password, input_file):
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
        if pdf_reader.is_encrypted:
            self.ui.label_3.setText('The file is already encrypted')
            self.ui.label_3.show()
            return True
        try:
            for page_number in range(len(pdf_reader.pages)):
                pdf_writer.addPage(pdf_reader.pages[page_number])
                pdf_writer.encrypt(password)

                open(input_file[:-4] + '_encrypted.pdf', 'a').close()
                with open(input_file[:-4] + '_encrypted.pdf', 'ab') as output:
                    pdf_writer.write(output)
            return True

        except Exception as e:
            self.ui.label_3.setText(f"Error reading PDF File {input_file.split('/')[-1]}.")
            print(e)
            self.ui.label_3.setStyleSheet('font-size: 25%; color: red')
            self.ui.label_3.show()
            return False

    def select_files_click(self):
        self.files = QtWidgets.QFileDialog.getOpenFileNames(self, "Select PDF Files", "~", 'PDF files (*.pdf)')[0]
        if not self.files:
            return
        self.ui.pushButton_2.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit.setPlaceholderText('Type a password here, or click "Get password"')
        self.ui.pushButton.setEnabled(True)
        self.ui.label_2.setText(f'File: "{self.files[0].split("/")[-1]}"')


if __name__ == "__main__":
    import sys

    app1 = QApplication(sys.argv)
    app1.setStyleSheet(stylesheet)  # <---
    clipboard = app1.clipboard()
    window = EncryptPDF()
    window.show()
    sys.exit(app1.exec_())

    # Creating the EXE file:
    # pyinstaller --onefile --clean --windowed --add-data "*.png;." encrypt_pdf.py