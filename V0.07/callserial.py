import sys
from serial.tools import list_ports
import serial
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizePolicy
from PyQt5.QtGui import QColor
from serialdemo import *
from threading import Thread
import time
import cProfile
import numpy as np


# from playsound import playsound


class MySerial(QMainWindow):
    def __init__(self, patient, filename):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.col = QColor
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showgraph)
        self.smtimer = QtCore.QTimer(self)
        self.smtimer.timeout.connect(self.samplerate)
        self.smtimer.start(1000)
        self.seriallist = []
        self.record = False
        self.begining = time.time()
        self.monitor = False
        self.t = Thread(target=self.startmonitor, daemon=True)
        self.serials()
        self.pName, self.pLName, self.pid, self.DOB = patient
        self.filename = filename
        self.setWindowTitle(
            f"{filename}      Patien İD: {self.pid}, {self.pName} {self.pLName},  Birth Year: {self.DOB} ")
        self.ui.pushButtonRefeshPorts.clicked.connect(self.serials)
        self.ui.textBrowser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.pushButtonStartM.clicked.connect(self.startthread)
        self.ui.pushButtonStopM.clicked.connect(self.stopmonitor)
        self.ui.pushButtonGraph.clicked.connect(self.starttimer)
        self.ui.pushButtonClear.clicked.connect(self.clear)
        self.ui.pushButtonRecord.clicked.connect(self.recordtgl)
        self.ui.pushButtonAnalyze.clicked.connect(self.rranalyzer)
        self.ui.widget.mouseEnabled = False
        self.graphWidget = pg.PlotWidget()
        self.ui.spinBoxFps.valueChanged.connect(self.starttimer)
        self.tm = 0.
        self.rrarray = np.array([])
        self.rr = 0.
        self.rrylist = []
        self.rrxlist = []
        self.trsh = []
        self.xlist = []
        self.ylist = []
        self.tm_previus = 0.
        self.counter = 0
        self.samrate = 0
        self.starttimer()
        self.show()

    def autothreshold(self):
        if self.monitor and self.ui.checkBoxAutoTrsh.isChecked():
            try:
                last1000 = np.array(self.ylist[-1000:-1])
                trs = last1000.max()
                self.ui.verticalSliderTrsh.setValue(trs - 30)
            except:
                pass


    def rranalyzer(self):
        rrarray = np.array(self.rrylist)
        self.ui.textBrowser.append(str(len(self.rrylist)) + " RR's recorded ")
        self.ui.textBrowser.append("STD : " + str(rrarray.std()))
        self.ui.textBrowser.append("Shortest :" + str(rrarray.min()))
        self.ui.textBrowser.append("Longest :" + str(rrarray.max()))
    def hrupdate(self, rr):
        self.ui.labelHR.setText("HR is :" + str(60000 // rr))

    def recordtgl(self):
        if self.record:
            self.record = False
            self.ui.pushButtonRecord.setText("Recording Stopped")
            self.ui.checkBoxECG.setEnabled(True)
        else:
            self.record = True
            self.ui.pushButtonRecord.setText("Recording...")
            self.ui.checkBoxECG.setEnabled(False)

    def recorder(self, timestamp="", ecg="", treshold="", rr="_", extension=""):
        if self.record:
            if self.ui.checkBoxECG.isChecked():
                try:
                    with open((self.filename + extension), "a") as data:
                        rr = str(rr).replace(".", ",", 1)
                        print(f"{str(timestamp)};{str(ecg)};{str(treshold)};{rr}", file=data)
                except:
                    print("cant write")
            else:
                if not rr == "":
                    with open((self.filename + extension), "a") as data:
                        rr = str(rr).replace(".", ",", 1)
                        print(f"{str(timestamp)};;;{rr}", file=data)

    def samplerate(self):
        sr = len(self.xlist) - self.samrate
        self.samrate = len(self.xlist)
        self.ui.labelSampRate.setText(str(sr) + " Samples/Second")
        self.autothreshold()

    def starttimer(self):

        self.timeout = int(1000 / self.ui.spinBoxFps.value())
        self.timer.start(self.timeout)

    def serials(self):
        self.ui.comboBoxPorts.clear()
        self.seriallist = list_ports.comports()
        for i in self.seriallist:
            self.ui.comboBoxPorts.addItem(str(i))

    def startmonitor(self):

        if len(self.seriallist) > 0:
            comport, _ = self.ui.comboBoxPorts.currentText().split('-')
            comport = comport.strip()
            self.ui.textBrowser.append("----MONİTOR STARTED----")
            with serial.Serial(comport, 9600) as series:
                aprevius = 0
                slopeprevius = 0
                tm = 0
                rr = ""
                abowetrsh = []
                rpreviustime = 0
                while True:
                    serialline = series.readline()
                    # self.ui.textBrowser.append(str(serialline.strip())[1:])
                    try:
                        a = int(serialline)
                        slope = (a - aprevius)
                        self.ylist.append(a)
                        timestamp = int((time.time() - self.begining) * 1000)
                        self.xlist.append(timestamp)
        # Plot Threshold-------------------------
                        if len(self.trsh) >= 1001:
                            self.trsh.pop(0)
                            self.trsh.append(self.ui.verticalSliderTrsh.value())
                        else:
                            self.trsh.append(self.ui.verticalSliderTrsh.value())
        # Plot With First Pick Method------------
                        if self.ui.radioButtonFP.isChecked():
                            if aprevius > int(self.ui.verticalSliderTrsh.value()):
                                if slopeprevius >= 0 and slope <= 0:
                                    if self.counter < 1:
                                        tm = self.tm
                                        self.rr = tm - self.tm_previus
                                        if 10000 > self.rr > 3:
                                            self.rrylist.append(self.rr)
                                            rr = self.rr
                                        else:
                                            rr = ""
                                        self.counter += 1
                                        self.hrupdate(rr=rr)
                                    else:
                                        rr = ""
                            else:
                                self.tm_previus = tm
                                self.counter = 0
                                rr = ""
                        self.tm = timestamp
                        slopeprevius = slope
                        aprevius = a
    # Plot with Max Pick Method
                        if self.ui.radioButtonMP.isChecked():
                            if a > int(self.ui.verticalSliderTrsh.value()):
                                abowetrsh.append([a, timestamp])
                                rr=""
                            else:
                                if len(abowetrsh) > 0:
                                    array = np.array(abowetrsh)
                                    rtime = array[array[::, 0].argmax(), 1]
                                    if rpreviustime:
                                        self.rr = rtime - rpreviustime
                                        self.rrylist.append(self.rr)
                                        rr = self.rr
                                        self.hrupdate(rr=rr)
                                    rpreviustime = rtime
                                    abowetrsh = []
                                else:
                                    rr=""
                        if rr:
                            self.autothreshold()
                        self.recorder(timestamp=timestamp, ecg=a, treshold=self.ui.verticalSliderTrsh.value(), rr=rr)
                    except Exception as er:
                        print(er)
                        print("something went wrong")

                    self.ui.textBrowser.verticalScrollBar().setValue(self.ui.textBrowser.verticalScrollBar().maximum())
                    if not self.monitor:
                        break

        else:
            self.ui.textBrowser.setText("no ports found")

    def startthread(self):
        self.ui.pushButtonRecord.setEnabled(True)
        self.ui.pushButtonStopM.setEnabled(True)
        self.ui.radioButtonFP.setEnabled(False)
        self.ui.radioButtonMP.setEnabled(False)
        self.monitor = True
        self.t = Thread(target=self.startmonitor, daemon=True)
        self.t.start()
        self.ui.pushButtonStartM.setText("Monitor Running.")

    def stopmonitor(self):
        self.ui.pushButtonRecord.setEnabled(False)
        self.ui.pushButtonStopM.setEnabled(False)
        self.ui.radioButtonMP.setEnabled(True)
        self.ui.radioButtonFP.setEnabled(True)
        if self.record:
            self.recordtgl()
        self.monitor = False
        time.sleep(1)
        self.ui.textBrowser.append("----MONİTOR STOPED----")
        self.ui.pushButtonStartM.setText("Start Monitor")

    def showgraph(self):
        plotslice = self.ui.horizontalSliderZoom.value()
        self.ui.widgetRRplot.plot(self.rrylist, clear=True)
        self.ui.widget.plot(self.xlist[plotslice:-1], self.trsh[plotslice:-1], clear=True,
                            pen=pg.mkPen('r', style=QtCore.Qt.DotLine))

        self.ui.widget.plot(self.xlist[plotslice:-1], self.ylist[plotslice:-1])

    def clear(self):
        self.xlist = []
        self.ylist = []
        self.trsh = []
        self.rrylist = []
        self.ui.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    M = MySerial()
    M.show()
    sys.exit(app.exec_())
