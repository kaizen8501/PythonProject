from distutils.core import setup
import py2exe, sys, os
from glob import glob

sys.argv.append('py2exe')
#sys.path.append("C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT")


setup(
	options = {'py2exe':{'bundle_files':1}},
	windows = [{'script':'S2E_TestTool.py'}],
	zipfile = None,
)
