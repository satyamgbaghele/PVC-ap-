# PVC Production Calculator - Client Setup Guide

## What You Need
- Windows computer
- Internet connection (for initial setup)
- Python installed on your computer

## Quick Start (Easiest Method)
1. **Download Python** (if not already installed):
   - Go to https://www.python.org/downloads/
   - Download Python 3.8 or newer
   - During installation, make sure to check "Add Python to PATH"

2. **Run the Application**:
   - Double-click on `run_app.bat`
   - The application will automatically install required packages and start
   - Your web browser will open automatically to http://127.0.0.1:5000

## Manual Setup (If needed)
1. Open Command Prompt (cmd)
2. Navigate to the application folder
3. Run: `pip install -r requirements.txt`
4. Run: `python clculationsheet.py`
5. Open your browser and go to: http://127.0.0.1:5000

## How to Use
1. Enter your values in the form fields
2. Click "Calculate" to see results
3. The application will show all calculated values

## Troubleshooting
- If you get "Python not found" error, install Python first
- If you get "pip not found" error, reinstall Python with "Add to PATH" checked
- If the browser doesn't open automatically, manually go to http://127.0.0.1:5000

## Files Included
- `clculationsheet.py` - Main application
- `requirements.txt` - Required Python packages
- `run_app.bat` - Easy startup script
- `templates/` - Web interface files
- `static/` - Styling and JavaScript files
