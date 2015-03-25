REM # -*- coding: utf-8 -*-

REM # Go under dev/lib/lmf/ and launch this script using the following command:
REM # ./run_japhug.bat

REM # Results are available under dev/lib/lmf/user/japhug/result/ folder.

REM # LaTeX file is generated with sound records and with cross references
REM #python user/japhug/guillaume/run_japhug.py

REM # LaTeX file is generated without sound records and with cross references
REM #python user/japhug/guillaume/run_japhug.py -a

REM # LaTeX file is generated with sound records and without cross references
REM #python user/japhug/guillaume/run_japhug.py -c

REM # LaTeX file is generated without sound records and without cross references
python user/japhug/guillaume/run_japhug.py -a -c

REM # Generate PDF
C:/texlive/2013/bin/win32/xelatex.exe -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex
C:/texlive/2013/bin/win32/xelatex.exe -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex
