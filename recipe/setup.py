import sys
import os
import platform
from distutils.core import setup, Extension

if platform.architecture()[0] == '32bit':
    arch = 'x84'
else:
    arch = 'x64'

libdir = os.path.join('lib', arch)
Leap_i = os.path.join('include', 'Leap.i')

# fix Leap.i
with open(Leap_i, 'r') as handle:
    contents = handle.read().replace('%}}', '}}')
if sys.platform.startswith('win'):
    contents = contents.replace('%include "stdint.i"', '')
with open(Leap_i, 'w') as handle:
    handle.write(contents)

setup(
    name="Leap",
    version=os.getenv("PKG_VERSION", "0"),
    package_dir={'': 'lib'},
    packages=[''],
    ext_modules=[
        Extension("LeapPython",
            [Leap_i],
            swig_opts=['-c++', '-interface', 'LeapPython'],
            include_dirs=['include'],
            libraries=['Leap'],
            library_dirs=[libdir],
        ),
    ],
)
