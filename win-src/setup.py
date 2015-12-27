# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

includefiles=["nofts.sqlite", "index.html", "gpl.txt"]
includes = []
excludes = ['Tkinter', 'PyQt5', '_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
              'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
              'Tkconstants', 'cython', 'IdleHistory', 'PyParse', 'PyShell', 'json','kivy', 'idle', 'idlelib', 'turtle', 'turtledemo']
packages = []
path = []

build_exe_options = {"packages": packages, "excludes": excludes, "include_files": includefiles, "path":path}


base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Nigandu",
        version = "1.0.0",
        description = "Nigandu is the first cross-platform  dictionary application for English to Tamil word meanings.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Nigandu.py", base=base)])