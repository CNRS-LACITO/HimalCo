#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./run_japhug.sh

# Results are available under dev/lib/lmf/user/japhug/result/ folder.

# LaTeX file is generated with sound records and with cross references
python user/japhug/guillaume/run_japhug.py

# LaTeX file is generated without sound records and with cross references
#python user/japhug/guillaume/run_japhug.py -a

# LaTeX file is generated with sound records and without cross references
#python user/japhug/guillaume/run_japhug.py -c

# LaTeX file is generated without sound records and without cross references
#python user/japhug/guillaume/run_japhug.py -a -c

# Generate PDF
xelatex -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex >> /dev/null
xelatex -output-directory=user/japhug/result/ user/japhug/result/dictionary.tex >> /dev/null
