
'''
this is a required file for cx-freeze
'''

import sys
from cx_Freeze import setup, Executable

myfullpath = "C:\\Users\\gdangca\\OneDrive - Infor\\Projects\\Project - Python\\HR DocSign\\Signature Applet.py"
myscript = "Signature Applet.py"
myscriptexe = "Signature Applet.exe"
appname = "Signature Applet"


def buildexeversion2():

    # Dependencies are automatically detected, but it might need fine tuning.
    build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

    Exe_Param = Executable(
        # what to build
        script=mypath,
        initScript=None,
        base=None,
        # targetDir=r".\\dist",  # needs in Windows format relative to the working dir!
        targetName=myscriptexe,
        # compress=True,
        # copyDependentFiles=True,
        # appendScriptToExe=False,
        # appendScriptToLibrary=False,
        # icon=None
    )

    setup(name="Signature App",
          version="0.1",
          description="This is a signature applet",
          options={"build_exe": build_exe_options},
          executables=[Executable(mypath)])


def buildexeversion2():
    setup(name="Signature Applet",
          version="0.1",
          description="This is a signature applet",
          executables=[Executable(myfullpath)])


def buildexeversion3():
    executables = [Executable(
        myfullpath, base='Win32GUI', shortcutName=appname)]

    setup(
        name=appname,
        executables=executables
    )


buildexeversion3()
