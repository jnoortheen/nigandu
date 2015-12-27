from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('"Nigandu.py"', base=base, targetName = '"Nigandu"')
]

setup(name='noor',
      version = '1.0',
      description = '"sample"',
      options = dict(build_exe = buildOptions),
      executables = executables)
