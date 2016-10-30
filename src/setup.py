# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable
import sys

includefiles=["nofts.sqlite", "index.html", "gpl.txt"]
includes = []
excludes = ['Tkinter', 'PyQt5', '_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
              'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
              'Tkconstants', 'cython', 'IdleHistory', 'PyParse', 'PyShell', 'json','kivy', 'idle', 'idlelib', 'turtle', 'turtledemo']
packages = []
path = []

buildOptions =  {"packages": packages, "excludes": excludes, "include_files": includefiles, "path":path}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(script='Nigandu.py', base=base)
]

setup(name='Nigandu',
      version = '1.0.0',
      description = 'Nigandu is the first cross-platform  dictionary application for English to Tamil word meanings.',
      options = dict(build_exe = buildOptions),
      executables = executables)
