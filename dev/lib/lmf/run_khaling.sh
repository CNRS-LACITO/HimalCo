#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./run_khaling.sh

# Results are available under dev/lib/lmf/user/khaling/result/ folder.

# LaTeX file is generated with sound records and with cross references
python user/khaling/guillaume/run_khaling.py

# LaTeX file is generated without sound records and with cross references
#python user/khaling/guillaume/run_khaling.py -a

# LaTeX file is generated with sound records and without cross references
#python user/khaling/guillaume/run_khaling.py -c

# LaTeX file is generated without sound records and without cross references
#python user/khaling/guillaume/run_khaling.py -a -c

# Generate PDF
xelatex -output-directory=user/khaling/result/ user/khaling/result/dictionary.tex >> /dev/null
xelatex -output-directory=user/khaling/result/ user/khaling/result/dictionary.tex >> /dev/null
