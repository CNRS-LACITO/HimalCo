for %%a in ("*.wav") do ffmpeg -i "%%a" -ab 128k -ar 44100 "%%~na.mp3"
