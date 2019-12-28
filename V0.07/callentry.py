
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QFileDialog
from entry import *
from callserial import MySerial
import time
from pathlib import Path


class MyEntry(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStart.clicked.connect(self.start)
        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.ui.pushButtonOpen.clicked.connect(self.openexisting)
        self.show()
    def openexisting(self):

        self.fileName, OK = fname = QFileDialog.getOpenFileName(self, 'Open file', ".\\","CSV files (*.csv)")
        if OK:
            try:
                lst = self.fileName.split("/")
                filename, extension =lst[-1].split(".")
                filename, extension = Path(self.fileName).name.split(".")
                patient = filename.split("_")
                print(lst)
                self.openMainwindow(patient=tuple(patient), filename=self.fileName)

            except Exception as er:
                print(er)
                self.ui.label.setText("Wrong file type selected")



    def start(self):
        pName = self.ui.lineEditPatientFN.text()
        plName = self.ui.lineEditPatientLN.text()
        pid = self.ui.lineEditPatientD.text()
        _, _, self.pDOB = self.ui.dateEditPatientDOB.text().split('.')
        if pName and plName and pid and self.pDOB:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            patient_data = f"{pName}_{plName}_{pid}_{self.pDOB}.csv"
            self.fileName, OK = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", patient_data,
                                                       "AllFiles(*);;CSV Files(*.csv)", options=options)
            if OK:
                f = open(self.fileName, 'w')


                text = time.ctime()
                f.write(text)
                f.close()

                self.openMainwindow(patient=(self.ui.lineEditPatientFN.text(),
                                 self.ui.lineEditPatientLN.text(),
                                 self.ui.lineEditPatientD.text(),

                                 self.pDOB), filename=self.fileName)
        else:
            self.ui.label.setText("Enter Valid Data")
    def openMainwindow(self, patient, filename):
        print("starting main app")

        self.m=MySerial(patient=patient, filename=filename)
        self.close()
        self.m.show()





if __name__=='__main__':
    app=QApplication(sys.argv)
    entry=MyEntry()
    entry.show()
    sys.exit(app.exec_())
