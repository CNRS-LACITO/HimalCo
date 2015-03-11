#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./run_khaling.sh

# Results are available under dev/lib/lmf/user/guillaume/ folder.

# LaTeX file is generated with sound records and with cross references
#python user/guillaume/run_khaling.py

# LaTeX file is generated without sound records and with cross references
#python user/guillaume/run_khaling.py -a

# LaTeX file is generated with sound records and without cross references
#python user/guillaume/run_khaling.py -c

# LaTeX file is generated without sound records and without cross references
python user/guillaume/run_khaling.py -a -c

# Generate PDF
/usr/texbin/xelatex -output-directory=user/guillaume/ user/guillaume/Dictionary.tex >> /dev/null
/usr/texbin/xelatex -output-directory=user/guillaume/ user/guillaume/Dictionary.tex >> /dev/null
