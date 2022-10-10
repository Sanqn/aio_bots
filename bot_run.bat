@echo off

call %~dp0aio_bots\venv\Scripts\activate.ps1

cd %~dp0aio_bots

set TOKEN=5791794596:AAHJ-zoS8V2FtbY1yltmB-Lht0cYDT6g-lw

python aiobot_teleg.py

pause