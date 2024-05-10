@echo off
start pypolis.py
start music.wav

:loop
timeout /t 226 >nul
start music.wav
goto loop