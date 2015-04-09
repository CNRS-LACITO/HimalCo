:: -*- coding: utf-8 -*-

:: Go under dev/lib/lmf/ and launch this script using the following command:
:: ./run_japhug.bat

:: Results are available under dev/lib/lmf/user/japhug/result/ folder.

:: LaTeX file is generated with sound records and with cross references
python user/japhug/guillaume/run_japhug.py

:: LaTeX file is generated without sound records and with cross references
::python user/japhug/guillaume/run_japhug.py -a

:: LaTeX file is generated with sound records and without cross references
::python user/japhug/guillaume/run_japhug.py -c

:: LaTeX file is generated without sound records and without cross references
::python user/japhug/guillaume/run_japhug.py -a -c

:: Generate PDF: add xelatex binary location to your PATH environment variable
xelatex.exe -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex
xelatex.exe -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex
