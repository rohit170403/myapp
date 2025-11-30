# Convert to Android APK - Step by Step

## Method 1: WSL (Recommended)

### Step 1: Install WSL
1. Open PowerShell as **Administrator**
2. Run: `wsl --install`
3. Restart your computer
4. Set up Ubuntu username/password when prompted

### Step 2: Install Dependencies in WSL
Open WSL terminal and run:
```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install buildozer cython
```

### Step 3: Navigate to Project
```bash
cd /mnt/c/Users/ACER/Downloads/myapp
```

### Step 4: Build APK
```bash
buildozer android debug
```

### Step 5: Get Your APK
The APK will be in: `bin/myapp-0.1-debug.apk`

## Method 2: Online (If WSL fails)

1. Go to https://replit.com
2. Create new Python project
3. Upload all your files
4. Run in terminal:
```bash
pip install buildozer
buildozer android debug
```

## Install on Phone
1. Enable "Unknown Sources" in Android Settings > Security
2. Transfer APK to phone
3. Install the APK file

## Troubleshooting
- If build fails, try: `buildozer android clean`
- For permission errors: `chmod +x buildozer.spec`
- For Java errors: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`