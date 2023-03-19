import subprocess
import time
import os
import win32api

# Set the source and destination paths
user = subprocess.check_output(["echo", "%userprofile%"], shell=True).decode().strip()
src = 'input.wav'
dst = os.path.join(user, 'input.wav')
src2 = 'output.wav'
dst2 = os.path.join(user, 'output.wav')

# Run the xcopy command
subprocess.run(['xcopy', src, user, '/i', '/y'], shell=True)
subprocess.run(['xcopy', src2, user, '/i', '/y'], shell=True)

dconnect = 'HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceDisconnect\.Current'
connect = 'HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceConnect\.Current'

# Run the reg add command
subprocess.run(['reg', 'add', connect, '/t', 'REG_SZ', '/d', dst, '/f'], shell=True)
subprocess.run(['reg', 'add', dconnect, '/t', 'REG_SZ', '/d', dst2, '/f'], shell=True)

