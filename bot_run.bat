@echo off

call %~dp0aio_bots\venv\Scripts\activate

cd %~dp0aio_bots

python aiobot_teleg.py

pause
