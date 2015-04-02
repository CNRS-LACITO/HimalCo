REM # -*- coding: utf-8 -*-

REM # Go under dev/lib/lmf/ and launch this script using the following command:
REM # ./run_na.bat

REM # Results are available under dev/lib/lmf/user/na/result/ folder.

REM # LaTeX file is generated with sound records and with cross references
python user/na/alexis/run_na.py

REM # LaTeX file is generated without sound records and with cross references
REM #python user/na/alexis/run_na.py -a

REM # LaTeX file is generated with sound records and without cross references
REM #python user/na/alexis/run_na.py -c

REM # LaTeX file is generated without sound records and without cross references
REM #python user/na/alexis/run_na.py -a -c

REM # Generate PDF: add xelatex binary location to your PATH environment variable or set following variable
set target="C:/Program Files (x86)/MiKTeX 2.9/miktex/bin/xelatex.exe"
%target% -output-directory=user/na/result/ user/na/result/dictionary.tex
%target% -output-directory=user/na/result/ user/na/result/dictionary.tex
