# -*- coding: utf-8 -*-
import json
import sys
import threading
import time
import multiprocessing
import os
import logging

from PyQt5 import QtWidgets

from ftp_win import Ui_Dialog
from log_win import Ui_Dialog as Log_Dialog
from main_win import Ui_MainWindow
from help_win import Ui_Dialog as Help_Dialog
from main import ftp_server

SETTINGS = {}
PROCESS = None
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'fileZoneServer.log'), level=logging.INFO)


def get_data(dui: Ui_Dialog):
    username = dui.lineEdit_username.text()
    password = dui.lineEdit_password.text()
    homedir = dui.lineEdit_homedir.text()
    perm = ''
    if dui.e.isChecked():
        perm += 'e'
    if dui.l.isChecked():
        perm += 'l'
    if dui.r.isChecked():
        perm += 'r'
    if dui.a.isChecked():
        perm += 'a'
    if dui.d.isChecked():
        perm += 'd'
    if dui.f.isChecked():
        perm += 'f'
    if dui.m.isChecked():
        perm += 'm'
    if dui.w.isChecked():
        perm += 'w'
    if dui.M.isChecked():
        perm += 'M'
    if dui.T.isChecked():
        perm += 'T'
    return {"username": username, "password": password, "homedir": homedir, "perm": perm}


def add_line(data: dict):
    row = ui.tableWidget.rowCount()
    ui.tableWidget.setRowCount(row + 1)
    ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['username']))
    ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data['password']))
    ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data['homedir']))
    ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data.get('perm', '')))
    widget = QtWidgets.QWidget()
    hbox = QtWidgets.QHBoxLayout(widget)
    edit_btn = QtWidgets.QPushButton('编辑')
    edit_btn.clicked.connect(edit_ftp)
    hbox.addWidget(edit_btn)
    delete_btn = QtWidgets.QPushButton('删除')
    delete_btn.clicked.connect(delete_ftp)
    hbox.addWidget(delete_btn)
    ui.tableWidget.setCellWidget(row, 4, widget)
    ui.tableWidget.resizeColumnsToContents()
    ui.tableWidget.resizeRowsToContents()


def select_folder(lineEdit: QtWidgets.QLineEdit):
    folder = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "选择文件夹", os.path.expanduser("~"))
    lineEdit.setText(folder)


def delete_ftp():
    global SETTINGS
    btn = MainWindow.sender()
    cell = ui.tableWidget.indexAt(btn.parent().pos())
    ui.tableWidget.removeRow(cell.row())
    SETTINGS['users'].pop(cell.row())


def edit_ftp():
    global SETTINGS
    dialog = QtWidgets.QDialog()
    dui = Ui_Dialog()
    dui.setupUi(dialog)
    dui.homedir_btn.clicked.connect(lambda: select_folder(dui.lineEdit_homedir))
    btn = MainWindow.sender()
    cell = ui.tableWidget.indexAt(btn.parent().pos())
    dui.lineEdit_username.setText(ui.tableWidget.item(cell.row(), 0).text())
    dui.lineEdit_password.setText(ui.tableWidget.item(cell.row(), 1).text())
    dui.lineEdit_homedir.setText(ui.tableWidget.item(cell.row(), 2).text())
    perm = ui.tableWidget.item(cell.row(), 3).text()
    dui.e.setChecked(True if 'e' in perm else False)
    dui.l.setChecked(True if 'l' in perm else False)
    dui.r.setChecked(True if 'r' in perm else False)
    dui.a.setChecked(True if 'a' in perm else False)
    dui.d.setChecked(True if 'd' in perm else False)
    dui.f.setChecked(True if 'f' in perm else False)
    dui.m.setChecked(True if 'm' in perm else False)
    dui.w.setChecked(True if 'w' in perm else False)
    dui.M.setChecked(True if 'M' in perm else False)
    dui.T.setChecked(True if 'T' in perm else False)
    if dialog.exec_():
        data = get_data(dui)
        ui.tableWidget.setItem(cell.row(), 0, QtWidgets.QTableWidgetItem(data['username']))
        ui.tableWidget.setItem(cell.row(), 1, QtWidgets.QTableWidgetItem(data['password']))
        ui.tableWidget.setItem(cell.row(), 2, QtWidgets.QTableWidgetItem(data['homedir']))
        ui.tableWidget.setItem(cell.row(), 3, QtWidgets.QTableWidgetItem(data['perm']))
        SETTINGS['users'][cell.row()] = data
        write_config()


def add_ftp():
    global SETTINGS
    dialog = QtWidgets.QDialog()
    dui = Ui_Dialog()
    dui.setupUi(dialog)
    dui.homedir_btn.clicked.connect(lambda: select_folder(dui.lineEdit_homedir))
    if dialog.exec_():
        data = get_data(dui)
        add_line(data)
        SETTINGS['users'].append(data)
        write_config()


def change_port():
    global SETTINGS
    port, ok = QtWidgets.QInputDialog.getInt(MainWindow, "修改端口", "请输入新的端口号", SETTINGS['port'], 0, 65535)
    if ok:
        SETTINGS['port'] = port
        write_config()


def refresh_log(browser: QtWidgets.QTextBrowser):
    browser.setText("")
    with open(os.path.join(os.path.dirname(__file__), 'fileZoneServer.log'), 'r') as f:
        browser.setText(f.read())


def clear_log(browser: QtWidgets.QTextBrowser):
    browser.setText("")
    with open(os.path.join(os.path.dirname(__file__), 'fileZoneServer.log'), 'w') as f:
        f.write("")


def show_log():
    dialog = QtWidgets.QDialog()
    lui = Log_Dialog()
    lui.setupUi(dialog)
    with open(os.path.join(os.path.dirname(__file__), 'fileZoneServer.log'), 'r') as f:
        lui.textBrowser.setText(f.read())
    lui.refresh.clicked.connect(lambda: refresh_log(lui.textBrowser))
    lui.clear.clicked.connect(lambda: clear_log(lui.textBrowser))
    dialog.exec_()


def check_running():
    time.sleep(10)
    global PROCESS
    if PROCESS is not None and PROCESS.is_alive():
        ui.statusbar.clearMessage()
        ui.statusbar.showMessage(f"Server running, Listening on port {SETTINGS['port']}")
    else:
        ui.statusbar.clearMessage()
        ui.statusbar.showMessage("Server start failed")
        ui.start_btn.setDisabled(False)


def start_handler():
    global PROCESS
    if PROCESS is None or not PROCESS.is_alive():
        ui.statusbar.clearMessage()
        ui.statusbar.showMessage("Starting")
        ui.start_btn.setDisabled(True)
        PROCESS = multiprocessing.Process(target=ftp_server, args=(SETTINGS,))
        PROCESS.start()
        thread = threading.Thread(target=check_running)
        thread.start()


def stop_handler():
    global PROCESS
    if PROCESS is not None and PROCESS.is_alive():
        PROCESS.terminate()
        PROCESS.join()
        PROCESS = None
        logging.info(">>> Stop <<<")
        ui.statusbar.clearMessage()
        ui.statusbar.showMessage("Server stopped")
        ui.start_btn.setDisabled(False)


def restart_handler():
    stop_handler()
    time.sleep(1)
    start_handler()


def help_handler():
    dialog = QtWidgets.QDialog()
    dui = Help_Dialog()
    dui.setupUi(dialog)
    dialog.exec_()


def load_config():
    global SETTINGS
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'fileZoneServer.json')):
        with open(os.path.join(os.path.dirname(__file__), 'fileZoneServer.json'), "r") as f:
            try:
                SETTINGS = json.loads(f.read())
            except json.JSONDecodeError:
                pass
    if "port" not in SETTINGS:
        SETTINGS["port"] = 2121
    if "users" not in SETTINGS:
        SETTINGS["users"] = []
    for user in SETTINGS["users"]:
        add_line(user)


def write_handler():
    with open(os.path.join(os.path.dirname(__file__), 'fileZoneServer.json'), "w") as f:
        f.write(json.dumps(SETTINGS))


def write_config():
    threading.Thread(target=write_handler).start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_btn.clicked.connect(add_ftp)
    ui.port_btn.clicked.connect(change_port)
    ui.log_btn.clicked.connect(show_log)
    ui.start_btn.clicked.connect(start_handler)
    ui.stop_btn.clicked.connect(stop_handler)
    ui.help_btn.clicked.connect(help_handler)
    ui.restart_btn.clicked.connect(restart_handler)
    load_config()
    ui.statusbar.clearMessage()
    ui.statusbar.showMessage("Ready")
    MainWindow.show()
    sys.exit(app.exec_())
