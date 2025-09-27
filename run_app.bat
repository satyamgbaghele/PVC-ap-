@echo off
echo Starting PVC Production Calculator...
echo.
echo Installing required packages...
pip install -r requirements.txt
echo.
echo Starting the application...
echo The application will open in your default web browser.
echo To stop the application, close this window or press Ctrl+C
echo.
python clculationsheet.py
pause
