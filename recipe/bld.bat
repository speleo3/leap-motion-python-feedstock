cd LeapSDK

if "%ARCH%"=="32" (
    set libdir=lib\x86
) else (
    set libdir=lib\x64
)

copy "%libdir%\Leap.dll" "%LIBRARY_BIN%"\

"%PYTHON%" "%RECIPE_DIR%\setup.py" build install
if errorlevel 1 exit 1
