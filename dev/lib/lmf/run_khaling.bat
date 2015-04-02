REM # -*- coding: utf-8 -*-

REM # Go under dev/lib/lmf/ and launch this script using the following command:
REM # ./run_khaling.bat

REM # Results are available under dev/lib/lmf/user/khaling/result/ folder.

REM # LaTeX file is generated with sound records and with cross references
python user/khaling/guillaume/run_khaling.py

REM # LaTeX file is generated without sound records and with cross references
REM #python user/khaling/guillaume/run_khaling.py -a

REM # LaTeX file is generated with sound records and without cross references
REM #python user/khaling/guillaume/run_khaling.py -c

REM # LaTeX file is generated without sound records and without cross references
REM #python user/khaling/guillaume/run_khaling.py -a -c

REM # Generate PDF: add xelatex binary location to your PATH environment variable
xelatex.exe -output-directory=user/khaling/result/ user/khaling/result/dictionary.tex
xelatex.exe -output-directory=user/khaling/result/ user/khaling/result/dictionary.tex
