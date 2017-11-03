#!/bin/bash

cd LeapSDK

if [[ "`uname`" == "Darwin" ]]; then
    libdir=lib
    install_name_tool -id '@rpath/libLeap.dylib' $libdir/libLeap.dylib
elif [[ "$ARCH" == "32" ]]; then
    libdir=lib/x86
else
    libdir=lib/x64
fi

mkdir -p "$PREFIX/lib"
install $libdir/libLeap.* "$PREFIX/lib/"

python "$RECIPE_DIR/setup.py" build install
