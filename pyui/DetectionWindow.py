# Katarzyna Zaleska
# WCY19IJ1S1

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DetectionWindow(object):
    def setupUi(self, DetectionWindow):
        DetectionWindow.setObjectName("DetectionWindow")
        DetectionWindow.resize(996, 592)
        DetectionWindow.setStyleSheet("QDialog {\n"
"background-color:  #2a292e;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color: #1db954;\n"
"border: 2px solid #1db954;\n"
"border-radius: 14px;\n"
"letter-spacing: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"color: #121212;\n"
"background-color:     #1db954;\n"
"border: 2px solid #121212;\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DetectionWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 25, 25, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.detected_gesture_name = QtWidgets.QLabel(DetectionWindow)
        self.detected_gesture_name.setObjectName("detected_gesture_name")
        self.verticalLayout_4.addWidget(self.detected_gesture_name)
        self.detection_confidence = QtWidgets.QLabel(DetectionWindow)
        self.detection_confidence.setObjectName("detection_confidence")
        self.verticalLayout_4.addWidget(self.detection_confidence)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.detection_camera = QtWidgets.QLabel(DetectionWindow)
        self.detection_camera.setText("")
        self.detection_camera.setObjectName("detection_camera")
        self.verticalLayout_3.addWidget(self.detection_camera)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_2 = QtWidgets.QPushButton(DetectionWindow)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 56))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 56))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DetectionWindow)
        QtCore.QMetaObject.connectSlotsByName(DetectionWindow)

    def retranslateUi(self, DetectionWindow):
        _translate = QtCore.QCoreApplication.translate
        DetectionWindow.setWindowTitle(_translate("DetectionWindow", "Detection"))
        self.detected_gesture_name.setText(_translate("DetectionWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.detection_confidence.setText(_translate("DetectionWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("DetectionWindow", "START"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DetectionWindow = QtWidgets.QDialog()
#     ui = Ui_DetectionWindow()
#     ui.setupUi(DetectionWindow)
#     DetectionWindow.show()
#     sys.exit(app.exec_())
