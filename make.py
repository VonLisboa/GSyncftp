import os

key = "key_16_caracters"
tools = os.getcwd() + "\\tools"
icons = os.getcwd() + "\\icons\\main.ico"
version = os.getcwd() + "\\version.txt"
compile_path = os.getenv('TEMP') + '\\py_compile_tmp'

os.system("pyinstaller --clean " +
          "--workpath {} ".format(compile_path) +
          "--specpath {} ".format(compile_path) +
          # "--upx-dir {}  ".format(tools) +
          "--icon {} ".format(icons) +
          # "--key {} ".format(key.encode('utf-8')) +
          "--version-file={} ".format(version) +
          # "--upx-exclude vcruntime140.dll "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\synced.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync1.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync2.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync3.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync4.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync5.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync6.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync7.ico\";icons "
          "--add-data \"C:\\Users\\glaucio\\PycharmProjects\\GSyncftp\\icons\\sync8.ico\";icons "
          "--exclude-module Tkinter "
          "--exclude-module tkinter "
          "--exclude-module _tkinter "
          "--exclude-module tk "
          "--exclude-module tcl "
          "--exclude-module FixTk "
          "--noconsole "
          # "--onefile "
          "{}\\Main.py".format(os.getcwd()))
