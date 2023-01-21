import time
import subprocess

while True:
  subprocess.call(['sh', 'ss8.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '18.py'])
  subprocess.call(['nohup', 'python3', '20.py'])
  break