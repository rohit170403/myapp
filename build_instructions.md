# Build Instructions for Android APK

## Method 1: WSL (Recommended)
1. Install WSL: `wsl --install` (in PowerShell as Admin)
2. Restart computer
3. Copy project to WSL: `cp -r /mnt/c/Users/ACER/Downloads/myapp ~/`
4. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip git zip unzip openjdk-8-jdk
   pip3 install buildozer cython
   ```
5. Build APK: `buildozer android debug`

## Method 2: GitHub Codespaces
1. Push code to GitHub
2. Open in Codespaces
3. Run: `pip install buildozer && buildozer android debug`

## Method 3: Docker
1. Install Docker Desktop
2. Run: `docker build -t myapp . && docker run -v ${PWD}:/app myapp`

## Method 4: Online Services
- Use Replit, CodeSandbox, or similar online IDEs with Linux

## APK Location
After successful build: `bin/myapp-0.1-debug.apk`