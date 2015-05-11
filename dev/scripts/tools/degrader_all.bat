md degrades
for %%a in ("*.wav") do ffmpeg -i "%%a" -ar 22050 -ac 1 "degrades\%%~na.wav"
for %%a in ("*.wav") do ffmpeg -i "%%a" -ab 128k -ar 44100 "degrades\%%~na.mp3"
