#/bin/bash
@echo off
set /p input_file="C:\cygwin64\home\bcz\Maktabsherif\MaktabsharifMiniProject3-1\Icons.txt"
set /p output_dir="C:\cygwin64\home\bcz\Maktabsherif\MaktabsharifMiniProject3-1\front\Icones"

for /f %%i in (%input_file%) do (
    copy "%%i" "%output_dir%"
)

echo All images have been copied to the icon directory.
