#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./run_na.sh

# Results are available under dev/lib/lmf/user/na/result/ folder.

# LaTeX file is generated with sound records and with cross references
#python user/na/alexis/run_na.py

# LaTeX file is generated without sound records and with cross references
#python user/na/alexis/run_na.py -a

# LaTeX file is generated with sound records and without cross references
#python user/na/alexis/run_na.py -c

# LaTeX file is generated without sound records and without cross references
python user/na/alexis/run_na.py -a -c

# Generate PDF
/usr/texbin/xelatex -output-directory=user/na/result/ user/na/result/dictionary.tex >> /dev/null
/usr/texbin/xelatex -output-directory=user/na/result/ user/na/result/dictionary.tex >> /dev/null
