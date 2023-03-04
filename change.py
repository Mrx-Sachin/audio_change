import subprocess
import time
import os
import ctypes
# Set the source and destination paths
user=r"" 
user = subprocess.check_output(["echo", "%userprofile%"],shell=True,text=True  )

'''enter your address use "echo %USERPROFILE% " in cmd to get address '''
src = 'input.wav'
dst = '%USERPROFILE%\input.wav'
src2 = 'output.wav'
dst2 = '%USERPROFILE%\output.wav'
# Run the xcopy command
subprocess.run(['xcopy', src, user, '/i', '/y'],shell=True)
subprocess.run(['xcopy', src2, user, '/i', '/y'],shell=True)

dconnect = 'HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceDisconnect\.Current'
connect = 'HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceConnect\.Current'

# Run the @reg add command

subprocess.run(['@reg', 'add', connect, '/t', 'REG_SZ', '/d', dst, '/f'],shell=True)
subprocess.run(['@reg', 'add', dconnect, '/t', 'REG_SZ', '/d', dst2, '/f'],shell=True)



def changewallpaper(filepath):
    pwd=""
    pwd=subprocess.check_output(['cd'],shell=True,text=True)
    pwd=pwd[:-1]
    imgpath = os.path.join(pwd, filepath)
    print(imgpath)
    if os.path.exists(imgpath):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, imgpath, 0)
            print("Wallpaper set successfully")
            print(filepath)
            print(imgpath)
        except:
            print("Error setting wallpaper")
    else:
        print(f"Image not found: {imgpath}")
path = 'magic.jpg'
changewallpaper(path)



time.sleep(5)

