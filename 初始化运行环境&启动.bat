::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDpQQQ2MNXiuFLQI5/rHy++UqVkSRN4HNa3UzjNnyGbvJsMQox/WMEZi1ckDGFZ0fwaufRt04V5Qs3KMMtDVj4oJt81ODc7c7e2rd+sRYKzVr1aqeYWGI+87FoWxmr0VsQ==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
title Select Mode
echo https://mirrors.huaweicloud.com/python/3.13.0/python-3.13.0rc3.exe
echo If you was not install python,you can copy link to download and install
echo 0 = Initialization
echo 1 = Run QQ Bot
set /p input=(Default=0):
if "%input%" == "1" goto run

cls
title Updating pip...
python -m pip install --upgrade pip
echo pip was successfully installed? If so, please press any key to continue.Or not,please close the window
pause >nul

cls
echo Now Installing Runtime Libraries...
title Installing websockets lib...
pip install websockets
title Installing asyncio lib...
pip install asyncio
title Installing requests lib...
pip install requests
title Installing psutil lib...
pip install psutil
title Installing mcrcon lib...
pip install mcrcon
title Installing msvcrt lib...
pip install msvcrt
title Installing atexit lib...
pip install atexit
title Installing rcon lib...
pip install rcon
title Installing pyotp lib...
pip install pyotp
title Installing platform lib...
pip install platform
title Installing pywinrm lib...
pip install pywinrm
title Installing mcstatus lib...
pip install mcstatus

cls
title Successfully

echo Done!
echo You can close the window,or press any key to continue to run bot script.
pause >nul

:run
title Running QQ Bot
cls
python bot.py
title Closed
echo Bot already closed!
pause
