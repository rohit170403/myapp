@echo off
echo Installing WSL...
wsl --install
echo.
echo After WSL installation and restart, run these commands in WSL:
echo.
echo sudo apt update
echo sudo apt install -y python3-pip git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
echo pip3 install buildozer cython
echo cd /mnt/c/Users/ACER/Downloads/myapp
echo buildozer android debug
echo.
pause