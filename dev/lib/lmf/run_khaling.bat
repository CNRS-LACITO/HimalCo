REM # -*- coding: utf-8 -*-

REM # Go under dev/lib/lmf/ and launch this script using the following command:
REM # run_khaling.bat

REM # Results are available under dev/lib/lmf/user/guillaume/ folder.

REM # LaTeX file is generated with sound records and with cross references
REM #python user/guillaume/run_khaling.py

REM # LaTeX file is generated without sound records and with cross references
REM #python user/guillaume/run_khaling.py -a

REM # LaTeX file is generated with sound records and without cross references
REM #python user/guillaume/run_khaling.py -c

REM # LaTeX file is generated without sound records and without cross references
python user/guillaume/run_khaling.py 

REM # Generate PDF
C:/texlive/2013/bin/win32/xelatex.exe -output-directory=user/guillaume/ user/guillaume/Dictionary.tex
C:/texlive/2013/bin/win32/xelatex.exe -output-directory=user/guillaume/ user/guillaume/Dictionary.tex
