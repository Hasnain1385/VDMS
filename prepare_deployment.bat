@echo off
echo Preparing deployment packages...

:: Clean up existing directories
echo Cleaning up existing directories...
rmdir /s /q windows 2>nul
rmdir /s /q linux 2>nul
rmdir /s /q macos 2>nul

:: Create necessary directories
echo Creating directories...
mkdir windows\app
mkdir linux\app
mkdir macos\app

:: Copy main application files
echo Copying application files...
copy /Y app.py windows\app\
copy /Y app.py linux\app\
copy /Y app.py macos\app\

copy /Y config.py windows\app\
copy /Y config.py linux\app\
copy /Y config.py macos\app\

xcopy /E /I /Y templates windows\app\templates\
xcopy /E /I /Y templates linux\app\templates\
xcopy /E /I /Y templates macos\app\templates\

xcopy /E /I /Y static windows\app\static\
xcopy /E /I /Y static linux\app\static\
xcopy /E /I /Y static macos\app\static\

copy /Y requirements.txt windows\app\
copy /Y requirements.txt linux\app\
copy /Y requirements.txt macos\app\

:: Copy platform-specific files
echo Copying platform-specific files...
copy /Y vehicle_management.spec windows\app\

:: Copy installation files to each platform folder
echo Copying installation files...
copy /Y windows\install.bat windows\
copy /Y windows\README.md windows\

copy /Y linux\install.sh linux\
copy /Y linux\README.md linux\

copy /Y macos\install.sh macos\
copy /Y macos\README.md macos\

:: Create data and logs directories in each platform folder
echo Creating data and logs directories...
mkdir windows\app\data
mkdir linux\app\data
mkdir macos\app\data

mkdir windows\app\logs
mkdir linux\app\logs
mkdir macos\app\logs

:: Verify files exist
echo Verifying files...
dir windows\app\requirements.txt
dir linux\app\requirements.txt
dir macos\app\requirements.txt

:: Create zip files
echo Creating deployment packages...
powershell Compress-Archive -Path windows\* -DestinationPath BismillahMotors_Windows.zip -Force
powershell Compress-Archive -Path linux\* -DestinationPath BismillahMotors_Linux.zip -Force
powershell Compress-Archive -Path macos\* -DestinationPath BismillahMotors_macOS.zip -Force

echo Deployment packages created successfully!
echo You can find the zip files in the root directory.
echo.
echo Folder structure for each platform:
echo Windows:
echo   - app/
echo     - app.py
echo     - config.py
echo     - templates/
echo     - static/
echo     - requirements.txt
echo     - vehicle_management.spec
echo     - data/
echo     - logs/
echo   - install.bat
echo   - README.md
echo.
echo Linux/macOS:
echo   - app/
echo     - app.py
echo     - config.py
echo     - templates/
echo     - static/
echo     - requirements.txt
echo     - data/
echo     - logs/
echo   - install.sh
echo   - README.md
pause 