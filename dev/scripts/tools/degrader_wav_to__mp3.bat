for %%a in ("C:\Users\crlao\Documents\GitHub\HimalCo\dict\japhug\data\audio\new\*.wav") do ffmpeg -i "%%a" -ab 128k -ar 22005 "C:\Users\crlao\Desktop\journee\%%~na.mp3"
