# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ftp_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 323)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_username = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout_2.addWidget(self.lineEdit_username)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_3.addWidget(self.lineEdit_password)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_homedir = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_homedir.setObjectName("lineEdit_homedir")
        self.horizontalLayout.addWidget(self.lineEdit_homedir)
        self.homedir_btn = QtWidgets.QPushButton(Dialog)
        self.homedir_btn.setObjectName("homedir_btn")
        self.horizontalLayout.addWidget(self.homedir_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.e = QtWidgets.QCheckBox(Dialog)
        self.e.setChecked(True)
        self.e.setObjectName("e")
        self.verticalLayout.addWidget(self.e)
        self.l = QtWidgets.QCheckBox(Dialog)
        self.l.setChecked(True)
        self.l.setObjectName("l")
        self.verticalLayout.addWidget(self.l)
        self.r = QtWidgets.QCheckBox(Dialog)
        self.r.setChecked(True)
        self.r.setObjectName("r")
        self.verticalLayout.addWidget(self.r)
        self.a = QtWidgets.QCheckBox(Dialog)
        self.a.setChecked(True)
        self.a.setObjectName("a")
        self.verticalLayout.addWidget(self.a)
        self.d = QtWidgets.QCheckBox(Dialog)
        self.d.setChecked(True)
        self.d.setObjectName("d")
        self.verticalLayout.addWidget(self.d)
        self.f = QtWidgets.QCheckBox(Dialog)
        self.f.setChecked(True)
        self.f.setObjectName("f")
        self.verticalLayout.addWidget(self.f)
        self.m = QtWidgets.QCheckBox(Dialog)
        self.m.setChecked(True)
        self.m.setObjectName("m")
        self.verticalLayout.addWidget(self.m)
        self.w = QtWidgets.QCheckBox(Dialog)
        self.w.setChecked(True)
        self.w.setObjectName("w")
        self.verticalLayout.addWidget(self.w)
        self.M = QtWidgets.QCheckBox(Dialog)
        self.M.setChecked(True)
        self.M.setObjectName("M")
        self.verticalLayout.addWidget(self.M)
        self.T = QtWidgets.QCheckBox(Dialog)
        self.T.setChecked(True)
        self.T.setObjectName("T")
        self.verticalLayout.addWidget(self.T)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "编辑FTP"))
        self.label_4.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.label_2.setText(_translate("Dialog", "根目录"))
        self.homedir_btn.setText(_translate("Dialog", "选择"))
        self.label.setText(_translate("Dialog", "权限"))
        self.e.setText(_translate("Dialog", "change directory (CWD, CDUP commands)"))
        self.l.setText(_translate("Dialog", "list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)"))
        self.r.setText(_translate("Dialog", "retrieve file from the server (RETR command)"))
        self.a.setText(_translate("Dialog", "append data to an existing file (APPE command)"))
        self.d.setText(_translate("Dialog", "delete file or directory (DELE, RMD commands)"))
        self.f.setText(_translate("Dialog", "rename file or directory (RNFR, RNTO commands)"))
        self.m.setText(_translate("Dialog", "create directory (MKD command)"))
        self.w.setText(_translate("Dialog", "store a file to the server (STOR, STOU commands)"))
        self.M.setText(_translate("Dialog", "change file mode / permission (SITE CHMOD command)"))
        self.T.setText(_translate("Dialog", "change file modification time (SITE MFMT command)"))
