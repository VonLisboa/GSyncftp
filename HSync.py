import asyncio
import json
import os
import sys
import threading
import time

# from asyncqt import QEventLoop
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QListWidgetItem
from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QMenu, qApp

from FileUtils import WatchFiles
from controller.CLogin import Login
from controller.CLoginSession import LoginSession
from controller.CSyncFolder import SyncFolder, SyncSession
from controller.CTasklist import Tasklist
from controller.CUpload import UploadFiles

APP_PATH = None
SYNC_RUNNING = False

if getattr(sys, 'frozen', False):
    APP_PATH = os.path.dirname(sys.executable)
elif __file__:
    APP_PATH = os.path.dirname(__file__)
# print(APP_PATH)


def resource_path(relative_path):
    base_path = None
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.executable)))
    elif __file__:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return base_path + relative_path


CONFIGS = {}
if os.path.isfile(APP_PATH + "\\config.json"):
    with open(APP_PATH + "\\config.json") as config_file:
        CONFIGS = json.load(config_file)


@pyqtSlot("QWidget*", "QWidget*")
def on_focus_out(old, now):
    if not now:
        if isinstance(old, Login) or isinstance(old.parent(), Login):
            app.closeAllWindows()
            return
        if isinstance(old, SyncFolder) or isinstance(old.parent(), SyncFolder):
            app.closeAllWindows()
            return
        if isinstance(old, Tasklist) or isinstance(old.parent(), Tasklist) or isinstance(old.parent().parent(),
                                                                                         Tasklist):
            app.closeAllWindows()


def toggle_menu_autosync(state):
    if state:
        monitor_files.run(CONFIGS['path_sync'])
    else:
        monitor_files.stop()
    CONFIGS['autosync'] = state
    with open(APP_PATH + "\\config.json", 'w') as f:
        json.dump(CONFIGS, f)


is_logged = lambda fn: lambda: fn() if session.logged_status else Login(session, fn).exec_()


def logout():
    session.logged_status = False


def swap_icon():
    global SYNC_RUNNING
    task.status_sync()
    while SYNC_RUNNING:
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync1.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync2.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync3.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync4.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync5.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync6.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync7.ico")))
        time.sleep(.2)
        tray_icon.setIcon(QIcon(resource_path("\\icons\\sync8.ico")))
        time.sleep(.2)
    tray_icon.setIcon(QIcon(resource_path("\\icons\\synced.ico")))
    task.status_synced()


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
qApp.focusChanged.connect(on_focus_out)

menu_login = QAction('Login')
menu_login.triggered.connect(lambda: logout() if session.logged_status else Login(session).exec_())
session = LoginSession()
session.logged.connect(
    lambda status: menu_login.setText('Logout') if status else menu_login.setText('Login'))  # pyqtSlot
Login(session).exec_()

menu = QMenu()
menu_checkbox = QAction('Auto Sync', menu, checkable=True)
menu_checkbox.triggered.connect(toggle_menu_autosync)
menu_checkbox.setChecked(CONFIGS['autosync'])
menu.addAction(menu_checkbox)


@pyqtSlot(object)
def update_tasklist(files):
    ####
    # receive array of files to upload from SyncFolder
    ###
    global SYNC_RUNNING
    files_name = lambda x: list(map(os.path.basename, x))

    if files and len(files) > 0:
        if task.isVisible() and task.not_in_animation():
            files = files_name(files)
            task.listWidget.clear()
            task.listWidget.addItems(files)
    else:
        SYNC_RUNNING = False
        task.listWidget.clear()
        task.listWidget.addItem("Nenhum arquivo na fila")


@pyqtSlot(str)
def new_upload_instance(path_folder):
    global SYNC_RUNNING
    try:
        # loop = QEventLoop(app)
        # asyncio.set_event_loop(loop)
        upload_instance = UploadFiles(CONFIGS['path_sync'], path_folder)
        upload_instance.files.connect(update_tasklist)
        t = threading.Thread(target=upload_instance.run)
        t.start()
        SYNC_RUNNING = True
        t2 = threading.Thread(target=swap_icon)
        t2.start()
    except Exception as e:
        print(e)


def finalize():
    asyncio.get_running_loop().close()
    asyncio.get_event_loop().close()
    app.quit()

sync_session = SyncSession()
sync_session.sending_folder.connect(new_upload_instance)
menu.addAction('Manual Sync').triggered.connect(is_logged(lambda: SyncFolder(CONFIGS["path_sync"], sync_session).exec_()))
menu.addAction(menu_login)
menu.addAction("Exit").triggered.connect(lambda: finalize())

task = Tasklist()
tray_icon = QSystemTrayIcon(QIcon(resource_path("\\icons\\synced.ico")), app)
tray_icon.activated.connect(
    lambda: task.exec_() if Qt.LeftButton and not task.isVisible() and not menu.isVisible() else task.close())
tray_icon.setContextMenu(menu)
tray_icon.show()

monitor_files = WatchFiles()
monitor_files.run(CONFIGS['path_sync']) if CONFIGS['autosync'] else None

sys.exit(app.exec_())
