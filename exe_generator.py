import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files":["icon.png"], "build_exe": "build/GoDoku"}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="GoDoku",
    version="1.0",
    author="aurims",
    description="Sudoku solver",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name='GoDoku.exe', icon="icon.ico")],
)

#env\Scripts\activate.bat
#python exe_generator.py build