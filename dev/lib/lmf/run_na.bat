:: -*- coding: utf-8 -*-

:: Go under dev/lib/lmf/ and launch this script using the following command:
:: ./run_na.bat

:: Results are available under dev/lib/lmf/user/na/result/ folder.

:: LaTeX file is generated with sound records and with cross references
::python user/na/alexis/run_na.py

:: LaTeX file is generated without sound records and with cross references
python user/na/alexis/run_na.py -a > log.txt

:: LaTeX file is generated with sound records and without cross references
::python user/na/alexis/run_na.py -c

:: LaTeX file is generated without sound records and without cross references
::python user/na/alexis/run_na.py -a -c

:: Generate PDF: add xelatex binary location to your PATH environment variable or set following variable
:: Path :
set target="C:/Program Files (x86)/MiKTeX 2.9/miktex/bin/xelatex.exe"
%target% -output-directory=user/na/result/ user/na/result/dictionary_eng.tex --halt-on-error=N
%target% -output-directory=user/na/result/ user/na/result/dictionary_eng.tex --halt-on-error=N
%target% -output-directory=user/na/result/ user/na/result/dictionary_fra.tex --halt-on-error=N
%target% -output-directory=user/na/result/ user/na/result/dictionary_fra.tex --halt-on-error=N
