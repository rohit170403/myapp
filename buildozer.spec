[app]
title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy,kivymd

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.arch = arm64-v8a